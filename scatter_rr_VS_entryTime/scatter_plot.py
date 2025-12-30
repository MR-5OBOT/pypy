import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def scatter_plot(x: pd.Series, y: pd.Series):
    plot = sns.scatterplot(x=x, y=y)
    # plt.show()
    plt.savefig("plot.png")
    return plot
