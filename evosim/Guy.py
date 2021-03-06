import numpy as np


class Guy:
    def __init__(self, pos, speed, target, name=None, energy=100, energy_strat=None):
        self.pos = pos
        self.speed = speed
        self.target = target
        self.name = name
        self.energy = energy
        self.alive = True
        if energy_strat is None:
            self.energy_strat = self.simple_energy_strat

    def move(self, new_pos):
        self.pos = new_pos

    def update_energy(self):
        self.energy_strat()
        if self.energy <= 0:
            self.alive = False

    def get_state(self):
        return {
            "posx": self.pos[0],
            "posy": self.pos[1],
            "tarx": self.target[0],
            "tary": self.target[1],
            "energy": self.energy,
        }

    def set_target(self):
        ...

    def simple_energy_strat(self):
        self.energy = self.energy - 1


def calc_newpos(old_pos, target, speed):
    if target is None:
        return old_pos

    dist_0 = target[0] - old_pos[0]
    dist_1 = target[1] - old_pos[1]
    distance = np.sqrt(dist_0**2 + dist_1**2)

    if distance < speed:
        return target

    cos_angle = dist_0 / distance
    sin_angle = dist_1 / distance
    speed_x = speed * cos_angle
    speed_y = speed * sin_angle

    new_pos = (old_pos[0] + speed_x, old_pos[1] + speed_y)
    return new_pos
