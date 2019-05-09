import re
from operator import add


def extract_features(string):

    splited = string.split(" ")

    return splited[0],\
        [int(x) for x in splited[2][:-1].split(",")],\
        [int(x) for x in splited[-1].split("x")]


def draw_outline(input):
    max_row = max(e[1][0] + e[2][0] for e in input)
    max_col = max(e[1][1] + e[2][1] for e in input)
    return [[[] for c in range(max_col)] for r in range(max_row)]


def fill_up(features):

    starting_x = features[1][0]
    starting_y = features[1][1]

    dim_x = features[2][0]
    dim_y = features[2][1]

    for x in range(starting_x, starting_x + dim_x):
        for y in range(starting_y, starting_y + dim_y):
            outline[x][y].append(features[0])
    return outline


def check_unique(features):

    starting_x = features[1][0]
    starting_y = features[1][1]

    dim_x = features[2][0]
    dim_y = features[2][1]

    matching_goal = dim_x * dim_y
    # print("matching_goal:{}".format(matching_goal))
    matching_count = 0
    for x in range(starting_x, starting_x + dim_x):
        for y in range(starting_y, starting_y + dim_y):
            if features[0] in outline[x][y] and len(outline[x][y]) == 1:
                matching_count = matching_count + 1
    if matching_count == matching_goal:
        return print(features[0])



# extract features
features = [extract_features(line) for line in open("../data/day3.txt").read().split("\n")[:-1]]
# createa an outline
outline = draw_outline(features)
# fill up the outline with the features providided
[fill_up(feature) for feature in features]
# check for each claims if number of elem in the list is 1
[check_unique(feature) for feature in features]
