# Read the input file
lines = open("day02_input.txt").readlines()

# Set the initial variables
x = 1
y = 1
code = []

# For each button instruction
for line in lines:
    for move_direction in line:
        if move_direction == "R":
            x += 1
        elif move_direction == "L":
            x -= 1
        elif move_direction == "D":
            y += 1
        else:
            y -= 1

        # Make sure the finger stays on the pad
        if x < 0:
            x = 0
        elif x > 2:
            x = 2
        if y < 0:
            y = 0
        elif y > 2:
            y = 2

    # Add the number to the code
    number = 3 * y + x + 1
    code.append(number)

# Display the code (answer)
print(code)
