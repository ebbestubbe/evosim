def plot_guys(df, ax):
    guy_names = df.columns.get_level_values(0).unique()
    for guy_name in guy_names:

        ax.plot(df[(guy_name, "posx")], df[(guy_name, "posy")], "ro")
