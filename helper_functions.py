import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
import plotly.express as px

"""
This file defines several functions used in the cal sports project. Separating in a different file to prevent clutter in 
the main project file.
"""


# Function to contain data cleaning steps for ____ df
def clean_data(df_name):
    # TODO
    df = pd.read_csv(df_name)

    return df


# Function to plot overlayed line plots
# All arrays must be same length for this function
def plot_line_graph(x, y, dfs, label, title):
    for i in range(len(x)):
        sns.lineplot(data=dfs[i], x=x[i], y=y[i], label=label[i])
    plt.title(title)
    plt.legend()
    plt.show()


def plot_scatter(x, y, dfs, title):
    for i in range(len(x)):
        sns.scatterplot(data=dfs[i], x=x[i], y=y[i])
        plt.title(title[i])
        plt.legend()
        plt.xlabel(x[i])
        plt.ylabel(y[i])
        plt.show()
