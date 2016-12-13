import hashlib
door_id = "uqwqemis"
password = ""
found, i = 0, 0

while found < 8:
  res = hashlib.md5((door_id + str(i)).encode("utf-8")).hexdigest()
  if res[:5] == '00000':
    found += 1
    password += res[5]
  i += 1
  
print("Password: ", password)
