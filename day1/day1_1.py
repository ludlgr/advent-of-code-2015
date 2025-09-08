with open('input', 'r') as my_input:
    directions = my_input.read()

floor = 0

for c in directions:
    if c == "(":
        floor += 1
    else:
        floor -= 1

print(floor)
