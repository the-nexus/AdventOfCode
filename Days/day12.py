#read the input file and process it as a json file
import json
data = json.load(open("day12_input.txt", "r"))

#-------------------------------------------------------------------
#function that returns the sum of all integers in the json file
def getSum(data):
    totalSum = 0
    if isinstance(data, int):
        totalSum = totalSum + data
    elif isinstance(data, str):
        totalSum = totalSum
    else:
        for item in data:
            if isinstance(data, dict):
                totalSum = totalSum + getSum(data[item])
            elif isinstance(data, list):
                totalSum = totalSum + getSum(item)
    return totalSum

#-------------------------------------------------------------------
#function that verifies if the data is a dictionnary containing red
def containsRed(data):
    redFound = False
    if isinstance(data, dict):
        for item in data.values():
            if isinstance(item, str):
                if item == "red":
                    redFound = True
                    break
    return redFound

#function that returns the sum of all integers in the json file but
#that ignores all dictionnaries that contains the string value "red"
def getSumIgnoreRed(data):
    totalSum = 0
    if isinstance(data, int):
        totalSum = totalSum + data
    elif isinstance(data, str):
        totalSum = totalSum
    else:
        ignore = containsRed(data)
        if not ignore:
            for item in data:
                if isinstance(data, dict):
                    totalSum = totalSum + getSumIgnoreRed(data[item])
                elif isinstance(data, list):
                    totalSum = totalSum + getSumIgnoreRed(item)
    return totalSum

#-------------------------------------------------------------------

totalSum = getSum(data)
totalSumIgnore = getSumIgnoreRed(data)

#print the results
print("The sum of all integers in the json file is: ", totalSum)
print("The sum of all integers in the json file (ignoring \"red\") is: ", totalSumIgnore)
                
