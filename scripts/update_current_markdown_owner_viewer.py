#!/usr/bin/env python3
"""Refresh the shared markdown owner viewer and rewrite current HTML links to use it."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path
from urllib.parse import parse_qs, quote, urlparse


ROOT = Path(__file__).resolve().parents[1]
CURRENT_VIEWS = ROOT / "views" / "current"
VIEWER_PATH = CURRENT_VIEWS / "markdown-owner-viewer.html"
VIEWER_LENS_ID = "lens-markdown-owner-viewer-current"
REPO_MD_LINK = re.compile(r"""(?<![\w-])href=(?P<q>['"])(?P<href>[^'"]+?\.md)(?P=q)""")
VIEWER_LINK = re.compile(
    r"""(?<![\w-])href=(?P<q>['"])(?P<href>[^'"]*markdown-owner-viewer[^'"]*)(?P=q)"""
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def markdown_title(path: Path) -> str:
    for line in read_text(path).splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def js_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False).replace("<", "\\u003c")


def normalize_md_target(source_html: Path, href: str) -> str | None:
    if href.startswith(("http://", "https://", "mailto:", "#")):
        return None
    candidate = (source_html.parent / href).resolve()
    try:
        rel = candidate.relative_to(ROOT)
    except ValueError:
        return None
    if candidate.suffix != ".md" or not candidate.exists():
        return None
    return rel.as_posix()


def extract_viewer_target(href: str) -> str | None:
    parsed = urlparse(href)
    params = parse_qs(parsed.query)
    target = params.get("path", [])
    return target[0] if target else None


def current_html_files() -> list[Path]:
    return sorted(
        path
        for path in CURRENT_VIEWS.rglob("*.html")
        if ".exports" not in path.parts and path.resolve() != VIEWER_PATH.resolve()
    )


def owner_paths_from_html(path: Path) -> set[str]:
    text = read_text(path)
    owners: set[str] = set()
    for match in REPO_MD_LINK.finditer(text):
        target = normalize_md_target(path, match.group("href"))
        if target:
            owners.add(target)
    for _, href in re.findall(r"""href=(['"])([^'"]+)['"]""", text):
        if "markdown-owner-viewer" not in href:
            continue
        target = extract_viewer_target(href)
        if target:
            owners.add(target)
    return owners


def viewer_href(base: str, owner_path: str, version: str) -> str:
    return f'{base}?v={quote(version, safe="")}&path={quote(owner_path, safe="/")}'


def rewrite_html_links(path: Path, link_version: str, dry_run: bool) -> tuple[bool, set[str]]:
    text = read_text(path)
    owners = owner_paths_from_html(path)
    local_viewer = Path(os.path.relpath(VIEWER_PATH, start=path.parent)).as_posix()
    changed = False

    def replace_md(match: re.Match[str]) -> str:
        nonlocal changed
        target = normalize_md_target(path, match.group("href"))
        if not target:
            return match.group(0)
        local = viewer_href(local_viewer, target, link_version)
        changed = True
        return f'href="{local}"'

    rewritten = REPO_MD_LINK.sub(replace_md, text)
    rewritten = re.sub(r"""\s+data-share-href=(['"])[^'"]*\1""", "", rewritten)
    rewritten = re.sub(
        r"""\s*<script id="markdown-owner-viewer-share-swap">.*?</script>\s*""",
        "\n",
        rewritten,
        flags=re.DOTALL,
    )

    def replace_viewer(match: re.Match[str]) -> str:
        nonlocal changed
        target = extract_viewer_target(match.group("href"))
        if not target:
            return match.group(0)
        changed = True
        return f'href="{viewer_href(local_viewer, target, link_version)}"'

    rewritten = VIEWER_LINK.sub(replace_viewer, rewritten)
    if rewritten != text:
        changed = True
        if not dry_run:
            write_text(path, rewritten)
    return changed, owners


def viewer_css() -> str:
    return """
    :root{
      color-scheme:light;
      --ink:#1d231e; --muted:#5f675d; --line:#dbe1d7; --line2:#c7d0c4; --paper:#ffffff; --wash:#f3f6f0;
      --panel:#f9fbf7; --teal:#0b6b57; --blue:#255f9c; --amber:#9b6616; --red:#a0342f;
      font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;
    }
    *{box-sizing:border-box;}
    body{margin:0;background:linear-gradient(180deg,#eef3ec 0%,#f7f9f4 180px,#f5f7f2 100%);color:var(--ink);}
    .wrap{width:min(1260px,calc(100vw - 32px));margin:0 auto;}
    header{padding:24px 0 18px;}
    .hero{background:rgba(255,255,255,.82);backdrop-filter:blur(8px);border:1px solid rgba(27,35,30,.08);border-radius:18px;padding:18px 20px;box-shadow:0 16px 50px rgba(31,38,33,.08);}
    .eyebrow{font-size:12px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--teal);}
    .hero h1{margin:8px 0 0;font-size:30px;line-height:1.2;}
    .meta{display:flex;gap:10px;flex-wrap:wrap;margin-top:12px;}
    .pill{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--line);background:var(--paper);border-radius:999px;padding:6px 10px;font-size:12px;color:var(--muted);}
    .pill.warn{background:#fbefd8;color:var(--amber);border-color:#ecd39e;}
    .actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;}
    .btn{display:inline-flex;align-items:center;justify-content:center;border:1px solid var(--line2);background:var(--paper);color:var(--ink);border-radius:10px;padding:9px 12px;font-size:13px;text-decoration:none;}
    .btn.primary{background:#0b6b57;color:#fff;border-color:#0b6b57;}
    .btn.warn{background:#fbefd8;color:#9b6616;border-color:#ecd39e;}
    main{padding:0 0 34px;}
    .layout{display:grid;grid-template-columns:320px minmax(0,1fr);gap:18px;align-items:start;}
    .panel,.frame{background:var(--paper);border:1px solid var(--line);border-radius:18px;box-shadow:0 20px 60px rgba(31,38,33,.08);overflow:hidden;}
    .panel-head,.frame-head{padding:14px 18px;border-bottom:1px solid var(--line);background:linear-gradient(180deg,#fbfcf8 0%,#f6f8f3 100%);}
    .panel-title{font-size:14px;font-weight:700;}
    .panel-sub{margin-top:4px;font-size:12px;color:var(--muted);}
    .owner-list{padding:10px;display:flex;flex-direction:column;gap:8px;max-height:calc(100vh - 220px);overflow:auto;}
    .owner-link{display:block;width:100%;border:1px solid var(--line);border-radius:14px;background:#fbfcfa;padding:12px 13px;text-decoration:none;color:var(--ink);font:inherit;text-align:left;cursor:pointer;}
    .owner-link:hover{border-color:#b7c7b4;background:#f7fbf6;}
    .owner-link.active{border-color:#0b6b57;background:#eef8f4;box-shadow:inset 0 0 0 1px rgba(11,107,87,.14);}
    .owner-name{font-size:14px;font-weight:700;line-height:1.35;}
    .owner-path{margin-top:5px;font-size:12px;color:var(--muted);word-break:break-all;font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;}
    .frame-path{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px;color:var(--muted);word-break:break-all;}
    .frame-body{padding:22px 24px 30px;}
    .empty{padding:20px;border:1px dashed var(--line2);border-radius:12px;background:var(--panel);font-size:14px;color:var(--muted);}
    .md-prose{font-size:15px;line-height:1.75;color:var(--ink);}
    .md-prose h1,.md-prose h2,.md-prose h3,.md-prose h4,.md-prose h5,.md-prose h6{margin:1.35em 0 .55em;line-height:1.26;color:#15221b;}
    .md-prose h1:first-child,.md-prose h2:first-child,.md-prose h3:first-child,.md-prose h4:first-child,.md-prose h5:first-child,.md-prose h6:first-child{margin-top:0;}
    .md-prose h1{font-size:31px;}
    .md-prose h2{font-size:25px;}
    .md-prose h3{font-size:20px;}
    .md-prose h4{font-size:17px;}
    .md-prose p{margin:.78em 0;}
    .md-prose ul,.md-prose ol{margin:.75em 0 .95em 1.35em;padding:0;}
    .md-prose li{margin:.24em 0;}
    .md-prose blockquote{margin:1em 0;padding:.3em 0 .3em 14px;border-left:4px solid #c9dbc6;color:#4f5b52;background:#f8fbf6;}
    .md-prose hr{border:0;border-top:1px solid var(--line);margin:1.2em 0;}
    .md-prose pre{margin:1em 0;padding:14px 16px;border-radius:12px;background:#1f2823;color:#edf6ef;overflow:auto;font-size:13px;line-height:1.58;}
    .md-prose code{padding:.12em .35em;border-radius:6px;background:#eef2ea;color:#183126;font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;}
    .md-prose pre code{padding:0;background:transparent;color:inherit;}
    .md-prose table{width:100%;border-collapse:collapse;margin:1em 0;font-size:14px;}
    .md-prose th,.md-prose td{border:1px solid var(--line);padding:8px 10px;vertical-align:top;}
    .md-prose th{background:#f5f7f1;text-align:left;}
    .md-prose a{color:var(--blue);}
    @media (max-width:980px){
      .layout{grid-template-columns:1fr;}
      .owner-list{max-height:none;}
    }
    @media (max-width:760px){
      .wrap{width:min(100vw - 20px,1260px);}
      .hero h1{font-size:24px;}
      .frame-body{padding:18px 16px 24px;}
    }
    @page{size:A4;margin:14mm;}
    @media print{
      body{background:#fff;}
      .wrap{width:auto;margin:0;}
      .layout{grid-template-columns:1fr;}
      .panel{display:none;}
      .hero,.frame{box-shadow:none;}
      .actions{display:none;}
    }
    """


def viewer_script() -> str:
    return """
    const sourcePack = __SOURCE_PACK__;
    const viewerVersion = encodeURIComponent(sourcePack.generated_at || sourcePack.source_revision || "current");
    const params = new URLSearchParams(window.location.search);
    const requestedPath = params.get("path") || "";
    const pathNode = document.getElementById("path");
    const titleNode = document.getElementById("title");
    const bodyNode = document.getElementById("body");
    const rawLink = document.getElementById("rawLink");
    const fallbackLink = document.getElementById("fallbackLink");
    const listNode = document.getElementById("ownerList");
    function escapeHtml(value) {
      return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
    }
    function renderInline(text) {
      let out = escapeHtml(text);
      out = out.replace(/`([^`]+)`/g, "<code>$1</code>");
      out = out.replace(/\\[([^\\]]+)\\]\\(([^)]+)\\)/g, (_match, label, href) => {
        return `<code>[${label}](${href})</code>`;
      });
      out = out.replace(/\\*\\*([^*]+)\\*\\*/g, "<strong>$1</strong>");
      out = out.replace(/\\*([^*]+)\\*/g, "<em>$1</em>");
      out = out.replace(/\\[\\[([^\\]]+)\\]\\]/g, "<code>[[$1]]</code>");
      return out;
    }
    function renderMarkdown(md) {
      const lines = String(md || "").replace(/\\r\\n/g, "\\n").split("\\n");
      const out = [];
      let i = 0;
      let inCode = false;
      let code = [];
      let listType = null;
      function closeList() {
        if (!listType) return;
        out.push(listType === "ol" ? "</ol>" : "</ul>");
        listType = null;
      }
      while (i < lines.length) {
        const line = lines[i];
        if (line.trim().startsWith("```")) {
          closeList();
          if (inCode) {
            out.push("<pre><code>" + escapeHtml(code.join("\\n")) + "</code></pre>");
            inCode = false;
            code = [];
          } else {
            inCode = true;
            code = [];
          }
          i += 1;
          continue;
        }
        if (inCode) {
          code.push(line);
          i += 1;
          continue;
        }
        if (!line.trim()) {
          closeList();
          i += 1;
          continue;
        }
        const heading = line.match(/^(#{1,6})\\s+(.*)$/);
        if (heading) {
          closeList();
          const level = heading[1].length;
          out.push(`<h${level}>${renderInline(heading[2])}</h${level}>`);
          i += 1;
          continue;
        }
        if (/^(-{3,}|\\*{3,}|_{3,})\\s*$/.test(line.trim())) {
          closeList();
          out.push("<hr>");
          i += 1;
          continue;
        }
        if (line.trim().startsWith(">")) {
          closeList();
          const quote = [];
          while (i < lines.length && lines[i].trim().startsWith(">")) {
            quote.push(lines[i].replace(/^\\s*>\\s?/, ""));
            i += 1;
          }
          out.push("<blockquote>" + quote.map((part) => `<p>${renderInline(part)}</p>`).join("") + "</blockquote>");
          continue;
        }
        const ordered = line.match(/^\\s*(\\d+)\\.\\s+(.*)$/);
        if (ordered) {
          if (listType !== "ol") {
            closeList();
            listType = "ol";
            out.push("<ol>");
          }
          out.push(`<li>${renderInline(ordered[2])}</li>`);
          i += 1;
          continue;
        }
        const bullet = line.match(/^\\s*[-*]\\s+(.*)$/);
        if (bullet) {
          if (listType !== "ul") {
            closeList();
            listType = "ul";
            out.push("<ul>");
          }
          out.push(`<li>${renderInline(bullet[1])}</li>`);
          i += 1;
          continue;
        }
        closeList();
        const tableLines = [];
        let j = i;
        while (j < lines.length && lines[j].includes("|")) {
          tableLines.push(lines[j]);
          j += 1;
        }
        if (
          tableLines.length >= 2 &&
          /^\\s*\\|?(\\s*:?-+:?\\s*\\|)+\\s*:?-+:?\\s*\\|?\\s*$/.test(tableLines[1])
        ) {
          const splitRow = (row) =>
            row
              .trim()
              .replace(/^\\|/, "")
              .replace(/\\|$/, "")
              .split("|")
              .map((cell) => cell.trim());
          const headers = splitRow(tableLines[0]);
          out.push("<table><thead><tr>" + headers.map((cell) => `<th>${renderInline(cell)}</th>`).join("") + "</tr></thead><tbody>");
          for (const row of tableLines.slice(2)) {
            const cells = splitRow(row);
            out.push("<tr>" + cells.map((cell) => `<td>${renderInline(cell)}</td>`).join("") + "</tr>");
          }
          out.push("</tbody></table>");
          i = j;
          continue;
        }
        out.push(`<p>${renderInline(line)}</p>`);
        i += 1;
      }
      closeList();
      return out.join("");
    }
    const available = sourcePack.items || {};
    const entries = Object.values(available).sort((a, b) => (a.owner_path || "").localeCompare(b.owner_path || "", "zh-Hans-CN"));
    function viewerUrl(ownerPath) {
      return `?v=${viewerVersion}&path=${encodeURIComponent(ownerPath)}`;
    }
    function renderOwner(ownerPath, updateUrl = false) {
      const chosen = available[ownerPath] || entries[0] || null;
      if (!chosen) {
        titleNode.textContent = "未收录任何 owner page";
        pathNode.textContent = "当前 source pack 为空";
        bodyNode.innerHTML = '<div class="empty">这个 viewer 还没有收进任何 markdown owner 页面。请先刷新相关 HTML lens。</div>';
        rawLink.style.display = "none";
        return;
      }
      titleNode.textContent = chosen.title || chosen.owner_path;
      pathNode.textContent = chosen.owner_path;
      bodyNode.innerHTML = `<div class="md-prose">${renderMarkdown(chosen.markdown || "")}</div>`;
      rawLink.href = chosen.raw_href || "#";
      fallbackLink.href = viewerUrl(chosen.owner_path);
      if (listNode) {
        listNode.querySelectorAll("[data-owner-path]").forEach((button) => {
          button.classList.toggle("active", button.dataset.ownerPath === chosen.owner_path);
        });
      }
      if (updateUrl && window.history && window.history.replaceState) {
        window.history.replaceState(null, "", viewerUrl(chosen.owner_path));
      }
    }
    if (listNode) {
      listNode.innerHTML = entries.map((item) => {
        return `<button type="button" class="owner-link" data-owner-path="${escapeHtml(item.owner_path)}">
          <div class="owner-name">${escapeHtml(item.title || item.owner_path)}</div>
          <div class="owner-path">${escapeHtml(item.owner_path)}</div>
        </button>`;
      }).join("");
      listNode.querySelectorAll("[data-owner-path]").forEach((button) => {
        button.addEventListener("click", () => {
          renderOwner(button.dataset.ownerPath || "", true);
        });
      });
    }
    renderOwner(requestedPath, false);
    """


def render_viewer(source_pack: dict[str, object]) -> str:
    script = viewer_script()
    script = script.replace("__SOURCE_PACK__", js_json(source_pack))
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Software Wiki Owner Markdown Viewer</title>
  <meta name="lens_id" content="{VIEWER_LENS_ID}">
  <meta name="lens_type" content="resource">
  <meta name="focus_object" content="owner page markdown reading surface for current HTML lenses">
  <meta name="generated_from" content="views/current/**/*.html">
  <meta name="evidence_boundary" content="viewer renders a controlled owner-page source pack; markdown owner pages remain source of truth; this local artifact is not publicly published">
  <meta name="output_mode" content="current html utility viewer">
  <meta name="export_profile" content="canonical HTML only; no PDF / PNG export required for this utility viewer">
  <meta name="print_profile" content="@page and @media print are declared for readable fallback printing">
  <meta name="equivalence_profile" content="canonical HTML / source / manifest render the same source pack; markdown owner pages remain source of truth">
  <meta name="default_auto_exports" content="not applicable; viewer is a utility page, not a problem-focused print lens">
  <meta name="conversation_png_preview" content="not applicable for utility viewer">
  <meta name="source_pack_contract" content="same source pack embedded in canonical HTML / source / manifest">
  <style>{viewer_css()}</style>
</head>
<body>
  <header class="wrap">
    <div class="hero">
      <div class="eyebrow">Owner Page Viewer</div>
      <h1 id="title">Markdown owner 预览</h1>
      <div class="meta">
        <span class="pill">viewer scope: current HTML lenses</span>
        <span class="pill">source of truth: markdown owner page</span>
        <span class="pill warn">local artifact; not publicly published</span>
      </div>
      <div class="actions">
        <a class="btn primary" id="rawLink" href="#" target="_blank" rel="noopener noreferrer">打开原始文件</a>
        <a class="btn" id="fallbackLink" href="markdown-owner-viewer.html">固定当前 viewer 入口</a>
      </div>
    </div>
  </header>
  <main class="wrap">
    <div class="layout">
      <aside class="panel">
        <div class="panel-head">
          <div class="panel-title">可切换 owner 页面</div>
          <div class="panel-sub">直接打开 viewer 也可以从这里切换，不依赖外层页面传参。</div>
        </div>
        <div class="owner-list" id="ownerList"></div>
      </aside>
      <section class="frame">
        <div class="frame-head">
          <div class="frame-path" id="path">等待选择 owner page…</div>
        </div>
        <div class="frame-body" id="body">
          <div class="empty">正在加载 owner page…</div>
        </div>
      </section>
    </div>
  </main>
  <script>(() => {{
{script}
  }})();</script>
</body>
</html>
"""


def git_revision() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def build_source_pack(owner_paths: set[str]) -> dict[str, object]:
    items: dict[str, object] = {}
    viewer_dir = VIEWER_PATH.parent
    for owner_path in sorted(owner_paths):
        abs_path = ROOT / owner_path
        if not abs_path.exists():
            continue
        items[owner_path] = {
            "owner_path": owner_path,
            "title": markdown_title(abs_path),
            "markdown": read_text(abs_path),
            "raw_href": Path(os.path.relpath(abs_path, start=viewer_dir)).as_posix(),
        }
    return {
        "generated_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "source_revision": git_revision(),
        "items": items,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="show planned changes without writing files")
    args = parser.parse_args()

    link_version = datetime.now().strftime("%Y%m%d%H%M%S")
    all_owners: set[str] = set()
    rewritten_files: list[str] = []

    for html_path in current_html_files():
        changed, owners = rewrite_html_links(html_path, link_version, dry_run=args.dry_run)
        all_owners.update(owners)
        if changed:
            rewritten_files.append(html_path.relative_to(ROOT).as_posix())

    source_pack = build_source_pack(all_owners)
    viewer_html = render_viewer(source_pack)
    viewer_changed = not VIEWER_PATH.exists() or read_text(VIEWER_PATH) != viewer_html
    if viewer_changed and not args.dry_run:
        write_text(VIEWER_PATH, viewer_html)

    print(f"viewer: {VIEWER_PATH.relative_to(ROOT).as_posix()} ({'changed' if viewer_changed else 'unchanged'})")
    print(f"owners packed: {len(source_pack['items'])}")
    if rewritten_files:
        print("rewritten html files:")
        for rel in rewritten_files:
            print(f"  - {rel}")
    else:
        print("rewritten html files: none")


if __name__ == "__main__":
    main()
