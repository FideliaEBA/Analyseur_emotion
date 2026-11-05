"""Convertit data/fiches_emotions.json en emotions.js pour l'interface web."""
import json
from pathlib import Path

fiches = json.loads(Path("data/fiches_emotions.json").read_text(encoding="utf-8"))
Path("emotions.js").write_text("const EMOTIONS = " + json.dumps(fiches, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")
print(f"{len(fiches)} catégories d'émotions exportées dans emotions.js")
