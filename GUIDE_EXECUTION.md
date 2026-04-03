# Guide d'exécution

## 1. Installer le projet

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Vérifier le dataset

Le fichier est déjà placé dans :

```text
data/raw/flux-et-taux-la-ldds-lep.csv
```

## 3. Entraîner le modèle simple

```bash
python -m src.train
```

Cela va :
- nettoyer les données
- créer `data/processed/cleaned_banque_france.csv`
- entraîner un modèle linéaire simple
- sauvegarder `model/model.pkl`

## 4. Lancer l'API

```bash
uvicorn api.app:app --reload
```

## 5. Ouvrir Swagger

```text
http://127.0.0.1:8000/docs
```

## 6. Tester `POST /forecast`

Exemple de payload :

```json
{
  "month_index": 24,
  "tla_tldds": 1.7,
  "tlep": 2.7
}
```

## 7. Endpoints utiles

### `GET /stats`
Retourne :
- nombre de lignes
- dates min et max
- moyennes des principaux flux et taux

### `GET /last-record`
Retourne la dernière ligne du dataset

### `POST /forecast`
Retourne une prévision simple du flux `Flux_LA_LDDS`

## 8. PostgreSQL

Le projet est prêt pour PostgreSQL.

Valeurs par défaut dans `.env.example` :

- base : `banque_france_db`
- user : `postgres`
- password : `postgres`

## 9. Docker

```bash
docker compose up --build
```

## 10. Idée de présentation GitHub

Tu peux présenter ce projet comme :

> Analyse et exposition via API de données d'épargne réglementée issues de la Banque de France, avec nettoyage, statistiques, prévision simple et journalisation en base.
