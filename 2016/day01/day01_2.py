# Read the input file for the movement instructions
instructions = open("day01_input.txt", "r").read().split(", ")

# Initialize the position and the look direction
x = 0
y = 0
look_direction = 0

# List of the visited positions
visited_positions = ["0,0"]
found_location = False

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

    for step in range(move_distance):
        # Move by one step
        if compass_direction == 0:      # North
            y += 1
        elif compass_direction == 1:    # East
            x += 1
        elif compass_direction == 2:    # South
            y -= 1
        else:                           # West
            x -= 1

        # Create a string to easily compare the positions
        new_position = ",".join([str(x), str(y)])

        # Check if we already visited this position
        if new_position in visited_positions:
            # If we did, stop moving
            found_location = True
            break

        # Add the position to the visited list
        visited_positions.append(new_position)

    # Check if we found the location
    if found_location:
        # If we did, stop moving
        break

# Calculate the total distance to travel
total_distance = abs(x) + abs(y)

# Display the final answer
print(total_distance)
