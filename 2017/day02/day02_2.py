import sys

def findEvenDividers(values):
    n_values = len(values)
    for i in range(n_values):
        numerator = values[i]
        for j in range(n_values):
            if i is j:
                continue

            denominator = values[j]
            if numerator % denominator is 0:
                return numerator, denominator

    return sys.maxint, sys.maxint


filename = "./day02/day02_input.txt"
input_file = open(filename)
lines = input_file.readlines()

spreadsheet = [[int(elem) for elem in line.split("\t")] for line in lines]

checksum = 0
for line in spreadsheet:
    numerator, denominator = findEvenDividers(line)
    if numerator < sys.maxint:
        checksum = checksum + (numerator / denominator)

print ("The checksum of the spreadsheet is:", checksum)