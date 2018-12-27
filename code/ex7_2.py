from collections import OrderedDict, Counter
from functools import reduce
import re


def create_path_dict(line):
    if line[0] in path_dict.keys():
        path_dict[line[0]].append(line[1])
    else:
        path_dict[line[0]] = [line[1]]


def create_freq_dict(lines):
    Alphabets_1 = [line[1] for line in lines]
    Alphabets_2 = [line[0] for line in lines]
    freq_dict = Counter(Alphabets_1)
    Alphabets = list(set(Alphabets_1 + Alphabets_2))
    for Alphabet in Alphabets:
        if Alphabet in freq_dict.keys():
            pass
        else:
            freq_dict[Alphabet] = 0
    return freq_dict


def my_print(path_dict, freq_dict):

    answer = []
    while True:
        candidates = [key for key, values in freq_dict.items() if values == 0]
        # print(candidates)
        answer.append(candidates[0])

        try:
            values = path_dict.pop(candidates[0])
        except KeyError:
            break

        for value in values + [candidates[0]]:
            freq_dict[value] = freq_dict[value] - 1

    return answer


lines = open("../data/day7.txt").read().split(".\n")[:-1]
pattern = "Step ([A-Z]{1}) .* step ([A-Z]{1}) .*"
lines = [re.findall(pattern, line)[0] for line in lines]
path_dict = OrderedDict()
[create_path_dict(line) for line in lines]
print(path_dict)
freq_dict = create_freq_dict(lines)
print(freq_dict)
print("".join(my_print(path_dict, freq_dict)))
