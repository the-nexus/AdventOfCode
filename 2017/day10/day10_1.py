filename = "./day10/day10_input.txt"
input_file = open(filename)
lines = input_file.readlines()

values = range(256)
window_lengths = [int(elem) for elem in lines[0].split(",")]

current_idx = 0
skip_size = 0
for window_length in window_lengths:
    for idx in range(window_length // 2):
        left_idx = (current_idx + idx) % len(values)
        right_idx = (current_idx + window_length - idx - 1) % len(values)
        temp = values[left_idx]
        values[left_idx] = values[right_idx]
        values[right_idx] = temp
    current_idx = (current_idx + window_length + skip_size) % len(values)
    skip_size = skip_size + 1

print("The result is", values[0] * values[1])