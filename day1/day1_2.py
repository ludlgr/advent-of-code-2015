with open('input', 'r') as my_input:
    directions = my_input.read()

floor = 0
step = 0

while floor >= 0:
    step += 1
    if directions[step-1] == "(":
        floor += 1
    else:
        floor -= 1


print(step)
