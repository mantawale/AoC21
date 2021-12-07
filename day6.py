def process_fishcount(input_census):

    popl_buckets = []
    for i in range (0, 9):
        popl_buckets.append([str(i), input_census.count(str(i))])

    return popl_buckets 

def repro_cycle(population, time_scale):
    
    while time_scale > 0:
        cycle_step = [0 for x in population]

        for i in range(0, 8):
            cycle_step[i] = population[i+1][1]
        cycle_step[8] = population[0][1]
        cycle_step[6] += population[0][1]
        
        for i in range(0, 9):
            population[i][1] = cycle_step[i]
            
        time_scale -= 1

    return sum([x[1] for x in population])

with open('day6input.txt') as input:
    lanternfish_popl = process_fishcount(input.read().split(','))

print(repro_cycle(lanternfish_popl, 256))
