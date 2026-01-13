import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def scatter_plot(x: pd.Series, y: pd.Series):
    plot = sns.scatterplot(x=x, y=y)
    # plt.show()
    plt.savefig("plot.png")
    return plot


def data_load(data):
    df = pd.read_csv(data)
    return df


def clean_numeric_series(risk_series: pd.Series):
    risk: pd.Series = pd.to_numeric(risk_series, errors="coerce")
    risk = risk.fillna(0)
    return risk


data = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQL7L-HMzezpuFCDOuS0wdUm81zbX4iVOokaFUGonVR1XkhS6CeDl1gHUrW4U0Le4zihfpqSDphTu4I/pub?gid=1587441688&single=true&output=csv"
df = data_load(data)

rr = clean_numeric_series(df["R/R"])
sl_points = clean_numeric_series(df["sl_points"])
outcomes = df["outcome"]
print(sl_points.head())


def rr_vs_hour_range_bubble_scatter(
    sl_points_series: pd.Series,
    rr_series: pd.Series,
    outcome: pd.Series,
    *,
    title: str = "R/R vs SL Points",
    # xlabel: str = "Entry Time Range",
    # ylabel: str = "R/R",
    figsize: tuple = (8, 6),
    rotation: int = 45,
    labelsize: int = 10,
    size_scale: tuple = (50, 500),  # min and max bubble size
):
    plt.style.use("dark_background")

    fig, ax = plt.subplots(figsize=figsize)
    sns.scatterplot(
        x=sl_points,
        y=rr_series,
        hue=outcome,
        sizes=size_scale,
        palette={"WIN": "#466963", "LOSS": "#C05478", "BE": "#888444"},
        edgecolor="black",
        alpha=0.8,
        ax=ax,
    )

    ax.set_title(title)
    # ax.set_xlabel(xlabel)
    # ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=rotation, labelsize=labelsize, color="gray")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("gray")
    ax.spines["bottom"].set_color("gray")
    ax.title.set_color("gray")
    ax.xaxis.label.set_color("gray")
    ax.yaxis.label.set_color("gray")
    ax.tick_params(colors="gray")

    fig.tight_layout()
    plt.savefig("plot.png")
    return fig


rr_vs_hour_range_bubble_scatter(sl_points, rr, outcomes)
# scatter_plot(sl_points, rr)
