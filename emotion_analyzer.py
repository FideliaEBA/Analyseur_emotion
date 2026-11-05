"""Moteur NLP d'analyse d'émotions et de sentiments.

Utilise TextBlob et TF-IDF / règles lexicographiques pour détecter les émotions dans un texte.

Utilisation :
    python emotion_analyzer.py
    python emotion_analyzer.py "J'adore ce projet, c'est vraiment génial !"
"""
import json
import sys
import unicodedata
import re
from pathlib import Path
from textblob import TextBlob

SEUIL_POLARITE_POSITIF = 0.1
SEUIL_POLARITE_NEGATIF = -0.1

def normaliser(texte: str) -> str:
    texte = unicodedata.normalize("NFD", texte.lower())
    texte = "".join(c for c in texte if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", " ", texte).strip()

class EmotionAnalyzer:
    def __init__(self, chemin_data: str = "data/fiches_emotions.json"):
        self.fiches = json.loads(Path(chemin_data).read_text(encoding="utf-8"))

    def analyser(self, texte: str) -> dict:
        blob = TextBlob(texte)
        polarite = float(blob.sentiment.polarity)
        subjectivite = float(blob.sentiment.subjectivity)
        
        texte_norm = normaliser(texte)

        # Détection de l'émotion dominante basée sur les mots-clés et le score de polarité
        scores_emotions = {}
        for f in self.fiches:
            mots = f["mots_cles"].split()
            count = sum(1 for m in mots if m in texte_norm)
            scores_emotions[f["id"]] = count

        emotion_detectee = max(scores_emotions, key=scores_emotions.get)
        
        # Secours basé sur la polarité si aucun mot-clé direct n'est trouvé
        if scores_emotions[emotion_detectee] == 0:
            if polarite > SEUIL_POLARITE_POSITIF:
                emotion_detectee = "joie"
            elif polarite < SEUIL_POLARITE_NEGATIF:
                emotion_detectee = "colere" if subjectivite > 0.5 else "tristesse"
            else:
                emotion_detectee = "neutre"

        fiche_resultat = next(f for f in self.fiches if f["id"] == emotion_detectee)

        return {
            "texte": texte,
            "emotion": fiche_resultat["emotion"],
            "couleur": fiche_resultat["couleur"],
            "description": fiche_resultat["description"],
            "polarite": round(polarite, 2),
            "subjectivite": round(subjectivite, 2),
            "nombre_mots": len(texte.split())
        }

if __name__ == "__main__":
    analyzer = EmotionAnalyzer()
    if len(sys.argv) > 1:
        res = analyzer.analyser(" ".join(sys.argv[1:]))
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print("--- Analyseur d'Émotions & Sentiments NLP ---")
        while (q := input("\nEntrez un texte (ou 'q' pour quitter) : ").strip().lower()) not in {"q", "quitter"}:
            if q:
                res = analyzer.analyser(q)
                print(f"Émotion : {res['emotion']}")
                print(f"Polarité : {res['polarite']} | Subjectivité : {res['subjectivite']}")
