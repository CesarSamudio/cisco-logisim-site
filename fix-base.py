"""
fix-base.py — Reescribe las URLs absolutas del dist/ para que funcionen
bajo el subpath /cisco-logisim-site/ en GitHub Pages.

Reescribe:
  - src="/images/foo.jpg"  → src="/cisco-logisim-site/images/foo.jpg"
  - src="/_astro/foo.css"   → src="/cisco-logisim-site/_astro/foo.css"
  - href="/cisco-it"        → href="/cisco-logisim-site/cisco-it"
  - href="/#anchor"         → href="/cisco-logisim-site/#anchor"
  - href="/"                → href="/cisco-logisim-site/"

NO toca:
  - href="https://..."  (links externos)
  - href="#algo"        (anchor puro en la misma página)
  - src="data:..."      (data URIs)

Uso: python3 fix-base.py [BASE]
Por defecto BASE=/cisco-logisim-site
"""
import re
import sys
from pathlib import Path

BASE = sys.argv[1] if len(sys.argv) > 1 else "/cisco-logisim-site"
DIST = Path(__file__).parent / "dist"

# Captura: src o href con path absoluto que NO empieza con http:, https:, data: ni #
# Permitimos: /, /foo, /foo/bar, /#anchor, /foo#anchor
PATTERN = re.compile(
    r'((?:src|href))="(/+(?!/)[^"]*)"'
)


def rewrite(match: re.Match) -> str:
    attr = match.group(1)
    path = match.group(2)
    # Si ya tiene la base al frente, no duplicar
    if path.startswith(BASE + "/") or path == BASE:
        return f'{attr}="{path}"'
    new = BASE + path
    return f'{attr}="{new}"'


def process_html(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    new_text, n = PATTERN.subn(rewrite, text)
    if n > 0:
        path.write_text(new_text, encoding="utf-8")
    return n


def main() -> None:
    if not DIST.exists():
        sys.exit(f"❌ No existe {DIST}. Corré `npm run build` primero.")
    total = 0
    files = 0
    for html in sorted(DIST.rglob("*.html")):
        n = process_html(html)
        if n > 0:
            total += n
            files += 1
            print(f"  ✓ {html.relative_to(DIST)}: {n} URLs reescritas")
    print(f"\n✅ Listo: {total} URLs reescritas en {files} archivos HTML.")
    print(f"   Base aplicada: {BASE}")


if __name__ == "__main__":
    main()