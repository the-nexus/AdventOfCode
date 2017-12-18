filename = "./day13/day13_input.txt"
input_file = open(filename)
lines = input_file.readlines()

firewall = []
for line in lines:
    layer = [int(arg) for arg in line.replace("\n", "").split(": ")]
    firewall.append(layer)

severity = 0
layer_idx = 0
for step in range(firewall[len(firewall) - 1][0] + 1):
    layer_depth = firewall[layer_idx][0]
    if step == layer_depth:
        layer_range = firewall[layer_idx][1]
        layer_idx = layer_idx + 1
        
        scanner_idx = step % (2 * layer_range - 2)
        scanner_idx = scanner_idx if scanner_idx < layer_range else layer_range - (scanner_idx - layer_range) - 2

        print(scanner_idx)

        if scanner_idx == 0:
            severity = severity + (step * layer_range)

print("The severity of the trip is", severity)