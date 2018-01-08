def generateNumber(in_number, multiplier, divider, modulo):
    generated_value = 1
    previous_number = in_number
    while generated_value % modulo != 0:
        generated_value = (previous_number * multiplier) % divider
        previous_number = generated_value
    return generated_value

def checkNumbersMatching(number_a, number_b, bit_count):
    mask = ((1 << 16) - 1)
    return (number_a & mask) == (number_b & mask)



filename = "./day15/day15_input.txt"
input_file = open(filename)
lines = input_file.readlines()
number_a = int(lines[0].split()[-1])
number_b = int(lines[1].split()[-1])

n_iteration = 5000000
match_count = 0

for iteration in range(n_iteration):
    if checkNumbersMatching(number_a, number_b, 16):
        match_count = match_count + 1
    number_a = generateNumber(number_a, 16807, 2147483647, 4)
    number_b = generateNumber(number_b, 48271, 2147483647, 8)

print("There were", match_count, "matches")
