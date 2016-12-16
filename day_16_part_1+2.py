def improve(a):
    b =  a[-1::-1].replace('1', '2').replace('0', '1').replace('2', '0')
    return a + '0' + b

def get_checksum(data):
    checksum = []
    for i in range(len(data)//2):
        a, b = data[(i * 2):(i * 2 + 2)]
        checksum.append(str((int(a) + int(b) + 1) % 2))
    checksum = "".join(checksum)
    if len(checksum) % 2 == 0:
        return get_checksum(checksum)
    else:
        return checksum

sizes = [272, 35651584]

for disc_size in sizes:
    data = "10111011111001111"
    while len(data) < disc_size:
        data = improve(data)

    res = get_checksum(data[:disc_size])

    print("Correct checksum using size {}: {}".format(disc_size, res))
    
