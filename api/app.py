import os
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

from config.settings import DATA_PATH, MODEL_PATH
from src.preprocess import load_and_clean_data
from src.schema import ForecastInput, ForecastResponse

app = FastAPI(
    title="Banque France API",
    version="1.0.0",
    description="API d'analyse et de prévision simple sur des données d'épargne réglementée."
)

df = None
model = None


@app.on_event("startup")
def startup_event():
    global df, model
    df = load_and_clean_data(DATA_PATH)
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)


@app.get("/")
def home():
    return {"message": "API Banque France active"}


@app.get("/health")
def health():
    return {
        "status": "ok",
        "rows": 0 if df is None else len(df),
        "model_loaded": model is not None
    }


@app.get("/stats")
def stats():
    if df is None:
        raise HTTPException(status_code=500, detail="Données non chargées")

    return {
        "nb_lignes": int(len(df)),
        "date_min": str(df["Date"].min().date()),
        "date_max": str(df["Date"].max().date()),
        "flux_la_ldds_moyen": round(float(df["Flux_LA_LDDS"].mean()), 4),
        "flux_la_moyen": round(float(df["Flux_LA"].mean()), 4),
        "flux_ldds_moyen": round(float(df["Flux_LDDS"].mean()), 4),
        "flux_lep_moyen": round(float(df["Flux_LEP"].mean()), 4),
        "taux_la_ldds_moyen": round(float(df["TLA/TLDDS"].mean()), 4),
        "taux_lep_moyen": round(float(df["TLEP"].mean()), 4)
    }


@app.get("/last-record")
def last_record():
    if df is None:
        raise HTTPException(status_code=500, detail="Données non chargées")

    row = df.iloc[-1].copy()
    row["Date"] = str(row["Date"].date())
    return row.to_dict()


@app.post("/forecast", response_model=ForecastResponse)
def forecast(data: ForecastInput):
    global model

    if model is None:
        raise HTTPException(
            status_code=500,
            detail="Le modèle n'est pas chargé. Lance d'abord python -m src.train"
        )

    X = pd.DataFrame([{
        "month_index": data.month_index,
        "TLA/TLDDS": data.tla_tldds,
        "TLEP": data.tlep
    }])

    prediction = float(model.predict(X)[0])

    return ForecastResponse(predicted_flux_la_ldds=round(prediction, 4))