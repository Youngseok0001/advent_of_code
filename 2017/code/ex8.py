import re

X = list(open("../data/day8.txt").read().split("\n")[:-1])

def parse(x):
    grps = re.search(r"(\w+) (\w{1,}) (-?[0-9]{1,}) (.*)", x).groups()
    target, operation, value, condition = grps
    return target, operation, value, condition

def gen_init_register_ops(X):
    registers = list(set([x[0] for x in X]))
    init_ops = [(str(r) + " = 0") for r in registers]
    return init_ops

def get_registers(X):
    registers = list(set([x[0] for x in X]))
    return registers


def to_command(x):
    operation_dict = {"inc": "+=", "dec": "-="}
    target, operation, value, condition = x
    cmd = condition + ": " +\
        target + operation_dict[operation] + value
    return cmd


# X = [parse(x) for x in X]
# resisters = get_registers(X)
# init_register_ops = gen_init_register_ops(X)
# [exec(op, globals()) for op in init_register_ops]
# cmds = [to_command(x) for x in X]
# [exec(cmd, globals()) for cmd in cmds]

# for regis in resisters:
#     print(regis + ":" + str(eval(regis)))

def get_registers_dict(X):
    registers = list(set([x[0] for x in X]))
    registers_list = {r:[] for r in registers}
    return registers_list



def to_command(x):
    operation_dict = {"inc": "+=", "dec": "-="}
    target, operation, value, condition = x
    cmd = condition + ": " +\
        target + operation_dict[operation] + value
    exec(cmd,globals())
    registers_dict[target].append(eval(target))
    return cmd

X = [parse(x) for x in X]
resisters = get_registers(X)
registers_dict = get_registers_dict(X)
init_register_ops = gen_init_register_ops(X)
[exec(op, globals()) for op in init_register_ops]
[to_command(x) for x in X]

ans_2 = {k:max(v) for k,v in registers_dict.items()}