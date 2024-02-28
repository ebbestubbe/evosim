import numpy as np

from evosim.Guy import calc_newpos
from evosim.Guy import Guy


def test_guy():
    pos = (1, 1)
    guy = Guy(pos, None, target=(None, None))
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


def test_default_energy_strat():
    """Default energy is 100. Should use the default energy strat: Subtract 1 every step"""
    guy = Guy(pos=(1, 1), speed=None, target=(None, None))
    assert guy.energy == 100
    guy.update_energy()
    assert guy.energy == 99
    guy.update_energy()
    assert guy.energy == 98


def test_default_energy_strat_custom_start():
    """Default energy is custom. Should use the default energy strat: Subtract 1 every step"""
    guy = Guy(pos=(1, 1), speed=None, target=(None, None), energy=12)
    assert guy.energy == 12
    guy.update_energy()
    assert guy.energy == 11
    guy.update_energy()
    assert guy.energy == 10


# def test_guy_alive_when_energy_above_0():
#     guy = Guy(pos=(0, 0), speed=None, target=(None, None), energy=1)
#     assert guy.alive


# def test_guy_dies_when_energy_0():
#     guy = Guy(pos=(0, 0), speed=None, target=(None, None), energy=1)
#     guy.update_energy()
#     assert not guy.alive


def test_updating_dead_guy_does_nothing():
    assert False
