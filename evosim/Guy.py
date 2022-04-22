import numpy as np


class Guy:
    def __init__(self, pos, speed):
        self.pos = pos
        self.speed = speed
        self.target = (None, None)

    def move(self, new_pos):
        self.pos = new_pos

    def set_target(self, board):
        print(self.target)
        print(self.pos)
        print(self.target == self.pos)
        if (self.target == self.pos) or (
            self.target[0] is None and self.target[1] is None
        ):
            self.target = (-0.5) * 10


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
