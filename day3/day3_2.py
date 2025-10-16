def get_addresses(directions):
    houses = set()
    address = (0, 0)
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

    return houses

with open('input', 'r') as my_input:
    directions = my_input.read()

santa_moves = [directions[i] for i in range(len(directions)) if i % 2 == 0]
robot_moves = [directions[i] for i in range(len(directions)) if i % 2 != 0]

santa_houses = get_addresses(santa_moves)
robot_houses = get_addresses(robot_moves)
houses = santa_houses.union(robot_houses)

print(len(houses))
