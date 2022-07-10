import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from evosim.Board import Board
from evosim.Guy import Guy
from evosim.visualize_board import plot_guys


def main():
    guy0 = Guy(pos=(0, 0), speed=1, target=(12, -5), name="guy0")
    guy1 = Guy(pos=(-10, 10), speed=2, target=(234, 5), name="guy1")
    guys = [guy0, guy1]
    board = Board(guys=guys)
    df = board.propagate_n(100)
    print(df)

    fig, ax = plt.subplots()
    plot_guys(df, ax=ax)

    plt.show()


if __name__ == "__main__":
    main()
