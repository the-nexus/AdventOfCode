filename = "./day01/day01_input.txt"

input_file = open(filename)
line = input_file.readline()

n_characters = len(line)
idx_offset = n_characters / 2

sum_result = 0
for idx in range(n_characters):
    current_value = int(line[idx])
    compare_value = int(line[(idx + idx_offset) % n_characters])
    if current_value is compare_value:
        sum_result = sum_result + current_value

print ("The sum of the captcha is:", sum_result)
