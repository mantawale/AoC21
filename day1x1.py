with open('day1input.txt') as input:
    depths = input.readlines()

increasecount = 0

for i in range(1, len(depths)):
    if int(depths[i]) > int(depths[i - 1]):
        increasecount += 1

print(increasecount)
