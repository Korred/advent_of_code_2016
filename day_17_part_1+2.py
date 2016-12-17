import hashlib

def find_short_long(passcode, start, end, size):

    moves = {
        0: ('U', lambda x, y: (x, y - 1)),
        1: ('D', lambda x, y: (x, y + 1)),
        2: ('L', lambda x, y: (x - 1, y)),
        3: ('R', lambda x, y: (x + 1, y))}
    pass_len = len(passcode)
    frontier = [(start, passcode)]
    shortest = None
    longest = None

    while frontier:
        curr = frontier.pop(0)
        if curr[0] == end:
            if not shortest:
                shortest = curr[1][pass_len:]
            longest = curr[1][pass_len:]
        else:
            doors = hashlib.md5((curr[1]).encode("utf-8")).hexdigest()[:4]

            for e, d in enumerate(doors):
                if d in ("bcdef"):
                    new_pos = moves[e][1](*curr[0])
                    if size[0] > new_pos[0] >= 0 and size[1] > new_pos[1] >= 0:
                        new_code = curr[1] + moves[e][0]
                        frontier.append((new_pos, new_code))

    return ((len(shortest), shortest), (len(longest), longest))

passcode = 'lpvhkcbi'
paths = find_short_long(passcode, (0, 0), (3, 3), (4, 4))
print("Shortest path (length {}): {}".format(*paths[0]))
print("Longest path (length {}): {}".format(*paths[1]))
