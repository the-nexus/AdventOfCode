def isConditionMet(value_a, comparator, value_b):
    if comparator == "!=":
        return value_a != value_b

    if comparator == "==":
        return value_a == value_b

    if comparator == ">":
        return value_a > value_b

    if comparator == ">=":
        return value_a >= value_b

    if comparator == "<":
        return value_a < value_b

    if comparator == "<=":
        return value_a <= value_b

    return False



filename = "./day08/day08_input.txt"
input_file = open(filename)
lines = input_file.readlines()

registers = {}

for line in lines:
    instructions = line.split()
    reg_key = instructions[0]
    should_increment = (instructions[1] == "inc")
    diff_value = int(instructions[2])
    comp_reg_key = instructions[4]
    comparator = instructions[5]
    comp_value = int(instructions[6])

    if reg_key not in registers.keys():
        registers[reg_key] = 0
    if comp_reg_key not in registers.keys():
        registers[comp_reg_key] = 0
    
    if isConditionMet(registers[comp_reg_key], comparator, comp_value):
        registers[reg_key] = registers[reg_key] + (diff_value if should_increment else -diff_value)

print("The largest register value is", max(registers.values()))