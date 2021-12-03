with open('day3input.txt') as input:
    report = input.read().splitlines()

def interpret_report(test_list, criteria):
    list = test_list[:]
    cursor = 0

    while len(list) > 1:

        count = 0
        for i in list:
            if int(i[cursor]) == 1:
                count += 1
            else:
                count -= 1
     
        bitcheck = 0
        if count >= 0:
            bitcheck = 1 

        if criteria == 'oxygen':
            list[:] = (x for x in list if int(x[cursor]) == bitcheck)
        if criteria == 'carbon':
            list[:] = (x for x in list if int(x[cursor]) != bitcheck)

        cursor += 1
    
    return int(list[0],2)

print(interpret_report(report, 'oxygen')*interpret_report(report, 'carbon'))
