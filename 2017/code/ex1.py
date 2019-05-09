from itertools import islice
from itertools import cycle

x = open("../data/day1.txt").read().split("\n")[0]


x_1 = islice(cycle(iter(x)), 0, len(x))
x_2 = islice(cycle(iter(x)), 1, len(x) + 1)

pairs = zip(x_1, x_2)

Y_1 = sum([int(p[0]) for p in pairs if p[0] == p[1]])

print("ans_1:",Y_1) # Answer for part 1
print("\n\n")


x_1 = islice(cycle(iter(x)), 0, int(len(x)/2))
x_2 = islice(cycle(iter(x)), int(len(x)/2), len(x) + 1)
j
pairs = zip(x_1, x_2)

Y_2 = sum([int(p[0]) + int(p[1]) for p in pairs if p[0] == p[1]])

print("ans_2:",Y_2) # Answer for part 1




