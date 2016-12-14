import hashlib, re
salt = "yjdafjpo"
keys = []
i = 0

while len(keys) < 64:
    first_key = hashlib.md5((salt + str(i)).encode("utf-8")).hexdigest()
    # for every 3-gram in key
    m1 = re.search(r'(.)\1{2,2}', first_key)
    if m1:
        for j in range(i + 1, i + 1001):
            second_key = hashlib.md5((salt + str(j)).encode("utf-8")).hexdigest()
            m2 = re.search(r'(.)\1{4,4}', second_key)
            if m2:
                if m2.group()[:3] == m1.group():
                    keys.append((i, first_key))
                    print(i, first_key)
                    break
    i += 1
print("64th key found at index: ", keys[-1][0])
