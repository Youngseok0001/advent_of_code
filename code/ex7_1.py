from collections import OrderedDict
from functools import reduce
import re


def create_dict(lines):
    return reduce(lambda x, y: x + y, lines)


lines = open("../data/day7.txt").read().split(".\n")

pattern = "Step ([A-Z]{1}) .* step ([A-Z]{1}) .*"
lines = [re.findall(pattern, line)[0] for line in lines]


lines = [[1, 2], [3, 4], [5, 6]]


out = reduce(lambda x, y: x + y, lines)

print(out)
