import re

def parse(dir):
    raw = open(dir,"r").read().split("\n")[:-1]
    init_state = "".join(re.findall("[/.#]",raw[0]))
    rules = [re.split(" => #",r)[0] for r in raw[2:]]
    return init_state, rules

def new_grow(state, idx, rules):

    state = ["."] * 4 + state + ["."] * 4
    idx -= 2
    state = ["".join(state[e-2:e+3]) for e in range(2,len(state)-2)]
    new_state = "".join(["#" if e in rules else "." for e in state])
    new_state_trimed = re.findall("\\.{1,}(#.*)", new_state)[0]
    idx -= len(new_state_trimed) - len(new_state)
    new_state_trimed = [s for s in re.findall("(#.*#)\\.{1,}", new_state_trimed)[0]]
    print("".join(new_state_trimed))
    print(idx)
    return new_state_trimed, idx

gen_num = 20
idx = 0
state, rules = parse("../data/day12.txt")
state = [s for s in state]
print("".join(state))

for i in range(gen_num):
     print("generation_{}".format(i))
     state, idx = new_grow(state, idx, rules)
print(sum([1 * i[1] for i in list(zip(state,range(idx,len(state)))) if i[0] == "#"]))




