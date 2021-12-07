with open('day7input.txt') as input:
    crab_positions = [int(i) for i in input.read().split(',')]
crab_positions.sort()

median = crab_positions[len(crab_positions) // 2]
burn = sum([abs(i - median) for i in crab_positions])

def vari_burn(a, b):
    return (abs(b - a) / 2) * (abs(b - a) + 1)

def min_burn(input_positions):
    burns = []
    for x in range(int(min(input_positions)), int(max(input_positions)) + 1):
        burns.append(sum([vari_burn(x, i) for i in input_positions]))
    return int(min(burns))

print(burn)
print(min_burn(crab_positions))
