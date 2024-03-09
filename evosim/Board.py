import pandas as pd
import numpy as np
from evosim.Food import Food
import random
from sklearn.metrics.pairwise import pairwise_distances
SEED = 42
class Board:
    def __init__(self, guys, min_food, food_list=None):
        self.guys = guys
        self.min_food = min_food
        if food_list is None:
            self.food_list = []
        else:
            self.food_list = food_list
        
        random.seed(SEED)

    def propagate(self):
        # Move all the guys.
        # Eat all the food and note the guys for eaten food.
        while len(self.food_list) < self.min_food:
            foodpos = (random.random()*100, random.random()*100)
            self.food_list.append(Food(foodpos))
        smallest_food_ind = self.get_distmatrix().idxmin(axis=1) 
        for i, guy in enumerate(self.guys):
            # newpos = calc_newpos(old_pos=guy.pos, target=guy.target, speed=guy.speed)
            target = (self.food_list[smallest_food_ind[i]].pos[0], self.food_list[smallest_food_ind[i]].pos[1])
            guy.update_step(target = target)
            # min_ind = food_list.argmin()
        
        self.guys_eat()

    def propagate_n(self, n):
        guy_states = {guy.name: [guy.get_state()] for guy in self.guys}
        food_available = [] # Update this to some "board state"
        for i in range(n):
            self.propagate()
            for guy in self.guys:
                state = guy.get_state()
                guy_states[guy.name].append(state)
                food_available.append(len(self.food_list))
        df_run_history = {
            name: pd.DataFrame.from_dict(states) for name, states in guy_states.items()
        }
        df_run_history = pd.concat(df_run_history, axis=1)
        df_guys_stats = pd.DataFrame(
            data={
                "speed": [guy.speed for guy in self.guys],
                "eaten": [guy.food_eaten for guy in self.guys]
            }
        )
        # df_results_board = pd.DataFrame(
        #     columns=pd.MultiIndex.from_tuples(
        #             [
        #                 ("board", "food_available")
        #             ]
        #         ),
        #     data=food_available
        # )
        return df_run_history, df_guys_stats#, df_results_board
    
    def guys_eat(self):
        df_distmatrix = self.get_distmatrix()
        # Find the food that was eaten and find out which food was eaten by whom:
        removed_food, food_per_guy = find_eaten_food(df_distmatrix=df_distmatrix)
        # Remove the food 
        for food_index in sorted(removed_food, reverse=True):
            del self.food_list[food_index]
        # Add points:
        for index, food in food_per_guy.items():
            self.guys[index].food_eaten += food
    
    def get_distmatrix(self):
        
        #Output: each row is a guy and each column is a food. The value is the distance
        #between them
        
        guy_pos = [[guy.pos[0], guy.pos[1]] for guy in self.guys]
        food_pos = [[food.pos[0], food.pos[1]] for food in self.food_list]
        df_distmatrix = pd.DataFrame(pairwise_distances(guy_pos, food_pos))
        return df_distmatrix


def find_eaten_food(df_distmatrix):
    # Find all food that will be eaten:
    food_distance = 1 # Length of mouth
    eat_match = df_distmatrix < food_distance
    s = eat_match.any(axis=0)
    removed_food = s[s].index
    eaten_per_guy = eat_match.sum(axis=1)
    above_0 = eaten_per_guy[eaten_per_guy>0]
    return removed_food, above_0