
X = [line.split("\t") for line in open("../data/day2.txt").read().split("\n")[:-1]]
X = [[float(_x) for _x in x] for x in X]

#################PART1#################


def min_max_diff(x):

    _min = min(x)
    _max = max(x)
    return (_max - _min)


out = sum([min_max_diff(x) for x in X])
print(out)
########################################


#################PART2##################
from itertools import permutations

out = 0
for x in X:
    perms = permutations(x, 2)
    o = [p[0] / p[1] for p in perms if p[0] % p[1] == 0][0]
    out = out + o

print(out)
########################################
