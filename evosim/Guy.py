import numpy as np
import random
from hrid import HRID
import numpy as np
hruuid = HRID()

from sklearn.metrics.pairwise import pairwise_distances
import pandas as pd
#Energy on hold for now, just move them towards current target.
speed_scale = 0.5
class Guy:
    def __init__(self, pos, speed, name=None):#, energy=0, energy_strat=None):
        self.pos = pos
        self.speed = speed
        #self.speed_scale = 0.1
        self.target = None
        
        if name is not None:

            self.name = name
        else:
            self.name = hruuid.generate()
        # Start with 1 food eaten makes no scientific sense, but in this case I want to
        # use it as a weight for selecting who breeds. See it as ballots in a tombola
        self.food_eaten = 1 
        # self.energy = energy
        # self.alive = True
        # if energy_strat is None:
        #     self.energy_strat = self.simple_energy_strat
    
    @classmethod
    def random(cls):
        pos = (random.random()*100, random.random()*100)
        speed = random.random()*5
        return cls(pos=pos, speed=speed)
    
    @classmethod
    def random_pos(cls):
        pos = (random.random()*100, random.random()*100)
        speed = 1
        return cls(pos=pos, speed=speed)
    
    @classmethod
    def spawn_child_with_mean(cls, speed_mean):
        # Used for breeding new guys from the old guys speed. Ideally this should be done
        # as a method on the Guy itself. But this way I don't have to keep track of
        # objects, or make new objects.
        pos = (random.random()*100, random.random()*100)
        speed = max(np.random.normal(loc=speed_mean, scale = speed_scale), 0.001)
        return cls(pos=pos, speed=speed)
    
    def spawn_child(self):
        pos = (random.random()*100, random.random()*100)
        speed = max(np.random.normal(loc=self.speed, scale = speed_scale), 0.001)
        return Guy(pos=pos, speed=speed)

    def update_step(self,target):

        self.target=target

        self.move_towards_target()
    
    def update_target(self, food_list):
        if len(food_list) == 0:
            self.target = None
            return
        #Find nearest food
        smallest_dist = np.inf
        smallest_index = None
        
        for j, food in enumerate(food_list):
            dist_0 = self.pos[0] - food.pos[0]
            dist_1 = self.pos[1] - food.pos[1]
            distance = np.sqrt(dist_0**2 + dist_1**2)
            if distance < smallest_dist:
                smallest_dist = distance
                smallest_index = j
        self.target = food_list[smallest_index].pos

    def move_towards_target(self):
        if self.target is None: #Do nothing
            return
        else: # Move towards target
            self.pos = calc_newpos(old_pos=self.pos, target=self.target, speed=self.speed)

    # def update_energy(self):
    #     self.energy_strat()
    #     # if self.energy <= 0:
    #     #     self.alive = False

    def get_state(self):
        if self.target is None: # Fix this to handle the "None" at self.target(maybe class?)
            return {
                "posx": self.pos[0],
                "posy": self.pos[1],
                "tarx": None,
                "tary": None,
                "food_eaten": self.food_eaten
                # "energy": self.energy,
            }
        return {
            "posx": self.pos[0],
            "posy": self.pos[1],
            "tarx": self.target[0],
            "tary": self.target[1],
            "food_eaten": self.food_eaten
            # "energy": self.energy,
        }

    # def simple_energy_strat(self):
    #     self.energy = self.energy - 1


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
