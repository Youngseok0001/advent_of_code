
from itertools import cycle, accumulate, islice, chain, groupby
import re

def get_set(list):
    return {e:list.count(e) for e in list}

def get_2_3(dic):
    return [e[1] for e in dic.items() if e[1] in [2,3]]

lists = [line for line in open("../data/day2.1.txt","r").read().split("\n")]
dicts = [get_set(list) for list in lists]
two_three = [list(set(get_2_3(dic))) for dic in dicts]
two = [1 for e in two_three if 2 in e]
two_sum = sum(two)
three = [1 for e in two_three if 3 in e]
three_sum = sum(three)

two_times_three = two_sum * three_sum
print(two_times_three)
