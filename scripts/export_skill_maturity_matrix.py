#!/usr/bin/env python3
"""Export the skill maturity matrix HTML to PNG and PDF.

The Playwright CLI does not expose printBackground / preferCSSPageSize, which
are required for the heatmap colors to survive PDF rendering. Use the API here
so the PDF and PNG stay visually equivalent to the canonical HTML.
"""

from __future__ import annotations

import shutil
import subprocess
import tempfile
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "views" / "current" / "governance" / "skill-maturity-matrix.html"
EXPORT_DIR = ROOT / "views" / ".exports"
PNG = EXPORT_DIR / "skill-maturity-matrix.png"
PDF = EXPORT_DIR / "skill-maturity-matrix.pdf"


def run(cmd: list[str], cwd: Path) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def main() -> int:
    if not HTML.is_file():
        raise SystemExit(f"missing canonical HTML: {HTML}")
    if not shutil.which("npm"):
        raise SystemExit("npm is required to run the Playwright export pipeline")

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="skill-maturity-export-") as temp:
        tempdir = Path(temp)
        script = tempdir / "export.js"
        script.write_text(
            textwrap.dedent(
                """
                const { chromium } = require("playwright");

                const [htmlUrl, pngPath, pdfPath] = process.argv.slice(2);

                (async () => {
                  const browser = await chromium.launch({ headless: true });
                  const page = await browser.newPage({
                    viewport: { width: 1600, height: 2600 },
                    deviceScaleFactor: 1
                  });
                  await page.goto(htmlUrl, { waitUntil: "load" });
                  await page.screenshot({ path: pngPath, fullPage: true });
                  await page.pdf({
                    path: pdfPath,
                    format: "A4",
                    landscape: true,
                    printBackground: true,
                    preferCSSPageSize: true
                  });
                  await browser.close();
                })().catch(error => {
                  console.error(error);
                  process.exit(1);
                });
                """
            ).strip()
            + "\n",
            encoding="utf-8",
        )
        run(["npm", "init", "-y"], cwd=tempdir)
        run(["npm", "install", "playwright"], cwd=tempdir)
        run(["node", str(script), HTML.as_uri(), str(PNG), str(PDF)], cwd=tempdir)

    print(f"updated {PNG}")
    print(f"updated {PDF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
