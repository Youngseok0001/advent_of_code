from collections import Counter
from itertools import combinations

X = [line.split(" ") for line in open("../data/day4.txt").read().split("\n")[:-1]]


# part 1
def is_passphrases(x):
    if len(set(x)) == len(x):
        return True
    else:
        return False


print(len([x for x in X if is_passphrases(x)]))


# part 2
def is_anagram(x):
    counter_x = [Counter(_x) for _x in x]
    combination_x = combinations(counter_x, 2)
    if any([_x[0] == _x[1] for _x in combination_x]):
        return False
    else:
        return True


X = [x for x in X if is_passphrases(x)]
print(len([x for x in X if is_anagram(x)]))
