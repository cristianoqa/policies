from pathlib import Path

root = Path(r"D:\policies")

NOTICE = {
    "es": (
        "Memio discontinuada",
        "Esta app ya no forma parte del catálogo de Flow Home Apps.",
        "Volver al catálogo",
    ),
    "en": (
        "Memio discontinued",
        "This app is no longer part of the Flow Home Apps catalog.",
        "Back to catalog",
    ),
    "pt": (
        "Memio descontinuada",
        "Esta app já não faz parte do catálogo Flow Home Apps.",
        "Voltar ao catálogo",
    ),
}


def page(lang: str) -> str:
    title, body, link = NOTICE[lang]
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta http-equiv="refresh" content="5;url=https://cristianoqa.github.io/" />
  <link rel="canonical" href="https://cristianoqa.github.io/" />
</head>
<body style="font-family:system-ui;margin:2rem;max-width:36rem;line-height:1.5">
  <h1>{title}</h1>
  <p>{body}</p>
  <p><a href="https://cristianoqa.github.io/">{link}</a></p>
</body>
</html>
"""


files = {
    "memio-es.html": page("es"),
    "memio.html": page("en"),
    "memio-pt.html": page("pt"),
}

for name, content in files.items():
    for d in (root, root / "docs"):
        (d / name).write_text(content, encoding="utf-8")
        print("wrote", d / name)

for idx in (root / "index.html", root / "docs" / "index.html"):
    t = idx.read_text(encoding="utf-8")
    t2 = t.replace('<a href="./memio-es.html">Memio</a> ·', "").replace("  ·\n", "\n")
    idx.write_text(t2, encoding="utf-8")
    print("updated", idx)

# README
for readme in (root / "README.md", root / "docs" / "README.md"):
    lines = []
    for line in readme.read_text(encoding="utf-8").splitlines():
        if "Memio" in line or "memio" in line.lower():
            continue
        lines.append(line)
    if "discontinuada" not in "\n".join(lines).lower():
        # insert note after title block
        out = []
        inserted = False
        for line in lines:
            out.append(line)
            if not inserted and line.startswith("Sitio"):
                out.append("")
                out.append("Memio: **discontinuada** (páginas memio-* redirigen al catálogo).")
                inserted = True
        lines = out
    readme.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("updated", readme)

# Patch generator: skip memio()
gen = root / "scripts" / "generate_reinforced_policies.py"
if gen.exists():
    g = gen.read_text(encoding="utf-8")
    g2 = g.replace("    memio()\n", "    # memio()  # discontinuada\n")
    g2 = g2.replace("- Memio: memio-es.html / memio.html / memio-pt.html\n", "")
    gen.write_text(g2, encoding="utf-8")
    print("patched generator")

print("OK")
