def processGroup(stream, start_idx):
    current_idx = start_idx
    total_garbage = 0
    while current_idx < len(stream) - 1:
        current_idx = current_idx + 1
        character = stream[current_idx]
        sub_total_garbage = 0

        if character == "}":
            break
        elif character == "{":
            sub_total_garbage, current_idx = processGroup(stream, current_idx)
        elif character == "<":
            sub_total_garbage, current_idx = processGarbage(stream, current_idx)

        total_garbage = total_garbage + sub_total_garbage

    return total_garbage, current_idx



def processGarbage(stream, start_idx):
    current_idx = start_idx
    total_garbage = 0
    ignore_character = False
    while current_idx < len(stream) - 1:
        current_idx = current_idx + 1
        character = stream[current_idx]

        if ignore_character:
            ignore_character = False
            continue

        if character == "!":
            ignore_character = True
            continue
        elif character == ">":
            break

        total_garbage = total_garbage + 1

    return total_garbage, current_idx



filename = "./day09/day09_input.txt"
input_file = open(filename)
lines = input_file.readlines()

total_garbage, current_idx = processGroup(lines[0], -1)

print("The total abount of valid garbage in the stream is", total_garbage)