row_list = [40, 400000]
for rows in row_list:
    curr = '.^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^.'
    width = len(curr)
    safe_tiles = curr.count(".")
    left = rows-1

    while left != 0:
        prev = "".join([".", curr, "."])
        new_curr = []
        for i in range(width):
            check = prev[i:i + 3]
            new_tile = "." if check[0] == check[2] else "^"
            new_curr.append(new_tile)
        curr = "".join(new_curr)
        safe_tiles += curr.count(".")
        left -= 1

    print("{} safe tiles in {} rows".format(safe_tiles, rows))
    
