import hashlib
door_id = "uqwqemis"
password = [None]*8
found = 0
i = 0

while found < 8:
  to_hash = door_id + str(i)
  res = hashlib.md5(to_hash.encode("utf-8")).hexdigest()
  
  try:
    pos = int(res[5])
  except ValueError:
    i += 1
    continue
  
  if res[:5] == '00000' and pos in range(8):
    if password[pos] is None:
      print(to_hash, res, res[5], res[6])
      found += 1
      password[pos] = res[6]
  i += 1
  
print("Password: ", "".join(password))
