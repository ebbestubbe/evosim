import pandas as pd
import numpy as np
from evosim.Food import Food
import random
SEED = 42
class Board:
    def __init__(self, guys, food_list):
        self.guys = guys
        self.food_list = food_list
        random.seed(SEED)

    def propagate(self):
        # Move all the guys.
        # Eat all the food and note the guys for eaten food.
        while len(self.food_list) < 100:
            foodpos = (random.random()*100, random.random()*100)
            self.food_list.append(Food(foodpos))
        for guy in self.guys:
            # newpos = calc_newpos(old_pos=guy.pos, target=guy.target, speed=guy.speed)
            guy.update_step(self.food_list)
        
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
        df_results_guys = {
            name: pd.DataFrame.from_dict(states) for name, states in guy_states.items()
        }
        df_results_guys = pd.concat(df_results_guys, axis=1)
        # df_results_board = pd.DataFrame(
        #     columns=pd.MultiIndex.from_tuples(
        #             [
        #                 ("board", "food_available")
        #             ]
        #         ),
        #     data=food_available
        # )
        return df_results_guys#, df_results_board
    
    def guys_eat(self):
        df_distmatrix = self.get_distmatrix()
        # Simple first approximation: All the guys eat all the food they can within their distance of X
        # Get the distance for all guys to all food.
        
        # Find the food that was eaten and find out which food was eaten by whom:
        removed_food, eat_dict = find_eaten_food(df_distmatrix)
        # Add points:
        for eater_index, eaten in eat_dict.items():
            for _ in range(len(eaten)): # The guy can eat more than 1 food if lucky.
                self.guys[eater_index].eat_food() # Assume all food counts for 1 point for now.
        # Remove the food 
        for food_index in sorted(removed_food, reverse=True):
            del self.food_list[food_index]

    
    def get_distmatrix(self):

        df_distmatrix = pd.DataFrame(index = range(len(self.guys)), columns = range(len(self.food_list))) 
        for i, guy in enumerate(self.guys):
            for j, food in enumerate(self.food_list):
                dist_0 = guy.pos[0] - food.pos[0]
                dist_1 = guy.pos[1] - food.pos[1]
                distance = np.sqrt(dist_0**2 + dist_1**2)
                df_distmatrix.iloc[i,j] = distance
        return df_distmatrix

        
def find_eaten_food(df_distmatrix):
        # Find all food that will be eaten:
        food_distance = 1 # Length of mouth
        eat_match = df_distmatrix < food_distance
        removed_food = set() #Set of the food that has been eaten this turn
        eat_dict = {} # dict of what food each guy has eaten.
        for guy_ind, row in eat_match.iterrows():
            eat_dict[guy_ind] = set()
            for food_ind, eaten in row.items():
                if eaten:
                    removed_food.add(food_ind)
                    eat_dict[guy_ind].add(food_ind)
        return removed_food, eat_dict