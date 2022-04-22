from evosim.Guy import Guy
from evosim.Guy import calc_newpos
import numpy as np
from hypothesis import given
from hypothesis import strategies as st


def test_guy():
    pos = (1, 1)
    guy = Guy(pos, None)
    new_pos = (5, 5)
    guy.move(new_pos=new_pos)
    assert guy.pos == new_pos


def test_calc_newpos_1():
    old_pos = (1, 1)
    target = (0, 0)
    speed = 10
    new_pos = calc_newpos(old_pos, target, speed)
    assert new_pos == target


def test_calc_newpos_2():
    old_pos = (1, 1)
    target = (-1, -1)
    speed = 10
    new_pos = calc_newpos(old_pos, target, speed)
    assert new_pos == target


def test_calc_newpos_3():
    old_pos = (1, 1)
    dir = (0, 0)
    speed = 0
    new_pos = calc_newpos(old_pos, dir, speed)
    assert new_pos == old_pos


def test_calc_newpos_4():
    old_pos = (1, 1)
    target = (10, 1)
    speed = 3
    new_pos = calc_newpos(old_pos, target, speed)
    assert new_pos == (4, 1)


def test_calc_newpos_5():
    old_pos = (10, -1)
    target = (10, -10)
    speed = 5
    new_pos = calc_newpos(old_pos, target, speed)
    assert new_pos == (10, -6)


def test_calc_newpos_6():
    old_pos = (-1, 10)
    target = (-10, 10)
    speed = 5
    new_pos = calc_newpos(old_pos, target, speed)
    assert new_pos == (-6, 10)


def test_calc_newpos_7():
    old_pos = (-545, 32.2)
    target = (343.1, 32.3)
    dist = np.sqrt((old_pos[0] - target[0]) ** 2 + (old_pos[1] - target[1]) ** 2)
    speed = dist / 2
    new_pos = calc_newpos(old_pos, target, speed)
    assert new_pos == ((old_pos[0] + target[0]) / 2, (old_pos[1] + target[1]) / 2)


def test_calc_newpos_None():
    old_pos = (2, 5)
    target = None
    speed = 6
    new_pos = calc_newpos(old_pos, target, speed)
    assert new_pos == old_pos
