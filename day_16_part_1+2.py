def improve(a):
    return '{}0{}'.format(a, a[::-1].translate(str.maketrans('01', '10')))

def get_checksum(data):

    size = len(data)
    div = (size // 2) - 2 if (size // 2) % 2 == 0 else (size // 2) - 1

    # find suitable eg. biggest even divisor (div) where quotient is odd
    while True:
        if size % div == 0 and (size // div % 2 != 0):
            break
        else:
            div -= 2

    new_checksum = []
    # split input into div parts
    for i in range(size//div):
        c = data[(i * div):((i * div) + div)]
        init =  0 if c.count('1')% 2 == 0 else 1
        new_checksum.append(1-init)

    return "".join(map(str,new_checksum))

sizes = [272, 35651584]
for disc_size in sizes:
    data = "10111011111001111"
    while len(data) < disc_size:
        data =  improve(data)

    res = get_checksum(data[:disc_size])

    print("Checksum for size {}: {}".format(disc_size, res))
