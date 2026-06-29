# 👋 Détection de Main et Visage en Temps Réel

Un projet de **Vision par Ordinateur** utilisant **OpenCV** et **MediaPipe** pour détecter les mains et les visages en temps réel via la webcam.

---

## ✨ Fonctionnalités

- Détection de main avec affichage des 21 landmarks
- Détection de visage avec dessin du contour
- Deux scripts indépendants
- Launcher (`main.py`) pour choisir facilement le mode
- Interface simple et fluide

---

## 🛠 Technologies utilisées

- **Python**
- **OpenCV**
- **MediaPipe**
- **NumPy**

---

## 📁 Structure du Projet

```bash
hand-face-detection/
├── src/
│   ├── hand_detection.py
│   └── face_detection.py
├── models/                  # Modèles MediaPipe (optionnel)
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── main.py
```

---

## 🚀 Installation

1. Clone le repository :
```bash
git clone https://github.com/tonusername/hand-face-detection.git
cd hand-face-detection
```

2. Crée un environnement virtuel (fortement recommandé) :
```bash
python -m venv venv

# Sur Windows :
venv\Scripts\activate

# Sur Linux / Mac :
source venv/bin/activate
```

3. Installe les dépendances :
```bash
pip install -r requirements.txt
```

4. (Optionnel) Télécharge le modèle `hand_landmarker.task` et place-le dans le dossier `models/`

---

## 🎮 Utilisation

### Avec le launcher (recommandé) :
```bash
python main.py
```

### Lancer directement un script :
```bash
# Détection de main
python src/hand_detection.py

# Détection de visage
python src/face_detection.py
```

**Appuie sur `q`** pour quitter n'importe quelle fenêtre.

---

## 📋 requirements.txt

```txt
opencv-python>=4.8.0
mediapipe>=0.10.14
numpy
```

---

## 📌 Améliorations futures possibles

- Détection simultanée (main + visage)
- Reconnaissance des gestes de la main
- Interface graphique (Tkinter / Streamlit)
- Enregistrement de la vidéo
- Support multi-mains

---

## 👨‍💻 Auteur

**Groupe 14**

Projet réalisé dans le cadre d'apprentissage en **Vision par Ordinateur**.

---

## 📄 License

Ce projet est sous licence **MIT** — voir le fichier [`LICENSE`](LICENSE) pour plus de détails.
