#get the lines from the input file
lines = open("day16_input.txt", "r").readlines()

#get the parameters of each sue
sueList = []
for line in lines:
    #replace ':' and ',' in the string on only leave spaces as seperators
    line = line.replace(":", "").replace(",", "")
    data = line.split()
    sue = {}
    sue["number"] = int(data[1])
    i = 2
    while i < len(data):
        sue[data[i]] = int(data[i+1])
        i = i + 2
    sueList.append(sue)

#setup the analysed parameters
tickerTape = {}
tickerTape["children"] = 3
tickerTape["cats"] = 7
tickerTape["samoyeds"] = 2
tickerTape["pomeranians"] = 3
tickerTape["akitas"] = 0
tickerTape["vizslas"] = 0
tickerTape["goldfish"] = 5
tickerTape["trees"] = 3
tickerTape["cars"] = 2
tickerTape["perfumes"] = 1

#-------------------------------------------------------------------------
#compare the aunts to the tape
sueNumber = -1

for sue in sueList:
    theRightOne = True
    for key in sue.keys():
        if key != "number" and sue[key] != tickerTape[key]:
            theRightOne = False
            break
    if theRightOne:
        sueNumber = sue["number"]
        break

#display the results
print("The number of the right Aunt Sue is #", sueNumber)


#-------------------------------------------------------------------------
#compare the aunts with the new values
sueNumber = -1

for sue in sueList:
    theRightOne = True
    for key in sue.keys():
        if key == "number":
            continue
        elif key == "cats" or key == "trees":
            if sue[key] <= tickerTape[key]:
                theRightOne = False
                break
        elif key == "pomeranians" or key == "goldfish":
            if sue[key] >= tickerTape[key]:
                theRightOne = False
                break
        else:
            if sue[key] != tickerTape[key]:
                theRightOne = False
                break
    if theRightOne:
        sueNumber = sue["number"]
        break

#display the results
print("The number of the actual Aunt Sue is #", sueNumber)
