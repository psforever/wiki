"""Write redirect stubs so the URLs of renamed and moved wiki pages keep working.

A few pages were renamed (their old file names can't be checked out on Windows)
or moved to another category. Run this after `zensical build`: for each old URL
in RENAMED it writes a small HTML page that forwards to the new one, keeping any
#anchor. It never overwrites a real page.

    python scripts/redirects.py            # uses site_dir and site_url from zensical.toml
    python scripts/redirects.py path/to/site
"""

import html
import posixpath
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Old URL -> new URL, both relative to the site root. Add an entry here when
# you rename or move a page.
RENAMED = {
    'archive/outfits/666th_Spec._Ops_"Devil_Dogs"/': "archive/outfits/666th_Spec._Ops_Devil_Dogs/",
    'archive/outfits/Fanteria_dello_Spazio_"FDS"/': "archive/outfits/Fanteria_dello_Spazio_FDS/",
    "archive/outfits/What_is_the_Matrix:param01/": "archive/outfits/What_is_the_Matrix_param01/",
    "terminology/Population_lock/": "terminology/Population_Lock_(Capacity)/",
    "AfterShock/": "terminology/AfterShock/",
}

STUB = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Page moved</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{canonical}">
<meta http-equiv="refresh" content="0; url={target}">
<script>location.replace({target_js} + location.hash);</script>
</head>
<body><p>This page has moved to <a href="{target}">{canonical}</a>.</p></body>
</html>
"""


def main() -> int:
    config = tomllib.loads((ROOT / "zensical.toml").read_text(encoding="utf-8"))["project"]
    site_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / config.get("site_dir", "site")
    site_url = config.get("site_url", "/").rstrip("/") + "/"
    if not (site_dir / "index.html").is_file():
        print(f"error: no built site in {site_dir}; run `zensical build` first", file=sys.stderr)
        return 1

    written = skipped = 0
    for old, new in sorted(RENAMED.items()):
        if not (site_dir / new / "index.html").is_file():
            print(f"error: redirect target {new} was not built", file=sys.stderr)
            return 1
        stub_path = site_dir / old / "index.html"
        if stub_path.exists():
            skipped += 1
            continue
        target = posixpath.relpath(new, old) + "/"
        try:
            stub_path.parent.mkdir(parents=True, exist_ok=True)
            stub_path.write_text(
                STUB.format(
                    canonical=html.escape(site_url + new),
                    target=html.escape(target),
                    target_js='"' + target.replace("\\", "\\\\").replace('"', '\\"') + '"',
                ),
                encoding="utf-8",
            )
            written += 1
        except OSError:
            # Some old URLs contain characters a Windows filesystem rejects.
            skipped += 1
    print(f"Wrote {written} redirect stubs for renamed pages ({skipped} skipped)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
