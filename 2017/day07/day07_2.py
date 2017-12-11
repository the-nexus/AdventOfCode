def findRootName(programs):
    root_programs = []
    for program in programs:
        if len(program) > 2:
            root_programs.append(program)

    root_name = ""
    for root in root_programs:
        found = False
        for other_root in root_programs:
            if root[0] in other_root[2:]:
                found = True
                break
        if not found:
            root_name = root[0]
            break

    return root_name



def findUnbalancedProgram(programs, root_name):

    program_idx = [program[0] for program in programs].index(root_name)
    program = programs[program_idx]
    program_name = program[0]
    weight_correction = 0
    total_weight = int(program[1])

    if len(program) > 2:
        weights = {}
        for child_root_name in program[2:]:
            temp_program_name, temp_weight_correction, temp_total_weight = findUnbalancedProgram(programs, child_root_name)
            if temp_weight_correction != 0:
                return temp_program_name, temp_weight_correction, 0

            if not (temp_total_weight in weights.keys()):
                weights[temp_total_weight] = []
            weights[temp_total_weight].append(temp_program_name)

        keys = weights.keys()
        if len(keys) > 1:
            for idx in range(len(keys)):
                if len(weights[keys[idx]]) == 1:
                    program_name = weights[keys[idx]][0]
                    weight_correction = keys[(idx + 1) % len(keys)] - keys[idx]
                    break
        else:
            common_weight = keys[0]
            total_weight = total_weight + (len(weights[common_weight]) * common_weight)

    return program_name, weight_correction, total_weight



filename = "./day07/day07_input.txt"
input_file = open(filename)
lines = input_file.readlines()
programs = [line.replace("-> ", "").replace(",", "").replace("(", "").replace(")", "").split() for line in lines]

program_name, weight_correction, total_weight = findUnbalancedProgram(programs, findRootName(programs))
program_idx = [program[0] for program in programs].index(program_name)
program_weight = int(programs[program_idx][1])

print("The program", program_name, "is unbalanced. It should have a weight of", program_weight + weight_correction)
