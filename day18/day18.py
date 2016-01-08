def lightsToString(lights):
    lightStr = []
    for lightLine in lights:
        for l in lightLine:
            if l == 1:
                lightStr.append("#")
            else:
                lightStr.append(".")
        lightStr.append("\n")
    return "".join(lightStr)



#open the input file and parse the data
lines = open("day18_input.txt", "r").readlines()

width = len(lines[0])
height = len(lines)
maxIt = 4

lights = [[0 for j in range(0, width)] for i in range(0, height)]

for i in range(0, len(lines)):
    line = lines[i].replace("\n", "")
    for j in range(0, len(line)):
        lights[i][j] = (1 if line[j] == "#" else 0)

print(lightsToString(lights))
for it in range(0, maxIt):
    nextLights = [[0 for j in range(0, width)] for i in range(0, height)]
    for i in range(0, height):
        for j in range(0, width):
            count = 0
            for ii in range(-1, 2):
                line = i + ii
                for jj in range(-1, 2):
                    column = j + jj
                    if line >= 0 and line < height and column >= 0 and column < width and line != i and column != j:
                        count = count + lights[line][column]
            if lights[i][j] == 1 and (count == 2 or count == 3):
                nextLights[i][j] = 1
            elif lights[i][j] == 0 and count == 3:
                nextLights[i][j] == 1
            if i == 0 and j == 2:
                print(count)
    lights = nextLights
    print(lightsToString(lights))
lightCount = 0
for lightLine in lights:
    lightCount = lightCount + lightLine.count(1)
print("There are", lightCount, "light lights on")
