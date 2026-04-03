import os
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

from config.settings import DATA_PATH, MODEL_PATH
from src.preprocess import load_and_clean_data


def main():
    os.makedirs("model", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    df = load_and_clean_data(DATA_PATH)

    X = df[["month_index", "TLA/TLDDS", "TLEP"]]
    y = df["Flux_LA_LDDS"]

    model = LinearRegression()
    model.fit(X, y)

    predictions = model.predict(X)
    mae = mean_absolute_error(y, predictions)
    r2 = r2_score(y, predictions)

    joblib.dump(model, MODEL_PATH)
    df.to_csv("data/processed/cleaned_banque_france.csv", index=False)

    print("=== Entraînement terminé ===")
    print(f"Nombre de lignes : {len(df)}")
    print(f"MAE : {mae:.4f}")
    print(f"R2  : {r2:.4f}")
    print(f"Modèle sauvegardé dans : {MODEL_PATH}")
    print("Données nettoyées sauvegardées dans : data/processed/cleaned_banque_france.csv")


if __name__ == "__main__":
    main()
