def create_empty_grid(max_row, max_col):
    return [[[] for y in range(max_y)] for x in range(max_x)]


def cal_dist(coord, city_name, city_coord):
    dist_x = abs(coord[0] - city_coord[0])
    dist_y = abs(coord[1] - city_coord[1])
    dist = dist_x + dist_y
    city_dist[city_name] = dist


def closest(coord, cities):
    global city_dist
    city_dist = {}
    [cal_dist(coord, city_name, city_coord) for city_name, city_coord in cities.items()]
    min_dist = min([items for key, items in city_dist.items()])
    min_city = [key for key, items in city_dist.items() if items == min_dist]
    return min_city


def area(i, filled_grid):
    count = 0
    for x in range(len(filled_grid)):
        for y in range(len(filled_grid[x])):
            if "city_{}".format(i) in filled_grid[x][y] and len(filled_grid[x][y]) == 1:
                if "city_{}".format(i) in filled_grid[x][0] +\
                        filled_grid[0][y] +\
                        filled_grid[x][-1] +\
                        filled_grid[-1][y]:
                    return "Inf"
                else:
                    count = count + 1

    return count


input = [[int(x) for x in line.split(",")] for line in open("../data/day_6.txt").read().split("\n")[:-1]]
cities = {"city_{}".format(i): input[i] for i in range(len(input))}
max_x = max([e[0] for e in input])
max_y = max([e[1] for e in input])
empty_grid = create_empty_grid(max_x, max_y)
filled_grid = [[closest((x, y), cities) for y in range(max_y)] for x in range(max_x)]
print(["city_{}:{}".format(i, area(i, filled_grid)) for i in range(len(input))])
