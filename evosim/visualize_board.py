import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import joypy
import seaborn as sns

colors = [
    "#000000",
    "#00FF00",
    "#0000FF",
    "#FF0000",
    "#01FFFE",
    "#FFA6FE",
    "#FFDB66",
    "#006401",
    "#010067",
    "#95003A",
    "#007DB5",
    "#FF00F6",
    "#FFEEE8",
    "#774D00",
    "#90FB92",
    "#0076FF",
    "#D5FF00",
    "#FF937E",
    "#6A826C",
    "#FF029D",
    "#FE8900",
    "#7A4782",
    "#7E2DD2",
    "#85A900",
    "#FF0056",
    "#A42400",
    "#00AE7E",
    "#683D3B",
    "#BDC6FF",
    "#263400",
    "#BDD393",
    "#00B917",
    "#9E008E",
    "#001544",
    "#C28C9F",
    "#FF74A3",
    "#01D0FF",
    "#004754",
    "#E56FFE",
    "#788231",
    "#0E4CA1",
    "#91D0CB",
    "#BE9970",
    "#968AE8",
    "#BB8800",
    "#43002C",
    "#DEFF74",
    "#00FFC6",
    "#FFE502",
    "#620E00",
    "#008F9C",
    "#98FF52",
    "#7544B1",
    "#B500FF",
    "#00FF78",
    "#FF6E41",
    "#005F39",
    "#6B6882",
    "#5FAD4E",
    "#A75740",
    "#A5FFD2",
    "#FFB167",
    "#009BFF",
    "#E85EBE",
]

def plot_board(guys, df_guys_history, df_guys_stats, ax):
    # Plot the guys positions over time
    guy_names = df_guys_history.columns.get_level_values(0).unique()
    #colors = ['r','b','k','y','m','c']
    guy_dict = {guy.name: guy for guy in guys}
    for i, guy_name in enumerate(guy_names):
        color = colors[i]
        ax['map'].plot(df_guys_history[(guy_name, "posx")], df_guys_history[(guy_name, "posy")], marker='.',color=color)
        ax['food_eaten'].plot(df_guys_history[(guy_name, "food_eaten")], color=color, label=f"speed: {guy_dict[guy_name].speed:.2f}; eaten: {guy_dict[guy_name].food_eaten}")
    #ax['food_eaten'].legend()
    
    plot_hist(array=df_guys_stats['speed'], color=color, ax=ax["speed_histogram"])
    #ax["food_available"].plot(df_board[("board", "food_available")])

def plot_hist(array, color, ax):
    bins = np.linspace(array.min(), array.max(), 10)
    ax.hist(array, color=color, bins=bins, density=True)
    kde = stats.gaussian_kde(array)
    xx = np.linspace(array.min(), array.max(), 1000)
    ax.plot(xx, kde(xx))

def plot_multiple_generations(df_guys):

    # fig,ax = plt.subplot_mosaic(
    #     [
    #         ["foo"]
    #     ]
    # )
    # fig,ax = joypy.joyplot(data=df_guys, by='generation', column='speed')
    fig,ax = plt.subplots()
    sns.scatterplot(data=df_guys, x= 'speed', y='eaten', hue='generation', ax=ax)
    # Total food each guy has eaten
    #Their speed
    # generation number
    # plot average, 5, 25, 50, 75. 95
    grouped = df_guys.groupby("generation")
    fig,ax = plt.subplots()
    ax.plot(grouped['speed'].mean(), color='black', linewidth=3)
    ax.plot(grouped['speed'].quantile(0.05), color='red', linestyle='--', linewidth=1)
    ax.plot(grouped['speed'].quantile(0.25), color='red', linestyle='--', linewidth=2)
    ax.plot(grouped['speed'].quantile(0.50), color='red', linewidth=3)
    ax.plot(grouped['speed'].quantile(0.75), color='red', linestyle='--', linewidth=2)
    ax.plot(grouped['speed'].quantile(0.95), color='red', linestyle='--', linewidth=1)