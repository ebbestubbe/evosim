import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from evosim.Guy import Guy
from evosim.Board import Board


def main():
    guys = [Guy(pos=(30, 5), speed=1)]  # , Guy(pos=(6,9), speed=3)]
    board = Board(guys)
    guy0_px = [board.guys[0].pos[0]]
    guy0_py = [board.guys[0].pos[1]]
    guy0_tx = [board.guys[0].target[0]]
    guy0_ty = [board.guys[0].target[1]]
    for i in range(100):
        board.propagate()
        guy0_px.append(board.guys[0].pos[0])
        guy0_py.append(board.guys[0].pos[1])
        guy0_tx.append(board.guys[0].target[0])
        guy0_ty.append(board.guys[0].target[1])

    df = pd.DataFrame(
        data={
            "guy0_px": guy0_px,
            "guy0_py": guy0_py,
            "guy0_tx": guy0_tx,
            "guy0_ty": guy0_ty,
        }
    )
    fig, ax = plt.subplots()
    ax.plot(df["guy0_px"], df["guy0_py"], "bo", label="pos")
    ax.plot(df["guy0_tx"], df["guy0_ty"], "ro", label="target")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
