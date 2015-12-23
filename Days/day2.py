#open the file
file = open("day2_input.txt", "r")

#iterate through the file
totalPaper = 0
totalRibbon = 0

for line in file:
    #----------------------------------------------------
    values = line.split('x')
    surface1 = int(values[0]) * int(values[1])
    surface2 = int(values[1]) * int(values[2])
    surface3 = int(values[2]) * int(values[0])
    totalPaper = totalPaper + 2*surface1 + 2*surface2 + 2*surface3 + min(surface1, surface2, surface3)

    
    #----------------------------------------------------
    perimeter = 2*(int(values[0]) + int(values[1]) + int(values[2]) - max(int(values[0]), int(values[1]), int(values[2])))
    volume = int(values[0]) * int(values[1]) * int(values[2])
    totalRibbon = totalRibbon + perimeter + volume

#display the results
print("Total surface of paper needed: ", totalPaper, " feet")
print("Total amount of ribbon needed: ", totalRibbon, " feet")
