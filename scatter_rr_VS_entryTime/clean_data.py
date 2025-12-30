import pandas as pd


def clean_rr(risk_series: pd.Series):
    risk: pd.Series = pd.to_numeric(risk_series, errors="coerce")
    risk.fillna(0)
    return risk


def filtered_entry_time(series: pd.Series):
    to_HMS = pd.to_timedelta(series, errors="coerce")
    return to_HMS


# url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQL7L-HMzezpuFCDOuS0wdUm81zbX4iVOokaFUGonVR1XkhS6CeDl1gHUrW4U0Le4zihfpqSDphTu4I/pub?gid=1587441688&single=true&output=csv"
#
# df = pd.read_csv(url)
# contracts = df["contracts"]
# rr = df["R/R"]
#
# data = {
#     "contracts": clean_risk(contracts),
#     "rr": clean_rr(rr),
# }
#
# clean_df = pd.DataFrame(data)
# print(clean_df)
