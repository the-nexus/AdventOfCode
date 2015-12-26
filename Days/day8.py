#-------------------------------------------------
#open the file
file = open("day8_input.txt", "r")

literalCount = 0
memoryCount = 0

#for each line of the file
for line in file:
    #add the amount of characters on the line for the literal length
    literalCount = literalCount + len(line)

    #count the actual in-memory length
    lineMemoryCount = len(line)
    
    i = 0
    while i < len(line):
        if line[i] == "\\":
            if line[i + 1] == "x":
                lineMemoryCount = lineMemoryCount - 3
                i = i + 3
            else:
                lineMemoryCount = lineMemoryCount - 1
                i = i + 1
        elif line[i] == "\"":
            lineMemoryCount = lineMemoryCount - 1
        i = i + 1
                                                                      
    memoryCount = memoryCount + lineMemoryCount

#display the results
print("There is a difference of ",  literalCount - memoryCount, " characters between the strings")

#-------------------------------------------------
#open the file
file = open("day8_input.txt", "r")

literalCount = 0
memoryCount = 0

#for each line of the file
for line in file:
    #add the amount of characters on the line for the literal length
    memoryCount = memoryCount + len(line)

    #count the actual in-memory length
    lineLiteralCount = len(line)
    
    i = 0
    while i < len(line):
        if line[i] == "\\":
                lineLiteralCount = lineLiteralCount + 1
        elif line[i] == "\"":
            lineLiteralCount = lineLiteralCount + 1
        i = i + 1
                                                                      
    literalCount = literalCount + lineLiteralCount + 2

#display the results
print("There is a difference of ",  literalCount - memoryCount, " characters between the strings")
