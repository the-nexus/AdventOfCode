filename = "./day03/day03_input.txt"
input_file = open(filename)
lines = input_file.readlines()

square_value = int(lines[0])

layer_length = 1

while layer_length**2 < square_value:
    layer_length = layer_length + 2

half_length = layer_length // 2

steps = -1
for side in range(4):
    mid_side_idx = (layer_length**2 - half_length) - (side * (layer_length - 1))
    dist = abs(mid_side_idx - square_value)
    if dist <= half_length:
        steps = half_length + dist
        break

print ("The Manhattan distance of the square is", steps, "steps")