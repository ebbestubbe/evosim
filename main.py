import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from evosim.Board import Board
from evosim.Guy import Guy
from evosim.Food import Food
from evosim.visualize_board import plot_guys


def main():
    guy0 = Guy(pos=(0, 0), speed=1, name="guy0")
    guy1 = Guy(pos=(20, 10), speed=2, name="guy1")#, energy=20)
    guys = [guy0, guy1]
    food_list = [Food((5,5)), Food((0,10)), Food((5,50))]
    board = Board(guys=guys, food_list=food_list)
    
    df = board.propagate_n(2)
    print(df)

    fig, ax = plt.subplot_mosaic(
        [
            ["map"],
            ["map"],
            ["map"],
            ["map"],
            ["food_eaten"]
        ]
    )
    plot_guys(df, ax=ax)


    plt.show()


if __name__ == "__main__":
    main()
