code = [int(x) for x in open("../data/day_8.txt").read().split(" ")]
# print(code)


metas = []


def parse_code(code, idx):
    global metas
    initial_idx = idx
    n_branches = code[idx]
    n_meta = code[idx + 1]

    for b in range(n_branches):
        shifted = parse_code(code, idx + 2)
        idx = idx + shifted


    idx += n_meta
    return idx - initial_idx + 2


parse_code(code, 0)
print(sum(metas))
