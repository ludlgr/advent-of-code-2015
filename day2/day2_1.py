total_paper = 0

with open('input', 'r') as my_input:
    for line in my_input:
        dimensions = line.replace("\n", "").split("x")
        dimensions = [int(x) for x in dimensions]

        sides = [dimensions[0]*dimensions[1], dimensions[1]* dimensions[2], dimensions[2]*dimensions[0]]
        n_paper = 2*sides[0] + 2*sides[1] + 2*sides[2] + min(sides)

        total_paper += n_paper

print(total_paper)
