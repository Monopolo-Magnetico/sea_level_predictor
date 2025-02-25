import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (12, 6))
    ax.scatter(x = df["Year"], y = df["CSIRO Adjusted Sea Level"], s = 15)

    # Create first line of best fit
    line_1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_ext = np.arange(df["Year"].min(), 2051)
    y_ext = line_1.intercept + line_1.slope * x_ext
    ax.plot(x_ext, y_ext, 'r', label = "line_1")

    # Create second line of best fit
    line_2 = linregress(df["Year"].iloc[120:], df["CSIRO Adjusted Sea Level"].iloc[120:])
    x_cut = np.arange(2000, 2051)
    y_cut = line_2.intercept + line_2.slope * x_cut
    ax.plot(x_cut, y_cut, 'g', label = "line_2")

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()