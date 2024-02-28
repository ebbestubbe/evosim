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
    def update_step(self):
        
        self.update_energy()
        self.move_towards_target()
        
    def move_towards_target(self):
        self.pos = calc_newpos(old_pos=self.pos, target=self.target, speed=self.speed)

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

    def simple_energy_strat(self):
        self.energy = self.energy - 1


def calc_newpos(old_pos, target, speed):
    """Calculate new position, within the allowed speed.

    Args:
        old_pos (_type_): current position
        target (_type_): Target to move towards
        speed (_type_): speed/maximum distance the guy can be moved.

    Returns:
        _type_: new position.
    """
    if target is None:
        return old_pos

    dist_0 = target[0] - old_pos[0]
    dist_1 = target[1] - old_pos[1]
    distance = np.sqrt(dist_0**2 + dist_1**2)
    
    if distance < speed: # If the target is within reach, move to the spot.
        return target

    # We cant make it all the way, just move as close as possible:
    cos_angle = dist_0 / distance
    sin_angle = dist_1 / distance
    speed_x = speed * cos_angle
    speed_y = speed * sin_angle

    new_pos = (old_pos[0] + speed_x, old_pos[1] + speed_y)
    return new_pos
