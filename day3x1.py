with open('day3input.txt') as input:
    report = input.read().splitlines()

def interpret_report(testlist, criteria):
    ratinglist = []
    cursor = 0

    while cursor < len(testlist[0]):
        
        count = 0
        for i in testlist:
            if int(i[cursor]) == 1:
                count += 1
            else:
                count -= 1

        bitcheck = 0
        if count > 1:
            bitcheck = 1

        if criteria == 'gamma':
            ratinglist.append(str(bitcheck))
        if criteria == 'epsilon':
            ratinglist.append(str(abs(bitcheck - 1)))

        cursor += 1

    return int(''.join(ratinglist), 2)

print(interpret_report(report, 'gamma')*interpret_report(report, 'epsilon'))
