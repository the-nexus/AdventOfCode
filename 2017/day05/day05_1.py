filename = "./day05/day05_input.txt"
input_file = open(filename)
lines = input_file.readlines()

jump_list = [int(elem) for elem in lines]

current_idx = 0
step_count = 0
while current_idx >= 0 and current_idx < len(jump_list):
    next_idx = current_idx + jump_list[current_idx]
    jump_list[current_idx] = jump_list[current_idx] + 1
    current_idx = next_idx
    step_count = step_count + 1


print("Completed in", step_count, "steps")