import hashlib

passcode = 'lpvhkcbi'

def find_shortest(passcode, start, end):

    move = {0: ("U", (0, -1)), 1: ("D", (0, 1)), 2: ("L", (-1, 0)), 3: ("R", (1, 0))}
    frontier = [(start, passcode)]

    while True:
        try:
            curr = frontier.pop(0)
        except IndexError:
            print("No valid path")
            return None
        if curr[0] == end:
            return curr[1][len(passcode):]
        doors = hashlib.md5((curr[1]).encode("utf-8")).hexdigest()[:4]

        for e, d in enumerate(doors):
            if d in ("b", "c", "d", "e", "f"):
                new_pos = (curr[0][0] + move[e][1][0]), (curr[0][1] + move[e][1][1])
                if new_pos[0] >= 0 and new_pos[1] >= 0:
                    new_code = curr[1] + move[e][0]
                    frontier.append((new_pos, new_code))


print("Shortest path: ", find_shortest(passcode, (0, 0), (3, 3)))
