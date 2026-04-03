import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(page_title="Banque France Dashboard", layout="wide")

DATA_PATH = Path("data/raw/flux-et-taux-la-ldds-lep.csv")
MODEL_PATH = Path("model/model.pkl")

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH, sep=";")
    df.columns = [c.strip() for c in df.columns]
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m", errors="coerce")

    numeric_cols = [
        "Flux_LA_LDDS",
        "Flux_LA",
        "Flux_LDDS",
        "Flux_LEP",
        "Année",
        "TLA/TLDDS",
        "TLEP"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna().sort_values("Date").reset_index(drop=True)
    df["month_index"] = range(len(df))
    return df

@st.cache_resource
def load_model():
    if MODEL_PATH.exists():
        return joblib.load(MODEL_PATH)
    return None

df = load_data()
model = load_model()

st.title("📊 Banque France Dashboard")
st.write("Analyse et prévision des données d’épargne réglementée")

st.header("📈 Statistiques")
stats = {
    "nb_lignes": int(len(df)),
    "date_min": str(df["Date"].min().date()),
    "date_max": str(df["Date"].max().date()),
    "flux_la_ldds_moyen": round(float(df["Flux_LA_LDDS"].mean()), 4),
    "flux_la_moyen": round(float(df["Flux_LA"].mean()), 4),
    "flux_ldds_moyen": round(float(df["Flux_LDDS"].mean()), 4),
    "flux_lep_moyen": round(float(df["Flux_LEP"].mean()), 4),
    "taux_la_ldds_moyen": round(float(df["TLA/TLDDS"].mean()), 4),
    "taux_lep_moyen": round(float(df["TLEP"].mean()), 4),
}
st.json(stats)

st.header("🧾 Dernière observation")
last_row = df.iloc[-1].copy()
last_row["Date"] = str(last_row["Date"].date())
st.json(last_row.to_dict())

st.header("📊 Graphique des flux moyens")
values = [
    stats["flux_la_ldds_moyen"],
    stats["flux_ldds_moyen"],
    stats["flux_lep_moyen"]
]
labels = ["LA+LDDS", "LDDS", "LEP"]

fig, ax = plt.subplots(figsize=(6, 3.5))
bars = ax.bar(labels, values)
ax.set_title("Flux moyens", fontsize=12, fontweight="bold")
ax.set_ylabel("Valeur moyenne")
ax.set_xlabel("Produits d’épargne")
ax.grid(axis="y", linestyle="--", alpha=0.5)

for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )

st.pyplot(fig)

st.header("🔮 Prévision")
month_index = st.number_input("Mois futur", value=int(df["month_index"].max()) + 1)
tla = st.number_input("Taux LA / LDDS", value=float(df["TLA/TLDDS"].mean()))
tlep = st.number_input("Taux LEP", value=float(df["TLEP"].mean()))

if st.button("Prédire"):
    if model is None:
        st.error("Le modèle n'est pas disponible. Lance d'abord python -m src.train puis pousse model/model.pkl sur GitHub.")
    else:
        X = pd.DataFrame([{
            "month_index": month_index,
            "TLA/TLDDS": tla,
            "TLEP": tlep
        }])
        prediction = float(model.predict(X)[0])
        st.success(f"Flux prédit LA+LDDS : {prediction:.2f}")