with open('day3input.txt') as input:
    report = input.read().splitlines()

oxy = report[:]
oxycursor = 0

while len(oxy) > 1:

    count = 0
    bitcheck = 0

    for i in oxy:
        if int(i[oxycursor]) == 1:
            count += 1
        else:
            count -= 1
   
    if count >= 0:
        bitcheck = 1

    oxy[:] = (x for x in oxy if int(x[oxycursor]) == bitcheck)
    oxycursor += 1

carb = report[:]
carbcursor = 0

while len(carb) > 1:

    count = 0
    bitcheck = 0

    for i in carb:
        if int(i[carbcursor]) == 1:
            count += 1
        else:
            count -= 1
   
    if count < 0:
        bitcheck = 1

    carb[:] = (y for y in carb if int(y[carbcursor]) == bitcheck)
    carbcursor += 1

print(int(oxy[0],2)*int(carb[0],2))