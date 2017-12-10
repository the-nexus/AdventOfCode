filename = "./day02/day02_input.txt"
input_file = open(filename)
lines = input_file.readlines()

spreadsheet = [[int(elem) for elem in line.split("\t")] for line in lines]

checksum = 0
for line in spreadsheet:
    min_value = min(line)
    max_value = max(line)
    checksum = checksum + max_value - min_value

print ("The checksum of the spreadsheet is:", checksum)