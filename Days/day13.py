#function that arranges the list of guests to generate the most happiness
def makeHappiness(relations, guestOrder, happiness):
    if len(guestOrder) == len(relations):
        return (guestOrder, happiness)

    maxHappiness = -float("inf")
    maxOrder = []

    if len(guestOrder) > 0:
        guestA = guestOrder[-1]
        for guestB in relations[guest[A]]:
            if guestB not in guestOrder:
                data = makeHappiness(relations, [guestOrder, guestB], happiness + relations[guestA][guestB])
                if data[1] > maxHappiness:
                    maxHappiness = data[1]
                    maxOrder = data[0]
    else:
        for guestA in relations:
            makeHappiness(relations, [guestA], happiness)


    return (maxOrder, maxHappiness)


#open the input file and get the lines
lines = open("day13_input.txt", "r").readlines()

#get the guest list
guests = []
for line in lines:
    data = line.split()
    if data[0] not in guests:
        guests.append(data[0])
    if data[10][:-1] not in guests:
        guests.append(data[10][:-1])

#set the relation matrix of the guests
#(relation of guest A towards guest B)
relations = {}
for guestA in guests:
    relations[guestA] = {}
    for guestB in guests:
        if guestB != guestA:
            relations[guestA][guestB] = 0

for line in lines:
    data = line.split()
    happiness = int(data[3])
    if data[2] == "lose":
        happiness = -happiness
    relations[data[0]][data[10][:-1]] = happiness

#makeHappiness(relations, [], 0)
#print(relations)

temp = [1, 2, 3]
otherTemp = [temp, 4]
print(temp)
print(otherTemp)
