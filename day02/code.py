
with open("input", "r") as fh:
    lines = fh.read().splitlines()
    input = []
    for line in lines:
        split = line.split(" ")
        input.append([split[0][0], int(split[1])])

horiz = 0
depth = 0
for command in input:
    if command[0] == "f":
        horiz += command[1]
    elif command[0] == "d":
        depth += command[1]
    elif command[0] == "u":
        depth -= command[1]

print("Part one: ", horiz * depth)

hor = 0
dep = 0
aim = 0
for command in input:
    if command[0] == "d":
        aim += command[1]
    elif command[0] == "u":
        aim -= command[1]
    elif command[0] == "f":
        hor += command[1]
        dep += (aim * command[1])

print("Part two: " , hor, dep, hor*dep)
