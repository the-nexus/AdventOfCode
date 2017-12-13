def processGroup(stream, start_idx, group_level):
    group_score = group_level
    current_idx = start_idx
    while current_idx < len(stream) - 1:
        current_idx = current_idx + 1
        character = stream[current_idx]
        
        if character == "}":
            break
        elif character == "{":
            sub_group_score, current_idx = processGroup(stream, current_idx, group_level + 1)
            group_score = group_score + sub_group_score
        elif character == "<":
            current_idx = processGarbage(stream, current_idx)

    return group_score, current_idx



def processGarbage(stream, start_idx):
    current_idx = start_idx
    ignore_character = False
    while current_idx < len(stream) - 1:
        current_idx = current_idx + 1
        character = stream[current_idx]
        
        if ignore_character:
            ignore_character = False
            continue

        if character == "!":
            ignore_character = True
        elif character == ">":
            break

    return current_idx



filename = "./day09/day09_input.txt"
input_file = open(filename)
lines = input_file.readlines()

group_score, current_idx = processGroup(lines[0], -1, 0)

print("The score of the stream is", group_score)