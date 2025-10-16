with open('input', 'r') as my_input:
    directions = my_input.read()

address = (0, 0)
houses = set()
houses.add(address)

for c in directions:
    if c == ">":
        address = (address[0]+1, address[1])
    elif c == "<":
        address = (address[0]-1, address[1])
    elif c == "^":
        address = (address[0], address[1]+1)
    elif c == "v":
        address = (address[0], address[1]-1)

    houses.add(address)

print(houses)
print(len(houses))
