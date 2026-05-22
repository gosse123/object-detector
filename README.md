# 👋 Détection de Main et Visage en Temps Réel

Un projet de **Vision par Ordinateur** utilisant **OpenCV** et **MediaPipe** pour détecter les mains et les visages en temps réel via la webcam.

---

## ✨ Fonctionnalités

- **Détection de main** avec affichage des landmarks (21 points)
- **Détection de visage** avec dessin du contour
- Interface simple et fluide
- Deux scripts indépendants + un launcher optionnel

---

## 🛠 Technologies utilisées

- **Python**
- **OpenCV**
- **MediaPipe**
- **NumPy**

---

## 📁 Structure du Projet
hand-face-detection/
├── src/
│   ├── hand_detection.py
│   └── face_detection.py
├── models/
├── requirements.txt
├── README.md
├── main.py
└── .gitignore

---

## 🚀 Installation

1. Clone le repository :
```bash
git clone https://github.com/tonusername/hand-face-detection.git
cd hand-face-detection

2. Crée un environnement virtuel (recommandé) :
python -m venv venv
source venv/bin/activate    # Windows : venv\Scripts\activate

3. Installe les dépendances :
pip install -r requirements.txt

4. (Optionnel) Télécharge le modèle MediaPipe Tasks et place-le dans le dossier models/

🎮 Utilisation
Lancer directement un script :
# Détection de main
python src/hand_detection.py

# Détection de visage
python src/face_detection.py

Ou utiliser le launcher (recommandé) :
python main.py
Appuie sur q pour quitter.

📌 Améliorations futures possibles

Détection simultanée main + visage
Reconnaissance des gestes (index levé, poing, etc.)
Interface graphique avec Tkinter ou Streamlit
Enregistrement vidéo
Support multi-mains

👨‍💻 Auteur
Nahounou gosse 
Projet réalisé dans le cadre d'apprentissage en Vision par Ordinateur.

📄 License
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.


### 3. Contenu des autres fichiers importants

#### `requirements.txt`

opencv-python>=4.8.0
mediapipe>=0.10.14
numpy

.gitignore

gitignore__pycache__/
venv/
*.pyc
.DS_Store
models/*.task