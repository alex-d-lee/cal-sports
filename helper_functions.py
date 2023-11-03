import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk

"""
This file defines several functions used in the cal sports project. Separating in a different file to prevent clutter in 
the main project file.
"""


# Function to plot overlayed line plots
# All arrays must be same length for this function
def plot_line_graph(x, y, dfs, label, title):
    for i in range(len(x)):
        sns.lineplot(data=dfs[i], x=x[i], y=y[i], label=label[i])
    plt.title(title)
    plt.legend()
    plt.show()
