# 🧠 NLP Emotion & Sentiment Analyzer

Application et moteur de traitement du langage naturel (NLP) permettant d'analyser les sentiments et de classer les émotions (Joie, Colère, Tristesse, Neutre) dans un texte.

---

## 📌 Fonctionnalités
- 🎯 **Analyse d'Émotions** : Classification du texte selon des catégories d'émotions prédéfinies.
- 📊 **Calcul de Sentiments** : Évaluation des scores de polarité (-1.0 à +1.0) et de subjectivité.
- 🌐 **Interface Web Sans Serveur** : Version web interactive avec `index.html`.
- 🐍 **Moteur Python NLP** : Traitement par TextBlob et extraction lexicographique (`emotion_analyzer.py`).

---

## 📂 Structure du projet

```
emotion-sentiment-analyzer/
├── data/
│   └── fiches_emotions.json    # Base d'émotions et mots-clés de référence
├── emotion_analyzer.py         # Moteur principal NLP en Python
├── build_web_data.py          # Script de conversion JSON vers JS
├── emotions.js                # Données exportées pour l'interface Web
├── index.html                 # Interface utilisateur Web
├── script.js                  # Logique JavaScript pour le Web
├── style.css                  # Design et mise en page
├── tester.py                  # Script de tests unitaires
├── requirements.txt           # Dépendances Python
└── README.md                  # Documentation du projet
```

---

## 🚀 Utilisation (Anaconda)

### 1. Interface Web (immédiate) :
Ouvrez simplement le fichier `index.html` dans votre navigateur.

### 2. Moteur Python (Ligne de commande) :
```bash
pip install -r requirements.txt
python emotion_analyzer.py "J'adore ce projet, il est génial !"
python tester.py
```

---

## 👤 Auteure
**Fidélia EBA-DOVI**  
*Étudiante en Informatique et Télécommunications | INSTI Lokossa*  
GitHub : [@FideliaEBA](https://github.com/FideliaEBA)
