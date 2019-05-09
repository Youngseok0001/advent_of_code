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
        print(len(input))
        break
