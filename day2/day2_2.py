total_ribbon = 0

with open('input', 'r') as my_input:
    for line in my_input:
        dimensions = line.replace("\n", "").split("x")
        dimensions = [int(x) for x in dimensions]
        dimensions.sort()
        total_ribbon += (2*dimensions[0] + 2*dimensions[1]) + dimensions[0]*dimensions[1]*dimensions[2]

print(total_ribbon)
