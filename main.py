import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from evosim.Board import Board
from evosim.Guy import Guy
from evosim.Food import Food
from evosim.visualize_board import plot_board


def main():
    running_experiment()

def single_experiment():
    n_guys = 5
    guys = [Guy.random_pos() for _ in range(n_guys)]

    #food_list = [Food((5,5)), Food((0,10)), Food((5,50))]
    food_list = []
    board = Board(guys=guys, food_list=food_list)
    
    df_guys = board.propagate_n(100)
    print(df_guys)

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
    plot_board(guys, df_guys, ax=ax)


    plt.show()

def running_experiment():
    n_guys = 5
    n_generations = 10
    guys = [Guy.random_pos() for _ in range(n_guys)]
    food_list = []
    board = Board(guys=guys, food_list=food_list)
    
    df_guys = board.propagate_n(100)
    for i in range(n_generations):
        print([guy.speed for guy in guys])
        new_guys = [guy.spawn_child() for guy in guys]
        guys = new_guys
        food_list = []
        board = Board(guys=guys, food_list=food_list)
        df_guys = board.propagate_n(100)
    print([guy.speed for guy in guys])
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
    plot_board(guys, df_guys, ax=ax)
    plt.show()

if __name__ == "__main__":
    main()
