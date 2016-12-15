import re

def is_free(x, y, fav):
    num = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + fav
    return not bool(len(re.findall(r'1', str(bin(num)))) % 2)

def find_shortest(s, e, fav):
    dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))
    lookup = {start: True}
    frontier = [(s, 0)]
    explored = set()

    while(True):
        if not frontier:
            raise ValueError("Cannot reach {} from {}!".format(e, s))
        node = frontier.pop(0)
        if node[0] == e:
            return  node[1]
        explored.add(node[0])

        for i in range(4):
            x, y = node[0][0] + dirs[i][0], node[0][1] + dirs[i][1]
            cost = node[1] + 1
            new = ((x, y), cost)

            if x < 0 or y < 0:
                continue

            if (x, y) not in explored:
                if (x, y) in lookup:
                    # if pos is a wall -> skip neighbor
                    if not lookup[(x, y)]:
                        continue
                else:
                    t = is_free(x, y, fav)
                    lookup[(x, y)] = t
                    if not t:
                        continue

                for f in frontier:
                    if f[0] == (x, y) and f[1] > cost:
                        f[1] = cost
                        continue
                frontier.append(new)


data = 1352
start = (1, 1)
end = (31, 39)

print("Shortest path: ", find_shortest(start, end, data))
