from itertools import cycle
from blist import blist


def parse(file_path):
    import re
    raw = open(file_path).read()[:-1]
    return re.findall("[0-9]{1,}", raw)


class circular_list(list):

    def __init__(self, list):
        self.list = blist(list)
        self.current_marble_loc = 1

    def insert_marble(self, value):
        move_one = self.c_idx(self.current_marble_loc + 1)
        self.list.insert(move_one + 1, value)
        self.current_marble_loc = move_one + 1

    def pop_marble(self, n_th):
        self.current_marble_loc = self.c_idx(self.current_marble_loc + n_th)
        to_be_removed = self.list[self.current_marble_loc]
        self.list.remove(to_be_removed)
        return to_be_removed

    def c_idx(self, index):
        cir_index = index % len(self.list)
        return cir_index

n_player, last_marble = parse("../data/day9.txt")
n_player = int(n_player)
last_marble = int(last_marble)

score_dict = {f"{i}th_player": 0 for i in range(1, n_player + 1)}
player_gen = cycle(range(1, n_player + 1))

c_list = circular_list([0, 1])

for ith_ball in range(2, last_marble + 1):
    nth_player = next(player_gen)
    if ith_ball % 23 is not 0:
        c_list.insert_marble(ith_ball)
    else:
        removed = c_list.pop_marble(-7)
        score_dict[f"{nth_player}th_player"] = score_dict[f"{nth_player}th_player"] + ith_ball + removed
        
print(max(score_dict.values()))
