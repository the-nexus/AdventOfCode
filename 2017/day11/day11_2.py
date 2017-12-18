filename = "./day11/day11_input.txt"
input_file = open(filename)
lines = input_file.readlines()

directions = lines[0].split(",")
#directions = "se,sw,se,sw,sw".split(",")

n_axis = 0
ne_axis = 0
nw_axis = 0
max_steps = 0

for direction in directions:
    if direction == "n":
        n_axis = n_axis + 1
    elif direction == "ne":
        ne_axis = ne_axis + 1
    elif direction == "nw":
        nw_axis = nw_axis + 1
    elif direction == "s":
        n_axis = n_axis - 1
    elif direction == "sw":
        ne_axis = ne_axis - 1
    elif direction == "se":
        nw_axis = nw_axis - 1
    
    if ne_axis !=  0 and nw_axis != 0:
        if ne_axis / nw_axis > 0:
            orientation = 1 if ne_axis > 0 else -1
            steps_to_even_out = min(abs(ne_axis), abs(nw_axis))
            for i in range(steps_to_even_out):
                ne_axis = ne_axis - orientation
                nw_axis = nw_axis - orientation
                n_axis = n_axis + orientation

    if n_axis != 0 and ne_axis != 0:
        if n_axis / ne_axis < 0:
            orientation = 1 if ne_axis > 0 else -1
            steps_to_even_out = min(abs(n_axis), abs(ne_axis))
            for i in range(steps_to_even_out):
                ne_axis = ne_axis - orientation
                nw_axis = nw_axis - orientation
                n_axis = n_axis + orientation

    if n_axis != 0 and nw_axis != 0:
        if n_axis / nw_axis < 0:
            orientation = 1 if nw_axis > 0 else -1
            steps_to_even_out = min(abs(n_axis), abs(nw_axis))
            for i in range(steps_to_even_out):
                ne_axis = ne_axis - orientation
                nw_axis = nw_axis - orientation
                n_axis = n_axis + orientation
                
    n_step = abs(n_axis) + abs(ne_axis) + abs(nw_axis)
    max_steps = max(max_steps, n_step)

print("The child has been at a maximum of", max_steps, "steps from the starting point")