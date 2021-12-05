def parse_line(input_line):

    coords = [[], []]
    str_coords = [input_line.split()[0].split(','), input_line.split()[2].split(',')]
    for i in range(0, 2):
        coords[i] = [int(x) for x in str_coords[i]]

    return coords

def expand_line(input_line):

    coords = parse_line(input_line)
    if coords[0][0] == coords[1][0]:
        return y_expand(coords)
    if coords[0][1] == coords[1][1]:
        return x_expand(coords)
    else:
        return diag_expand(coords)

def x_expand(input_coords):

    output_line = input_coords[:]
    add = (output_line[1][0] - output_line[0][0]) / abs(output_line[1][0] - output_line[0][0])
    while abs(output_line[len(output_line) - 1][0] - output_line[len(output_line) - 2][0]) > 1:
        output_line.insert(len(output_line) - 1, [int(input_coords[0][0] + add), input_coords[0][1]])
        add += (output_line[1][0] - output_line[0][0]) / abs(output_line[1][0] - output_line[0][0])
        
    return output_line

def y_expand(input_coords):

    output_line = input_coords[:]
    add = (output_line[1][1] - output_line[0][1]) / abs(output_line[1][1] - output_line[0][1])
    while abs(output_line[len(output_line) - 1][1] - output_line[len(output_line) - 2][1]) > 1:
        output_line.insert(len(output_line) - 1, [input_coords[0][0], int(input_coords[0][1] + add)])
        add += (output_line[1][1] - output_line[0][1]) / abs(output_line[1][1] - output_line[0][1])

    return output_line

def diag_expand(input_coords):

    output_line = input_coords[:]
    xadd = (output_line[1][0] - output_line[0][0]) / abs(output_line[1][0] - output_line[0][0])
    yadd = (output_line[1][1] - output_line[0][1]) / abs(output_line[1][1] - output_line[0][1])
    while abs(output_line[len(output_line) - 1][1] - output_line[len(output_line) - 2][1]) > 1:
        output_line.insert(len(output_line) - 1, [input_coords[0][0] + xadd, int(input_coords[0][1] + yadd)])
        xadd += (output_line[1][0] - output_line[0][0]) / abs(output_line[1][0] - output_line[0][0])
        yadd += (output_line[1][1] - output_line[0][1]) / abs(output_line[1][1] - output_line[0][1])

    return output_line

def vent_hash(input_vent_map):

    xcoords = [x[0] for x in input_vent_map]
    xrange = max(xcoords) - min(xcoords)
    vent_hmap = []
    for i in input_vent_map:
        vent_hmap.append((i[0] + (i[1] * (xrange))))
    
    return vent_hmap

def all_vents(input_terrain):

    vent_lines = [expand_line(i) for i in input_terrain]
    vent_map = []
    for i in vent_lines:
        for k in i:
            vent_map.append(k)

    return vent_hash(vent_map)

def vent_crossings(input_terrain):

    input_vent_hmap = all_vents(input_terrain)
    crosstracker = {}
    crosspoints_list = []
    for i in input_vent_hmap:
        if i not in crosstracker:
            crosstracker[i] = 1
        else:
            if crosstracker[i] == 1:
                crosspoints_list.append(i)
            crosstracker[i] += 1
    
    return len(crosspoints_list)

with open('day5input.txt') as input:
    terrain = input.read().splitlines()

print(vent_crossings(terrain))
