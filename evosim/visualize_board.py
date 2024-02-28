def plot_guys(df, ax):
    # Plot the guys positions over time
    guy_names = df.columns.get_level_values(0).unique()
    colors = ['black', 'red', 'blue']
    for i, guy_name in enumerate(guy_names):
        color = colors[i]
        ax['map'].plot(df[(guy_name, "posx")], df[(guy_name, "posy")], marker='o',color=color)
        ax['food_eaten'].plot(df[(guy_name, "food_eaten")], color=color)
    
