import pandas as pd


from load_data import data_load
from clean_data import filtered_entry_time, clean_rr
from scatter_plot import scatter_plot


data = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQL7L-HMzezpuFCDOuS0wdUm81zbX4iVOokaFUGonVR1XkhS6CeDl1gHUrW4U0Le4zihfpqSDphTu4I/pub?gid=1587441688&single=true&output=csv"
df = data_load(data)

rr = clean_rr(df["R/R"])
HMS_series = filtered_entry_time(df["entry_time"])
print(HMS_series.head())

scatter_plot(HMS_series, rr)
