import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Banque France Dashboard", layout="wide")

st.title("📊 Dashboard Banque France")
st.write("Analyse et prévision des données d’épargne")

API_URL = "http://127.0.0.1:8000"

# -----------------------------
# 📊 STATS
# -----------------------------
st.header("📊 Statistiques")

if st.button("Afficher les stats"):
    res = requests.get(f"{API_URL}/stats")
    data = res.json()
    st.json(data)

# -----------------------------
# 📈 DERNIER ENREGISTREMENT
# -----------------------------
st.header("📈 Dernier enregistrement")

if st.button("Voir dernier record"):
    res = requests.get(f"{API_URL}/last-record")
    data = res.json()
    st.json(data)

# -----------------------------
# 🔮 PRÉDICTION
# -----------------------------
st.header("🔮 Prédiction")

month_index = st.number_input("Mois futur", value=30)
tla = st.number_input("Taux LDDS", value=1.7)
tlep = st.number_input("Taux LEP", value=2.7)

if st.button("Prédire"):
    payload = {
        "month_index": month_index,
        "tla_tldds": tla,
        "tlep": tlep
    }
    res = requests.post(f"{API_URL}/forecast", json=payload)
    prediction = res.json()
    st.success("Résultat :")
    st.json(prediction)

    # -----------------------------
# 📊 GRAPHIQUE
# -----------------------------
import matplotlib.pyplot as plt

if st.button("Graphique flux"):
    res = requests.get(f"{API_URL}/stats")
    data = res.json()

    values = [
        data["flux_la_ldds_moyen"],
        data["flux_ldds_moyen"],
        data["flux_lep_moyen"]
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