
with open("input", "r") as fh:
    input = fh.read().splitlines()

counter = 0
for i in range(1, len(input)):
    if int(input[i]) > int(input[i-1]):
        counter += 1

print("Part one: ", counter)

prev = 0
counter = -1
for i in range(2, len(input)):
    s = int(input[i-2]) + int(input[i-1]) + int(input[i])
    if s > prev:
        counter += 1
    prev = s

print("Part two: ", counter)
