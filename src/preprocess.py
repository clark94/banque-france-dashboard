import pandas as pd


def load_and_clean_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, sep=";")
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
