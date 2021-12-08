def analyze_signal(signal_set):

    one = next(i for i in signal_set if len(i) == 2)
    four = next(i for i in signal_set if len(i) == 4)
    seven = next(i for i in signal_set if len(i) == 3)
    eight = next(i for i in signal_set if len(i) == 7)
    nine = next(i for i in signal_set if len(i) == 6 and all(x in i for x in four))
    zero = next(i for i in signal_set if len(i) == 6 and all(x in i for x in one) and i != nine)
    six = next(i for i in signal_set if len(i) == 6 and i != zero and i != nine)
    three = next(i for i in signal_set if len(i) == 5 and all(x in i for x in one))
    five = next(i for i in signal_set if len(i) == 5 and all(x in six for x in i))
    two = next(i for i in signal_set if len(i) == 5 and i != three and i != five)
    
    return [zero, one, two, three, four, five, six, seven, eight, nine]

def interpret_output(signal, output_set):
    
    display = []
    for i in output_set:
        for k in signal:
            if all(x in k for x in i) and all(x in i for x in k):
                display.append(signal.index(k))

    return int(''.join([str(i) for i in display]))

def repair_displays(display_set):

    signal_inputs = [i[0].split() for i in display_set]
    display_outputs = [i[1].split() for i in display_set]

    corrected_disps = []
    for x in range(0, len(signal_inputs)):
        corrected_disps.append(interpret_output(analyze_signal(signal_inputs[x]), display_outputs[x]))
    
    return corrected_disps

with open('day8input.txt') as input:
    print(sum(repair_displays([i.split('|') for i in input.read().splitlines()])))
