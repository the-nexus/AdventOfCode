# Read the input file for the movement instructions
instructions = open("day01_input.txt", "r").read().split(", ")

# Initialize the position and the look direction
x = 0
y = 0
look_direction = 0


# Parse each instruction
for instruction in instructions:
    turn_direction = instruction[0]
    move_distance = int(instruction[1:])

    # Turn on the spot
    if turn_direction == "R":
        look_direction += 1
    else:
        look_direction -= 1

    # Advance the position
    compass_direction = look_direction % 4

    if compass_direction == 0:      # North
        y += move_distance
    elif compass_direction == 1:    # East
        x += move_distance
    elif compass_direction == 2:    # South
        y -= move_distance
    else:                           # West
        x -= move_distance

# Calculate the total distance to travel
total_distance = abs(x) + abs(y)

# Display the final answer
print(total_distance)
