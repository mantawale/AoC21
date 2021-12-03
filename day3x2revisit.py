with open('day3input.txt') as input:
    report = input.read().splitlines()

def answer(testlist,criteria):  # return decimal int by applying Day 3 puzzle criteria to list input
    cursor = 0

    while len(testlist) > 1:  # strip elements from list input until only one remains
        count = 0
        bitcheck = 0

        for i in testlist:  # determine most common value for currently selected bit accross all items in input list
            if int(i[cursor]) == 1:
                count += 1
            else:
                count -= 1
     
        if count >= 0:  # set comparison value for applying Day 3 puzzle criteria to input list
            bitcheck = 1

        if criteria == 'mc': # applying criteria for most common bit value
            testlist[:] = (x for x in testlist if int(x[cursor]) == bitcheck)
            
        if criteria == 'lc': # applying criteria for least common bit value
            testlist[:] = (x for x in testlist if int(x[cursor]) != bitcheck)
            
        cursor += 1
    
    return int(testlist[0],2)

oxy = report[:]
carb = report[:]

print(answer(oxy, 'mc')*answer(carb, 'lc'))
