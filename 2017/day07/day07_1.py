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



filename = "./day07/day07_input.txt"
input_file = open(filename)
lines = input_file.readlines()
programs = [line.replace("-> ", "").replace(",", "").replace("(", "").replace(")", "").split() for line in lines]

print("The root of all programs is", findRootName(programs))