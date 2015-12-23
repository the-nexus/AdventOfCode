#open the file
file = open("day3_input.txt", "r")
text = file.read()


#-------------------------------------------------
x = 0
y = 0

visitedHouses = ["(" + str(x) + ", " + str(y) + ")"]

for i in range(0, len(text)):
    direction = text[i]

    if direction == '^':
        y = y + 1
    elif direction == 'v':
        y = y - 1
    elif direction == '>':
        x = x + 1
    elif direction == '<':
            x = x - 1
    house = "(" + str(x) + ", " + str(y) + ")"
    if house not in visitedHouses:
        visitedHouses.append(house)

#display result
print("Santa visited ", len(visitedHouses), " houses at least once")


#-------------------------------------------------
santaX = 0
santaY = 0
robotX = santaX
robotY = santaY

visitedHouses = ["(" + str(santaX) + ", " + str(santaY) + ")"]

for i in range(0, len(text)):
    direction = text[i]

    if i%2 == 0:
        x = santaX
        y = santaY
    else:
        x = robotX
        y = robotY
    
    if direction == '^':
        y = y + 1
    elif direction == 'v':
        y = y - 1
    elif direction == '>':
        x = x + 1
    elif direction == '<':
        x = x - 1
        
    if i%2 == 0:
        santaX = x
        santaY = y
    else:
        robotX = x
        robotY = y

    house = "(" + str(x) + ", " + str(y) + ")"
    if house not in visitedHouses:
        visitedHouses.append(house)

#display result
print("Santa and Robo-Santa visited ", len(visitedHouses), " houses at least once")
