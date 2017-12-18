def makeGroup(programs, target_program_idx):
    group = [target_program_idx]
    current_idx = 0
    while current_idx < len(group):
        targets = programs[group[current_idx]]
        for target in targets:
            if target not in group:
                group.append(target)
        current_idx = current_idx + 1
    return group


filename = "./day12/day12_input.txt"
input_file = open(filename)
lines = input_file.readlines()

programs = []

for line in lines:
    line_str = line.replace("\n", "").replace(",", "")
    line_args = line_str.split(" <-> ")
    line_args = line_args[1].split()
    programs.append([int(line_args[idx]) for idx in range(len(line_args))])

groups = []
for idx in range(len(programs)):
    grouped = False
    for group in groups:
        if idx in group:
            grouped = True
            break
    if not grouped:
        groups.append(makeGroup(programs, idx))

print("There are", len(groups), "groups")