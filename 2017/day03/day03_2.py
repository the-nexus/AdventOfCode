def sum_matrix(matrix, line_start, line_end, column_start, column_end):
    total_sum = 0
    for line_idx in range(line_start, line_end + 1):
        for column_idx in range(column_start, column_end + 1):
            total_sum = total_sum + matrix[line_idx][column_idx]
    return total_sum

filename = "./day03/day03_input.txt"
input_file = open(filename)
lines = input_file.readlines()

square_value = int(lines[0])

layer_length = 1

while layer_length**4 < square_value:
    layer_length = layer_length + 2

half_length = layer_length // 2

line_idx = half_length + 1
column_idx = half_length + 1
memory = [[0 for _ in range(layer_length + 2)] for _ in range(layer_length + 2)]
memory[line_idx][column_idx] = 1
steps = 0
layer_length = 1
current_value = 1
while current_value <= square_value:
    layer_length = layer_length + 2
    column_idx = column_idx + 1
    for idx in range(layer_length - 1):
        if idx != 0:
            line_idx = line_idx - 1
        current_value = sum_matrix(memory, line_idx - 1, line_idx + 1, column_idx - 1, column_idx + 1)
        memory[line_idx][column_idx] = current_value
        if current_value > square_value:
            break
    
    if current_value > square_value:
        break
    for idx in range(layer_length - 1):
        column_idx = column_idx - 1
        current_value = sum_matrix(memory, line_idx - 1, line_idx + 1, column_idx - 1, column_idx + 1)
        memory[line_idx][column_idx] = current_value
        if current_value > square_value:
            break
    
    if current_value > square_value:
        break
    for idx in range(layer_length - 1):
        line_idx = line_idx + 1
        current_value = sum_matrix(memory, line_idx - 1, line_idx + 1, column_idx - 1, column_idx + 1)
        memory[line_idx][column_idx] = current_value
        if current_value > square_value:
            break
    
    if current_value > square_value:
        break
    for idx in range(layer_length - 1):
        column_idx = column_idx + 1
        current_value = sum_matrix(memory, line_idx - 1, line_idx + 1, column_idx - 1, column_idx + 1)
        memory[line_idx][column_idx] = current_value
        if current_value > square_value:
            break

# memory_string = []
# for i in range(len(memory)):
#     for j in range(len(memory[0])):
#         memory_string.append(str(memory[i][j]))
#         memory_string.append("\t")
#     memory_string.append("\n")
# memory_string = str.join("", memory_string)
# print (memory_string)

print ("The The larger value is:", current_value)