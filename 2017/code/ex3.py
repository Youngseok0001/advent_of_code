X = 325489


### PART1 ###
move_dict = {"R": (0, 1), "U": (-1, 0), "L": (0, -1), "D": (1, 0)}

cycle = 3
move_steps = {"R": -1, "U": -1, "L": 0, "D": 0}
spiral_list = []

i = 1
loc = (0, 0)

while i <= X:

    move_steps = {k: v + 2 for k, v in move_steps.items()}
    moves = "".join([k * v for k, v in move_steps.items()])
    for move in moves:
        spiral_list.append([i, loc])

        i = i + 1
        loc = (loc[0] + move_dict[move][0],
               loc[1] + move_dict[move][1])


print(sum(abs(i) for i in spiral_list[X - 1][1]))
