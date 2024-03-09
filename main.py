import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from evosim.Board import Board
from evosim.Guy import Guy
from evosim.Food import Food
import evosim.visualize_board as visualize


def main():
    running_experiment()

def single_experiment():
    n_guys = 20
    guys = [Guy.random_pos() for _ in range(n_guys)]

    #food_list = [Food((5,5)), Food((0,10)), Food((5,50))]
    food_list = []
    board = Board(guys=guys, food_list=food_list)
    
    df_run_history, df_guys_stats = board.propagate_n(1000)

    fig, ax = plt.subplot_mosaic(
        [
            ["map"],
            ["map"],
            ["map"],
            ["map"],
            ["food_eaten"],
            # ["food_available"]
        ]
    )
    visualize.plot_board(guys, df_guys_history=df_run_history, df_guys_stats=df_guys_stats, ax=ax)


    plt.show()

def running_experiment():
    n_guys = 50
    n_generations = 500
    breeders = pd.DataFrame(
        data={
            "speed": [1 for _ in range(n_guys)],
            "eaten": [1 for _ in range(n_guys)]
        }
    )
    #food_list = []
    #board = Board(guys=guys, food_list=food_list)
    
    #df_guys_history = board.propagate_n(100)
    #df_run_history_runs = []
    df_guys_stats_runs = []
    for i in range(n_generations):
        
        new_guys = [Guy.spawn_child_with_mean(guy.speed) for _,guy in breeders.iterrows()]
        guys = new_guys
        print([f"{guy.speed:.2f}" for guy in guys])
        board = Board(guys=guys, min_food = np.round(n_guys/2))
        df_run_history, df_guys_stats = board.propagate_n(100)

        # Select guys for breeding:
        breeders = df_guys_stats.sample(
            n=n_guys,
            replace=True,
            weights="eaten"
        )
        #df_run_history_runs.append(df_run_history)
        df_guys_stats_runs.append(df_guys_stats)
    
    dfs_with_parent = [df.assign(generation=i) for i, df in enumerate(df_guys_stats_runs)]
    concatenated_df = pd.concat(dfs_with_parent)
    print([f"{guy.speed:.2f}" for guy in guys])
    fig, ax = plt.subplot_mosaic(
        [
            ["map", "map"],
            ["map", "map"],
            ["map", "map"],
            ["map", "map"],
            ["food_eaten", "speed_histogram"],
            # ["food_available"]
        ]
    )
    visualize.plot_board(guys, df_guys_history=df_run_history, df_guys_stats=df_guys_stats, ax=ax)
    visualize.plot_multiple_generations(concatenated_df)
    plt.show()

if __name__ == "__main__":
    main()
