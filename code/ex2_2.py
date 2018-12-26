from itertools import cycle, accumulate, islice, chain, groupby
import re


def str_vs_str(str_1, str_2):

    matching_n = 0
    matching = []

    for idx in range(len(str_1)):
        if str_1[idx] == str_2[idx]:
            matching.append(str_1[idx])
            matching_n = matching_n + 1
        else:
            pass

    return "".join(matching), matching_n


def matching_over_list(lists):

    for idx in range(len(lists)):

        ref = lists[idx]
        rests = lists[idx + 1:]

        [print(str_vs_str(ref, rest)[0]) for rest in rests if str_vs_str(ref, rest)[1] == len(lists[0]) - 1]


matching_over_list(list(open("../data/day2.1.txt").read().split("\n")))
