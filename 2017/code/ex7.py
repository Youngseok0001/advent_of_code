import re

raw = [i for i in open("../data/day7.txt").read().split('\n')]

def parse(x):

    splitted = x.split(" ")

    node = splitted[0]
    value = int(splitted[1][1:-1])

    if len(splitted) == 2:
        child = None
    else:
        child = [re.search("[a-z]{1,}",i).group() for i in splitted[3:]]

    return node, value, child



X = [parse(r) for r in raw]
X = {x[0]:{"value":x[1],"child":x[2]} for x in X}
temp_X = X.copy()
for k, v in X.items():
    if v["child"] is None:
        pass
    else:
        for c in v["child"]:
            if c in X.keys():
                del temp_X[c]


ev




