"""Inline the per-manual graphs into index.html.

    python3 build.py                      # public build: index.html, no manual links
    python3 build.py --protected DIR      # also write DIR/index.html whose panel links
                                          # "Open the manual at p. N" to DIR/manuals/<pdf>#page=N

The public build never links to the manuals, because no copy of them may be
published. The protected build is for the login-protected Cloudflare copy only:
upload DIR as a whole (index.html + manuals/), and only with Ponsse's agreement.
"""
import json, pathlib, shutil, sys
HERE = pathlib.Path(__file__).parent
MANUALS = [  # key (URL #hash), pill label, full label, graph file
    ("h7",     "H7 head",     "H7 harvester head",                 "graphs/h7.json"),
    ("c50",    "C50 crane",   "C50 crane",                         "graphs/c50.json"),
    ("engine", "SK8W engine", "Scorpion King 8W engine (A011333)", "graphs/engine.json"),
]
PDF_DIR = HERE / "../../download"        # where the source PDFs live locally (never published)

out = [{"key": k, "short": s, "label": l, "data": json.loads((HERE / f).read_text(encoding="utf-8"))}
       for k, s, l, f in MANUALS]
tpl = (HERE / "_template.html").read_text(encoding="utf-8")
assert "/*__MANUALS__*/" in tpl and "/*__PDF_BASE__*/" in tpl
data = json.dumps(out, ensure_ascii=False, separators=(",", ":"))

def render(pdf_base):
    return tpl.replace("/*__MANUALS__*/", data).replace("/*__PDF_BASE__*/", json.dumps(pdf_base))

html = render("")
(HERE / "index.html").write_text(html, encoding="utf-8")
print(f"index.html: {len(html)/1024:.0f} KB, {len(out)} manuals, no manual links")

if "--protected" in sys.argv:
    dest = pathlib.Path(sys.argv[sys.argv.index("--protected") + 1])
    (dest / "manuals").mkdir(parents=True, exist_ok=True)
    (dest / "index.html").write_text(render("manuals/"), encoding="utf-8")
    for m in out:
        src = PDF_DIR / m["data"]["meta"]["source"]
        shutil.copy(src, dest / "manuals" / src.name)
        print(f"  {src.name}: {src.stat().st_size/1e6:.1f} MB")
    print(f"{dest}/index.html: links to manuals/<pdf>#page=N — protected copy only")
