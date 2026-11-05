"""Tests unitaires pour valider l'analyseur d'émotions."""
from emotion_analyzer import EmotionAnalyzer

CAS_TESTS = [
    ("J'adore ce produit, il est vraiment génial et parfait !", "Joie / Enthousiasme"),
    ("Service client horrible et inadmissible, c'est une arnaque !", "Colère / Frustration"),
    ("C'est vraiment dommage, je suis très déçu du résultat.", "Tristesse / Déception"),
    ("Le colis est arrivé à 10 heures.", "Neutre / Informationnel")
]

if __name__ == "__main__":
    analyzer = EmotionAnalyzer()
    succes = 0
    print("--- Lancement des tests NLP d'Émotions ---\n")
    for texte, attendu in CAS_TESTS:
        res = analyzer.analyser(texte)
        obtenu = res["emotion"]
        ok = obtenu == attendu
        succes += ok
        print(f"[{'OK' if ok else 'ECHEC'}] '{texte[:35]}...' -> Détecté: {obtenu}")

    print(f"\nRésultat : {succes}/{len(CAS_TESTS)} tests réussis.")
