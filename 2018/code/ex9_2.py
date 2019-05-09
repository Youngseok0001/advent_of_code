from itertools import cycle
from collections import deque

def parse(file_path):
    import re
    raw = open(file_path).read()[:-1]
    return re.findall("[0-9]{1,}", raw)

n_player, last_marble = parse("../data/day9.txt")
n_player = int(n_player)
last_marble = 100 * int(last_marble)

score_dict = {f"{i}th_player": 0 for i in range(1, n_player + 1)}
player_gen = cycle(range(1, n_player + 1))
c_list = deque([0])

for ith_ball in range(1, last_marble + 1):
    nth_player = next(player_gen)
    if ith_ball % 23 is not 0:
        c_list.rotate(-1)
        c_list.append(ith_ball)
    else:
        c_list.rotate(7)
        removed = c_list.pop()
        score_dict[f"{nth_player}th_player"] += ith_ball + removed
        c_list.rotate(-1)
print(max(score_dict.values()))
