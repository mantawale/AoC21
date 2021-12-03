with open('day2input.txt') as input:
    instructions = input.readlines()

    horizontal = 0
    depth = 0

    for i in instructions:
        if 'forward' in i:
            horizontal += int(i[8:])
        if 'down' in i:
            depth += int(i[5:])
        if 'up' in i:
            depth -= int(i[3:])

print(horizontal*depth)
