with open('day3input.txt') as input:
    report = input.read().splitlines()

cursor = 0
bitcheck = []

while cursor < len(report[0]):
    count = 0

    for i in report:
        if int(i[cursor]) == 1:
            count += 1
        else:
            count -= 1
    
    bitcheck.append(count)
    cursor += 1

gammalist = []
epsilonlist = []

for i in bitcheck:
    if  i > 0:
        gammalist.append('1')
        epsilonlist.append('0')
    else:
        gammalist.append('0')
        epsilonlist.append('1')

gamma = int(''.join(gammalist), 2)
epsilon = int(''.join(epsilonlist), 2)

print(gamma*epsilon)
