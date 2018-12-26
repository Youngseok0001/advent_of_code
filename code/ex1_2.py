from itertools import accumulate, cycle, islice, chain
from operator import add


def check_for_2nd(cum_iter):

    cache = set()

    while True:
        extracted = next(cum_iter)
        if extracted in cache:
            return extracted
        else:
            cache.add(extracted)


# step1: import file, append 0,  cycle
input_iter = (int(string) for string in open("../data/day_1.txt"))
input_iter_2 = chain(iter([0]), cycle(input_iter))
# step2: accumuate
cum_iter = accumulate(input_iter_2, add)
# step3: search for 2nd occurance
answer = check_for_2nd(cum_iter)
# step4: print the answer
print(answer)
