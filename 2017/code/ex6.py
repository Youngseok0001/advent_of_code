#X = [0, 2, 7, 0]
X = [int(i) for i in open("../data/day6.txt").read()[:-1].split('\t')]
cache = []
pointer = X.index(max(X))

# PART 1
def redistribute(X_origin, pointer):

    X = X_origin.copy()
    val_pointer = X[pointer]
    X[pointer] = 0

    while val_pointer != 0:
        val_pointer = val_pointer - 1
        pointer = pointer + 1
        X[pointer % len(X)] = X[pointer % len(X)] + 1

    pointer = X.index(max(X))
    return X, pointer


def run(cache, X, pointer):

    i = 1
    while True:
        cache.append(X.copy())
        X, pointer = redistribute(X, pointer)
        if X in cache:
            break
        i = i + 1

    print(i)
    return X


X = run(cache, X, pointer)

# PART 2
#index = [i for i, c in enumerate(cache) if c == X][0]

print(len(cache) - cache.index(X))