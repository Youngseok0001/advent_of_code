from collections import OrderedDict, Counter
from functools import reduce
import re
from utils import name_generator
import string


def create_path_dict(lines):
    path_dict = {}
    for line in lines:
        if line[0] in path_dict.keys():
            path_dict[line[0]].append(line[1])
        else:
            path_dict[line[0]] = [line[1]]
    return path_dict


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


def create_work_amount_dict():
    return {letter: i + 1 + 60 for i, letter in enumerate(string.ascii_uppercase)}


def allocate_do_remove_work(worker_dict, candidates):

    # allocate
    for worker_name, sub_dict in worker_dict.items():
        if sub_dict["now_working"] == None and len(candidates) != 0:
            work_to_be_added = candidates.pop()
            sub_dict["now_working"] = work_to_be_added
            sub_dict["days_left"] = amount_dict[work_to_be_added]

    # do
    for worker_name, sub_dict in worker_dict.items():
        if sub_dict["now_working"] is not None:
            sub_dict["days_left"] = sub_dict["days_left"] - 1

    # remove
    work_done = []
    for worker_name, sub_dict in worker_dict.items():
        if sub_dict["days_left"] == 0:
            work_done.append(sub_dict["now_working"])
            sub_dict["now_working"] = None
            sub_dict["days_left"] = None
    return work_done


def do_your_project(freq_dict, path_dict, worker_dict, amount_dict):
    iter = 0
    while True:
        iter = iter + 1
        candidates = [k for k, v in freq_dict.items() if v == 0]
        working = [v["now_working"] for v in worker_dict.values()]
        candidates = [c for c in candidates if c not in working]
        candidates = sorted(candidates, reverse=True)
        work_done = allocate_do_remove_work(worker_dict, candidates)
        for w in work_done:
            next_work = path_dict.pop(w)
            for x in [w] + next_work:
                freq_dict[x] = freq_dict[x] - 1

        print(iter)


lines = open("../data/day7.txt").read().split(".\n")[:-1]
pattern = "Step ([A-Z]{1}) .* step ([A-Z]{1}) .*"
lines = [re.findall(pattern, line)[0] for line in lines]
path_dict = create_path_dict(lines)
freq_dict = create_freq_dict(lines)
amount_dict = create_work_amount_dict()
worker_dict = {"worker_{}".format(i): {"now_working": None, "days_left": None} for i in range(5)}
do_your_project(freq_dict, path_dict, worker_dict, amount_dict)
