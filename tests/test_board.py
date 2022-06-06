import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal

from evosim.Board import Board
from evosim.Guy import Guy


def test_board_propagate_1guys():
    guy = Guy(pos=(30, 5), speed=1, target=(30, 20))
    guys = [guy]
    board = Board(guys)
    board.propagate()
    assert guy.pos == (30, 6)


def test_board_propagate_2guys():
    guy0 = Guy(pos=(0, 0), speed=1, target=(2, 0))
    guy1 = Guy(pos=(3, 10), speed=1, target=(3, 9.5))
    guys = [guy0, guy1]
    board = Board(guys)
    board.propagate()
    assert guy0.pos == (1, 0)
    assert guy1.pos == (3, 9.5)


def test_board_propagate_multiple_steps():
    guy0 = Guy(pos=(0, 0), speed=1, target=(3, 0))
    guy1 = Guy(pos=(3, 10), speed=2, target=(3, 20))
    guy2 = Guy(pos=(3, 10), speed=0, target=(3, 15))
    guys = [guy0, guy1, guy2]
    board = Board(guys)
    board.propagate()
    board.propagate()
    board.propagate()
    assert guy0.pos == (3, 0)
    assert guy1.pos == (3, 16)
    assert guy2.pos == (3, 10)


def test_board_propagate_n():
    guy = Guy(pos=(30, 5), speed=1, target=(30, 20), name="guy0", energy=9)
    guys = [guy]
    board = Board(guys)
    df = board.propagate_n(2)
    guy_names = ["guy0"]
    measures = ["posx", "posy", "tarx", "tary", "energy"]
    columns = pd.MultiIndex.from_product([guy_names, measures])
    df_expected = pd.DataFrame(
        columns=columns,
        data=np.array(
            [[30, 30, 30], [5, 6, 7], [30, 30, 30], [20, 20, 20], [9, 8, 7]]
        ).T,
    )
    assert_frame_equal(df, df_expected, check_dtype=False)


def test_board_propagate_n_2():
    guy0 = Guy(pos=(30, 5), speed=1, target=(30, 20), name="guy0")
    guy1 = Guy(pos=(0, 0), speed=2, target=(100, 0), name="guy1", energy=13)

    guys = [guy0, guy1]
    board = Board(guys)
    df = board.propagate_n(2)
    guy_names = ["guy0", "guy1"]
    measures = ["posx", "posy", "tarx", "tary", "energy"]
    columns = pd.MultiIndex.from_product([guy_names, measures])
    df_expected = pd.DataFrame(
        columns=columns,
        data=np.array(
            [
                [30, 30, 30],
                [5, 6, 7],
                [30, 30, 30],
                [20, 20, 20],
                [100, 99, 98],
                [0, 2, 4],
                [0, 0, 0],
                [100, 100, 100],
                [0, 0, 0],
                [13, 12, 11],
            ]
        ).T,
    )
    assert_frame_equal(df, df_expected, check_dtype=False)


def test_board_propagate_n_get_energy():
    guy0 = Guy(pos=(30, 5), speed=1, target=(30, 20), name="guy0", energy=80)

    guys = [guy0]
    board = Board(guys)
    df = board.propagate_n(2)
    guy_names = ["guy0"]
    measures = ["posx", "posy", "tarx", "tary", "energy"]
    columns = pd.MultiIndex.from_product([guy_names, measures])
    df_expected = pd.DataFrame(
        columns=columns,
        data=np.array(
            [
                [30, 30, 30],
                [5, 6, 7],
                [30, 30, 30],
                [20, 20, 20],
                [80, 79, 78],
            ]
        ).T,
    )
    assert_frame_equal(df, df_expected, check_dtype=False)
