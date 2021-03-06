with open('day2input.txt') as input:
    instructions = input.readlines()

    horizontal = 0
    aim = 0
    depth = 0

    for i in instructions:
        if 'forward' in i:
            horizontal += int(i[8:])
            depth += aim * int(i[8:])
        if 'down' in i:
            aim += int(i[5:])
        if 'up' in i:
            aim -= int(i[3:])

print(horizontal*depth)
