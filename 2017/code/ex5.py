X = [int(x) for x in open("../data/day5.txt").read().split("\n")[:-1]]
#X = [0, 3, 0, 1, -3]


pointer = 0
step = 0

while pointer < len(X):

    n_jumps = X[pointer]
    if n_jumps >= 3:
        X[pointer] = X[pointer] - 1

    else:
        X[pointer] = X[pointer] + 1

    pointer = pointer + n_jumps
    step = step + 1


print(step)
