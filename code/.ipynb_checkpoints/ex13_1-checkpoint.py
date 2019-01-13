# ---
# jupyter:
#   jupytext_format_version: '1.2'
#   kernelspec:
#     display_name: Ignore This
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.5
# ---

from itertools import cycle


def parse(data_path):

    cr_dict = {"^": "|", "v": "|", ">": "-", "<": "-"}
    c_class = cr_dict.keys()

    raw = [[e for e in line] for line in
           open(data_path).read().split("\n")[:-1]]

    rs = [[val if val not in c_class else cr_dict.get(val) for val in vals] for vals in raw]

    cs = [(y, x, cycle(iter(["l", "s", "r"])), val) for y, vals in enumerate(raw) for x, val in enumerate(vals) if val in c_class]

    return rs, cs


def move(rs, cs):
    cs = sorted(cs, key=lambda x: (x[0], x[1]))
    new_cs = []
    for c in cs:
        new_c = []
        if c[3] == ">":
            new_c.append(c[0])
            new_c.append(c[1] + 1)
        elif c[3] == "<":
            new_c.append(c[0])
            new_c.append(c[1] - 1)
        elif c[3] == "^":
            new_c.append(c[0] - 1)
            new_c.append(c[1])
        elif c[3] == "v":
            new_c.append(c[0] + 1)
            new_c.append(c[1])
        new_c = update_mmt(new_c, c[2], c[3], rs[new_c[0]][new_c[1]])
        new_cs.append(new_c)

    return rs, new_cs


def update_mmt(new_c, a_iter, mmt, r):

    act_m_dict_1 = {"l,v": ">", "l,>": "^", "l,^": "<", "l,<": "v",
                    "s,v": "v", "s,>": ">", "s,^": "^", "s,<": "<",
                    "r,v": "<", "r,>": "v", "r,^": ">", "r,<": "^"}

    act_m_dict_2 = {"/,^": ">", "/,<": "v", "/,>": "^", "/,v": "<",
                    "\\,>": "v", "\\,^": "<", "\\,v": ">", "\\,<": "^"}

    if r not in ["/", "\\", "+"]:
        new_c.append(a_iter)
        new_c.append(mmt)
        return new_c
    elif r == "+":
        act_m = ",".join([next(a_iter), mmt])
        new_c.append(a_iter)
        new_c.append(act_m_dict_1[act_m])
        return new_c
    elif r in ["/", "\\"]:
        act_m = ",".join([r, mmt])
        new_c.append(a_iter)
        new_c.append(act_m_dict_2[act_m])
        return new_c


data_path = "../data/day13.txt"
rs, cs = parse(data_path)
while True:
    rs, cs = move(rs, cs)
    cs_xy = [(c[0], c[1]) for c in cs]
    u_cs_xy = list(set(cs_xy))
    [cs_xy.remove(u_c) for u_c in u_cs_xy]
    if len(cs_xy) != 0:
        print(cs_xy)
        break
