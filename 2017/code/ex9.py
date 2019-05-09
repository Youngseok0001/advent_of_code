import re

X = open("../data/day9.txt").read().split("\n")[0]
#X = "<{o\"i!a,<{i<a>"
# X = re.sub(r"\!.", "", X)
# X = (re.sub(r"\<(.*?)\>\,?", r"\1", X))
# X = (re.sub(r"\{", "[", X))
# X = (re.sub(r"\}", "]", X))
# X_eval = eval(X)


# def recursive(X, score):
#     score += 1
#     overall.append((score))
#     if X == []:
#         pass
#     else:

#         for x in X:
#             recursive(x, score)


# overall = []
# recursive(X_eval, 0)
# print(sum(overall))

# X = open("../data/day9.txt").read().split("\n")[0]
# X = "<{o\"i!a,<{i<a>"
X = re.sub(r"\!.", "", X)
X = re.findall(r"\<(.*?)\>\,?", X)
print(sum([len(x) for x in X]))
