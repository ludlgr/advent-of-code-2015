import hashlib

input = "bgvyzdsv"

num = 0
value_found = False

while not value_found:
    num += 1
    s = input + str(num)
    enc = hashlib.md5(s.encode())
    hash = enc.hexdigest()

    if hash.startswith("00000") and hash[5] in "123456789":
        value_found = True

print(num)
