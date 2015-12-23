#open the input file
file = open("day6_input.txt", "r")

#create a matrix of 'gridW' columns and 'gridH' rows
#False = off
#True = on

#Turn on: set to True
#Turn off: set to False
#Toggle: invert state
gridW = 1000
gridH = 1000
lightGrid = [[False for j in range(0, gridW)] for i in range(0, gridH)]
otherLightGrid = [[0 for j in range(0, gridW)] for i in range(0, gridH)]

#go through the steps of the plan
for line in file:
    data = line.split(" ")
    if data[0] == "turn":
        #turn lights on or off
        newState = data[1] == "on"
        startCoords = data[2].split(",")
        endCoords = data[4].split(",")
        for i in range(int(startCoords[1]), int(endCoords[1])+1):
            for j in range(int(startCoords[0]), int(endCoords[0])+1):
                lightGrid[i][j] = newState
                if newState:
                    otherLightGrid[i][j] = otherLightGrid[i][j] + 1
                elif otherLightGrid[i][j] > 0:
                    otherLightGrid[i][j] = otherLightGrid[i][j] - 1
    
    else:
        #toggle lights
        startCoords = data[1].split(",")
        endCoords = data[3].split(",")
        for i in range(int(startCoords[1]), int(endCoords[1])+1):
            for j in range(int(startCoords[0]), int(endCoords[0])+1):
                lightGrid[i][j] = not lightGrid[i][j]
                otherLightGrid[i][j] = otherLightGrid[i][j] + 2

#count each line
lightsOn = 0
totalBrightness = 0

for i in range(0, gridH):
    lightsOn = lightsOn + lightGrid[i].count(True)
    totalBrightness = totalBrightness + sum(otherLightGrid[i])
    

#display results
print("The grid has ", lightsOn, " lights on")
print("The grid has a total brightness of ", totalBrightness)
