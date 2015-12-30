import json

def getSum(data):
    totalSum = 0
    for item in data:
        if isinstance(item, list):
            print("here")
            totalSum = totalSum + getSum(item)
        elif isinstance(item, dict):
            print("there")
            #for dictItem in item:
                #totalSum = totalSum + getSum(item[dictItem])
        elif isinstance(item, int):
            print("NUMBER: ", item)
        else:
            print("STRING: ", item)
    return totalSum


data = json.load(open("day12_input.txt", "r"))
#print(json.dumps(data, indent=4, sort_keys=True))
totalSum = 0
for item in data:
    print("---------------------------------------------------------")
    print("KEY: ", item)
    totalSum = totalSum + getSum(data[item])

#print(totalSum)
                
