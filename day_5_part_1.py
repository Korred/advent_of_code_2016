import hashlib
door_id = "uqwqemis"
password = ""
found = 0
i = 0

while found < 8:
  to_hash = door_id + str(i)
  res = hashlib.md5(to_hash.encode("utf-8")).hexdigest()
  if res[:5] == '00000':
    print(to_hash, res, res[5])
    found += 1
    password += res[5]
  i += 1
  
print("Password: ", password)
