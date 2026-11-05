// Analyseur d'Émotions Frontend + Reconnaissance Vocale (Web Speech API)
function normaliser(t) {
  return t.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/[^a-z0-9]+/g, " ").trim();
}

function analyserEmotion(texte) {
  const norm = normaliser(texte);
  let meilleureEmotion = EMOTIONS.find(e => e.id === "neutre");
  let maxScore = 0;

  EMOTIONS.forEach(e => {
    const mots = e.mots_cles.split(" ");
    let score = 0;
    mots.forEach(m => {
      if (norm.includes(m)) score += 1;
    });
    if (score > maxScore) {
      maxScore = score;
      meilleureEmotion = e;
    }
  });

  const motsPos = ["super", "adore", "genial", "magnifique", "excellent", "parfait", "heureux", "ravi", "joie"];
  const motsNeg = ["nul", "horrible", "mauvais", "arnaque", "triste", "decu", "colere", "fache"];
  
  let pos = 0, neg = 0;
  norm.split(" ").forEach(w => {
    if (motsPos.includes(w)) pos++;
    if (motsNeg.includes(w)) neg++;
  });

  let polarite = (pos - neg) / (pos + neg + 1);
  let subjectivite = (pos + neg) / (norm.split(" ").length + 1);

  return {
    emotion: meilleureEmotion.emotion,
    couleur: meilleureEmotion.couleur,
    description: meilleureEmotion.description,
    polarite: polarite.toFixed(2),
    subjectivite: (subjectivite * 100).toFixed(0) + "%"
  };
}

function executerAnalyse() {
  const texte = document.getElementById("inputText").value.trim();
  if (!texte) return;

  const res = analyserEmotion(texte);
  const badge = document.getElementById("emotionBadge");
  
  badge.textContent = res.emotion;
  badge.style.backgroundColor = res.couleur;
  document.getElementById("emotionDesc").textContent = res.description;
  document.getElementById("scorePolarite").textContent = res.polarite;
  document.getElementById("scoreSubjectivite").textContent = res.subjectivite;
}

document.getElementById("btnAnalyze").addEventListener("click", executerAnalyse);

// Reconnaissance Vocale HTML5 / Web Speech API
const btnVoice = document.getElementById("btnVoice");
const voiceStatus = document.getElementById("voiceStatus");

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

if (SpeechRecognition) {
  const recognition = new SpeechRecognition();
  recognition.lang = "fr-FR";
  recognition.continuous = false;

  btnVoice.addEventListener("click", () => {
    recognition.start();
    voiceStatus.textContent = "🎙️ Écoute en cours... Parlez maintenant !";
    btnVoice.classList.add("recording");
  });

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    document.getElementById("inputText").value = transcript;
    voiceStatus.textContent = `🗣️ Capturé : "${transcript}"`;
    btnVoice.classList.remove("recording");
    executerAnalyse();
  };

  recognition.onerror = (event) => {
    voiceStatus.textContent = "❌ Erreur de reconnaissance vocale : " + event.error;
    btnVoice.classList.remove("recording");
  };

  recognition.onend = () => {
    btnVoice.classList.remove("recording");
  };
} else {
  btnVoice.style.display = "none";
  voiceStatus.textContent = "⚠️ La reconnaissance vocale n'est pas supportée sur ce navigateur (utilisez Chrome/Edge).";
}
