import re
import string


input = open("../data/day5.txt").read()[:-1]
pattern = "|".join([str(lower) + str(lower.upper()) + "|" +
                    str(lower.upper()) + str(lower)
                    for lower in list(string.ascii_lowercase)])

while True:
    str_length_prev = len(input)
    input = re.sub(pattern, "", input)
    if str_length_prev == len(input):
        break

# now we have the updated input from the first exercise,
# next, we remove each alphabet one by one to test which leads
# the smallest string output

for lower in list(string.ascii_lowercase):
    new_input = re.sub(lower + "|" + lower.upper(), "", input)
    while True:
        str_length_prev = len(new_input)
        new_input = re.sub(pattern, "", new_input)
        if str_length_prev == len(new_input):
            break
    print("when {} is removed, len is {}".format(lower, str_length_prev))
