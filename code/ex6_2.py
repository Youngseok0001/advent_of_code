def cal_dist(coord, city_name, city_coord):
    dist_x = abs(coord[0] - city_coord[0])
    dist_y = abs(coord[1] - city_coord[1])
    dist = dist_x + dist_y
    city_dist[city_name] = dist


def within_n(coord, cities):
    global city_dist
    city_dist = {}
    [cal_dist(coord, city_name, city_coord) for city_name, city_coord in cities.items()]
    sum_dist = sum([items for key, items in city_dist.items()])
    if sum_dist < 10000:
        return 1
    else:
        return 0


input = [[int(x) for x in line.split(",")] for line in open("../data/day_6.txt").read().split("\n")[:-1]]
cities = {"city_{}".format(i): input[i] for i in range(len(input))}
max_x = max([e[0] for e in input])
max_y = max([e[1] for e in input])
filled_grid = [[within_n((x, y), cities) for y in range(max_y)] for x in range(max_x)]
print(sum([sum([filled_grid[x][y] for y in range(max_y)]) for x in range(max_x)]))
