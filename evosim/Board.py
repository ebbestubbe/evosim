from evosim.Guy import calc_newpos


class Board:
    def __init__(self, guys):
        self.guys = guys

    def propagate(self):
        for guy in self.guys:
            guy.set_target(self)
            newpos = calc_newpos(old_pos=guy.pos, target=guy.target, speed=guy.speed)
            guy.move(newpos)
