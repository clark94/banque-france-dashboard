import os
import matplotlib.pyplot as plt

from config.settings import DATA_PATH
from src.preprocess import load_and_clean_data


def main():
    os.makedirs("data/processed", exist_ok=True)

    df = load_and_clean_data(DATA_PATH)

    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["Flux_LA_LDDS"], marker="o")
    plt.title("Évolution du flux LA + LDDS")
    plt.xlabel("Date")
    plt.ylabel("Flux_LA_LDDS")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/processed/flux_la_ldds_plot.png")
    print("Graphique sauvegardé dans data/processed/flux_la_ldds_plot.png")


if __name__ == "__main__":
    main()
