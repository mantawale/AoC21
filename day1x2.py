with open('day1input.txt') as input:
    depths = input.readlines()

tripdepths = []
for i in range(0, len(depths) - 2):
    tripsum = int(depths[i]) + int(depths[i + 1]) + int(depths[i + 2])
    tripdepths.append(tripsum)

increasecount = 0
for i in range(1, len(tripdepths)):
    if tripdepths[i] > tripdepths[i-1]:
        increasecount += 1

print(increasecount)
