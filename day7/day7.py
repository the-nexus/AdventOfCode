numbers = "0123456789"

#----------------------------------------------------
wires = {}
initialization = True
currentLine = 0

#open the file
file = open("day7_input.txt", "r")
lines = file.readlines()

#while the list of lines has items in it
while len(lines) > 0:
    data = lines[currentLine].split()
    deleteLine = False

    #if this is the first pass
    if initialization and data[0][0] in numbers and data[1] == "->":
        wires[data[2]] = int(data[0])
        deleteLine = True

    #if this isnt the first pass
    else:
        skipLine = False
        #get the first signal input
        sigIn1 = 0
        #if the first element of the line is a NOT operator
        if data[0] == "NOT":
            #get the first input signal
            if data[1][0] in numbers:   #is a number
                wires[data[3]] = ~int(data[1])
                deleteLine = True
            elif data[1] in wires.keys():   #is a known signal
                wires[data[3]] = ~wires[data[1]]
                deleteLine = True
            skipLine = True
        elif data[0][0] in numbers:     #is a number
            sigIn1 = int(data[0])
        elif data[0] in wires.keys():   #is a known signal
            sigIn1 = wires[data[0]]
        else:
            skipLine = True

        #if the action is to foward a signal
        if not skipLine and data[1] == "->":
            wires[data[2]] = sigIn1
            deleteLine = True
        #if the action is other than to forward the signal
        elif not skipLine:
            #get the second signal input
            sigIn2 = 0
            if data[2][0] in numbers:   #is a number
                sigIn2 = int(data[2])
            elif data[2] in wires.keys():   #is a known signal
                sigIn2 = wires[data[2]]
            else:
                skipLine = True

            if not skipLine:
                sigOut = 0
                #process the operation
                if data[1] == "AND":
                    sigOut = sigIn1 & sigIn2
                elif data[1] == "OR":
                    sigOut = sigIn1 | sigIn2
                elif data[1] == "RSHIFT":
                    sigOut = sigIn1 >> sigIn2
                elif data[1] == "LSHIFT":
                    sigOut = sigIn1 << sigIn2
                else:
                    print("ERROR: Invalid operation '", data[1], "'")
                
                wires[data[4]] = sigOut
                deleteLine = True
            

    #end the init phase if we reached the end of the first pass
    if initialization and currentLine == len(lines)-1:
        initialization = False
        #print("Init completed")
        
    #delete the line if it was processed or increment the current line number
    if deleteLine:
       del lines[currentLine]
       if len(lines) > 0:
           currentLine = currentLine % len(lines)
    else:
        currentLine = (currentLine + 1) % len(lines)
    #if currentLine == 0:
        #print(len(lines), " lines left to process")



#display results
#print("DONE!")
print("The signal on wire 'a' is: ", wires["a"])



#----------------------------------------------------

bOverride = wires["a"]
wires = {}
initialization = True
currentLine = 0

#open the file
file = open("day7_input.txt", "r")
lines = file.readlines()

#while the list of lines has items in it
while len(lines) > 0:
    data = lines[currentLine].split()
    deleteLine = False

    #if this is the first pass
    if initialization and data[0][0] in numbers and data[1] == "->":
        if data[2] == "b":
            wires[data[2]] = bOverride
        else:
            wires[data[2]] = int(data[0])
        deleteLine = True

    #if this isnt the first pass
    else:
        skipLine = False
        #get the first signal input
        sigIn1 = 0
        #if the first element of the line is a NOT operator
        if data[0] == "NOT":
            #get the first input signal
            if data[1][0] in numbers:   #is a number
                wires[data[3]] = ~int(data[1])
                deleteLine = True
            elif data[1] in wires.keys():   #is a known signal
                wires[data[3]] = ~wires[data[1]]
                deleteLine = True
            skipLine = True
        elif data[0][0] in numbers:     #is a number
            sigIn1 = int(data[0])
        elif data[0] in wires.keys():   #is a known signal
            sigIn1 = wires[data[0]]
        else:
            skipLine = True

        #if the action is to foward a signal
        if not skipLine and data[1] == "->":
            wires[data[2]] = sigIn1
            deleteLine = True
        #if the action is other than to forward the signal
        elif not skipLine:
            #get the second signal input
            sigIn2 = 0
            if data[2][0] in numbers:   #is a number
                sigIn2 = int(data[2])
            elif data[2] in wires.keys():   #is a known signal
                sigIn2 = wires[data[2]]
            else:
                skipLine = True

            if not skipLine:
                sigOut = 0
                #process the operation
                if data[1] == "AND":
                    sigOut = sigIn1 & sigIn2
                elif data[1] == "OR":
                    sigOut = sigIn1 | sigIn2
                elif data[1] == "RSHIFT":
                    sigOut = sigIn1 >> sigIn2
                elif data[1] == "LSHIFT":
                    sigOut = sigIn1 << sigIn2
                else:
                    print("ERROR: Invalid operation '", data[1], "'")
                
                wires[data[4]] = sigOut
                deleteLine = True
            

    #end the init phase if we reached the end of the first pass
    if initialization and currentLine == len(lines)-1:
        initialization = False
        #print("Init completed")
        
    #delete the line if it was processed or increment the current line number
    if deleteLine:
       del lines[currentLine]
       if len(lines) > 0:
           currentLine = currentLine % len(lines)
    else:
        currentLine = (currentLine + 1) % len(lines)
    #if currentLine == 0:
        #print(len(lines), " lines left to process")



#display results
#print("DONE!")
print("The new signal on wire 'a' is: ", wires["a"])
