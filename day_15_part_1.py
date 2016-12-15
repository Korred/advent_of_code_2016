data = '''Disc #1 has 5 positions; at time=0, it is at position 2.
Disc #2 has 13 positions; at time=0, it is at position 7.
Disc #3 has 17 positions; at time=0, it is at position 10.
Disc #4 has 3 positions; at time=0, it is at position 2.
Disc #5 has 19 positions; at time=0, it is at position 9.
Disc #6 has 7 positions; at time=0, it is at position 0.'''
import re


def load_disc_data(disc_data):
    entries = disc_data.split("\n")
    num_pos = []
    start = []
    for e in entries:
        num_pos.append(int(re.search(r'([\d]+) position', e).group(1)))
        start.append(int(re.search(r'position ([\d]+)', e).group(1)))
    return [num_pos, start]

discs = load_disc_data(data)

time = 0
shift = list(range(1, len(discs[0])+1))
solution = [0] * len(discs[0])
while True:
    pos = [(sum(i) + time) % discs[0][e] for e, i in enumerate(zip(discs[1], shift))]
    if pos == solution:
        print(time)
        break

    time += 1
