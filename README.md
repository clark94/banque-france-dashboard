🚀 Banque France Data Analytics & Forecasting App

Projet Data complet basé sur des données réelles de la Banque de France 🇫🇷
👉 API + Machine Learning + Dashboard interactif

---

📊 Objectif

Construire une application permettant :

- d’analyser les comportements d’épargne
- de visualiser les tendances économiques
- de prédire l’évolution des flux financiers

---

📁 Dataset utilisé

Dataset issu de data.gouv.fr / Banque de France

Fichier :

- "flux-et-taux-la-ldds-lep.csv"

🔑 Variables principales

- "Date" : période mensuelle
- "Flux_LA_LDDS" : flux global épargne
- "Flux_LA", "Flux_LDDS", "Flux_LEP"
- "TLA/TLDDS" : taux Livret A / LDDS
- "TLEP" : taux LEP

---

⚙️ Fonctionnalités

🔹 API FastAPI

- "GET /stats" → statistiques descriptives
- "GET /last-record" → dernière observation
- "POST /forecast" → prédiction des flux

---

🔹 Machine Learning

- Modèle de régression (Scikit-learn)
- Prédiction des flux d’épargne
- Pipeline de préparation des données

---

🔹 Dashboard (Streamlit)

Interface interactive permettant :

- affichage des statistiques
- visualisation graphique 📊
- prédiction en temps réel 🔮


🛠️ Technologies utilisées

- Python 🐍
- FastAPI ⚙️
- Streamlit 📊
- Pandas
- Scikit-learn 🤖
- Matplotlib 📈
- PostgreSQL
- Docker 🐳

---

💼 Cas d’usage

Ce projet peut être utilisé par :

- 🏦 Banques → analyse des flux d’épargne
- 📊 Data Analysts → suivi des tendances économiques
- 📈 Finance → aide à la décision stratégique
- 🤖 Data Scientists → modélisation prédictive

---

🧱 Architecture du projet

banque_france_api_project/
├── api/
├── config/
├── data/
├── model/
├── src/
├── tests/
├── dashboard.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

---

🚀 Lancer le projet en local

1️⃣ Installation

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

---

2️⃣ Entraînement du modèle

python -m src.train

---

3️⃣ Lancer l’API

uvicorn api.app:app --reload

Swagger :

http://127.0.0.1:8000/docs

---

4️⃣ Lancer le Dashboard

streamlit run dashboard.py

---

⚠️ Remarque

Le dataset contient peu de données, le modèle est donc volontairement simple.
L’objectif principal du projet est :

- démontrer un pipeline data complet
- intégrer API + ML + visualisation
- travailler avec des données réelles

---

🎯 Compétences démontrées

- Data Analysis 📊
- Machine Learning 🤖
- API Development ⚙️
- Data Visualization 📈
- Data Engineering (pipeline) 🔧

---

---

⭐ Conclusion

👉 Projet complet démontrant la capacité à construire une application data de bout en bout :

➡️ Data → Analyse → Modèle → API → Dashboard

---

## 🌍 Déploiement

Le dashboard est déployé avec Streamlit Cloud.

⚠️ Remarque :
La version en ligne utilise directement les données et le modèle sans passer par l’API FastAPI (utilisée uniquement en local).