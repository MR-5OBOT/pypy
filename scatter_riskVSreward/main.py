from load_data import data_load
from clean_data import clean_risk, clean_rr
from plots import risk_vs_reward_scatter


def main():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQL7L-HMzezpuFCDOuS0wdUm81zbX4iVOokaFUGonVR1XkhS6CeDl1gHUrW4U0Le4zihfpqSDphTu4I/pub?gid=1587441688&single=true&output=csv"
    df = data_load(url)
    x = clean_risk(df["contracts"])
    y = clean_rr(df["R/R"])
    risk_vs_reward_scatter(x, y)


if __name__ == "__main__":
    main()
    print("saved to ./data/scatter.png")
