import pandas as pd


def clean_risk(risk_series: pd.Series):
    risk: pd.Series = pd.to_numeric(risk_series, errors="coerce")
    risk.fillna(0)
    return risk


def clean_rr(rr_series: pd.Series) -> pd.Series:
    rr: pd.Series = pd.to_numeric(rr_series, errors="coerce")
    rr.fillna(0)
    return rr


url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQL7L-HMzezpuFCDOuS0wdUm81zbX4iVOokaFUGonVR1XkhS6CeDl1gHUrW4U0Le4zihfpqSDphTu4I/pub?gid=1587441688&single=true&output=csv"

df = pd.read_csv(url)
contracts = df["contracts"]
rr = df["R/R"]

data = {
    "contracts": clean_risk(contracts),
    "rr": clean_rr(rr),
}

clean_df = pd.DataFrame(data)
print(clean_df)
