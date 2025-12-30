import pandas as pd


def data_load(data):
    df = pd.read_csv(data)
    return df


# data = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQL7L-HMzezpuFCDOuS0wdUm81zbX4iVOokaFUGonVR1XkhS6CeDl1gHUrW4U0Le4zihfpqSDphTu4I/pub?gid=1587441688&single=true&output=csv"
# print(data_load(data).head())
