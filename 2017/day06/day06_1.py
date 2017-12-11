filename = "./day06/day06_input.txt"
input_file = open(filename)
lines = input_file.readlines()

memory = [int(elem) for elem in lines[0].split("\t")]

cycle_count = 0
states = []
while True:
    current_state = "\t".join([str(elem) for elem in memory])
    if current_state in states:
        break
    states.append(current_state)

    largest_value = max(memory)
    largest_idx = memory.index(largest_value)
    memory[largest_idx] = 0

    for idx in range(largest_value):
        bank_idx = (largest_idx + idx + 1) % len(memory)
        memory[bank_idx] = memory[bank_idx] + 1

    cycle_count = cycle_count + 1

print("It took", cycle_count, "cycles")