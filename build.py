"""Inline the per-manual graphs into index.html.  python3 build.py"""
import json, pathlib
HERE = pathlib.Path(__file__).parent
MANUALS = [  # key (URL #hash), pill label, full label, graph file
    ("h7",     "H7 head",     "H7 harvester head",                 "graphs/h7.json"),
    ("c50",    "C50 crane",   "C50 crane",                         "graphs/c50.json"),
    ("engine", "SK8W engine", "Scorpion King 8W engine (A011333)", "graphs/engine.json"),
]
out = [{"key": k, "short": s, "label": l, "data": json.loads((HERE / f).read_text(encoding="utf-8"))}
       for k, s, l, f in MANUALS]
tpl = (HERE / "_template.html").read_text(encoding="utf-8")
assert "/*__MANUALS__*/" in tpl
html = tpl.replace("/*__MANUALS__*/", json.dumps(out, ensure_ascii=False, separators=(",", ":")))
(HERE / "index.html").write_text(html, encoding="utf-8")
print(f"index.html: {len(html)/1024:.0f} KB, {len(out)} manuals")
