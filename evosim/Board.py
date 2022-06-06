import pandas as pd

from evosim.Guy import calc_newpos


class Board:
    def __init__(self, guys):
        self.guys = guys

    def propagate(self):
        for guy in self.guys:
            guy.set_target()
            newpos = calc_newpos(old_pos=guy.pos, target=guy.target, speed=guy.speed)
            guy.move(newpos)
            guy.update_energy()

    def propagate_n(self, n):
        guy_states = {guy.name: [guy.get_state()] for guy in self.guys}
        for i in range(n):
            self.propagate()
            for guy in self.guys:
                state = guy.get_state()
                guy_states[guy.name].append(state)
        df_results = {
            name: pd.DataFrame.from_dict(states) for name, states in guy_states.items()
        }
        df_results = pd.concat(df_results, axis=1)
        return df_results
