import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from evosim.Board import Board
from evosim.Guy import Guy
from evosim.Food import Food
from evosim.visualize_board import plot_board


def main():
    #guy0 = Guy(pos=(0, 0), speed=1, name="guy0")
    #guy1 = Guy(pos=(20, 10), speed=2, name="guy1")#, energy=20)

    #guys = [guy0, guy1, Guy.random()]

    n_guys = 50
    guys = [Guy.random() for _ in range(n_guys)]

    #food_list = [Food((5,5)), Food((0,10)), Food((5,50))]
    food_list = []
    board = Board(guys=guys, food_list=food_list)
    
    df_guys = board.propagate_n(1000)
    print(df_guys)

    fig, ax = plt.subplot_mosaic(
        [
            ["map"],
            ["map"],
            ["map"],
            ["map"],
            ["food_eaten"],
            ["food_available"]
        ]
    )
    plot_board(guys, df_guys, ax=ax)


    plt.show()


if __name__ == "__main__":
    main()
