from itertools import cycle


def parse(data_path):

    cr_dict = {"^": "|", "v": "|", ">": "-", "<": "-"}
    c_class = cr_dict.keys()

    raw = [[e for e in line] for line in
           open(data_path).read().split("\n")[:-1]]

    rs = [[val if val not in c_class else cr_dict.get(val) for val in vals] for vals in raw]

    cs = [[[y, x], val, cycle(iter(["l", "s", "r"]))]
          for y, vals in enumerate(raw)
          for x, val in enumerate(vals) if val in c_class]

    return rs, cs


def move(rs, c):
    if c[1] == ">":
        c[0] = [c[0][0], c[0][1] + 1]
    elif c[1] == "<":
        c[0] = [c[0][0], c[0][1] - 1]
    elif c[1] == "^":
        c[0] = [c[0][0] - 1, c[0][1]]
    elif c[1] == "v":
        c[0] = [c[0][0] + 1, c[0][1]]

    c = update_mmt(c, c[1], c[2], rs[c[0][0]][c[0][1]])
    return c


def update_mmt(c, mmt, a_iter, r):

    act_m_dict_1 = {"l,v": ">", "l,>": "^", "l,^": "<", "l,<": "v",
                    "s,v": "v", "s,>": ">", "s,^": "^", "s,<": "<",
                    "r,v": "<", "r,>": "v", "r,^": ">", "r,<": "^"}

    act_m_dict_2 = {"/,^": ">", "/,<": "v", "/,>": "^", "/,v": "<",
                    "\\,>": "v", "\\,^": "<", "\\,v": ">", "\\,<": "^"}

    if r not in ["/", "\\", "+"]:
        return c

    elif r == "+":
        act_m = ",".join([next(a_iter), mmt])
        c[2] = a_iter
        c[1] = act_m_dict_1[act_m]
        return c

    elif r in ["/", "\\"]:
        act_m = ",".join([r, mmt])
        c[1] = act_m_dict_2[act_m]
        return c


data_path = "../data/day13.txt"
rs, cs = parse(data_path)

initial_lenght = len(cs)
while len(cs) > (initial_lenght - 2):
    cs = sorted(cs, key=lambda x: (x[0][0], x[0][1]), reverse=True)
    for _ in range(len(cs)):
        c = cs.pop()
        updated_c = move(rs, c)
        if any([True if updated_c[0] == c[0] else False for c in cs]) == True:
            cs = [c for c in cs if c[0] != updated_c[0]]
            print(updated_c)
        else:
            cs = [updated_c] + cs
