#function that arranges the list of guests to generate the most happiness
def makeHappiness(relations, guestOrder, happiness):
    if len(guestOrder) == len(relations):
        guestA = guestOrder[-1]
        guestB = guestOrder[0]
        happiness = happiness + relations[guestA][guestB] + relations[guestB][guestA]
        #if happiness > 500:
            #print(guestOrder, happiness)
        return (guestOrder, happiness)

    maxHappiness = -float("inf")
    maxOrder = []

    if len(guestOrder) > 0:
        guestA = guestOrder[-1]
        guestOrder.append("")
        for guestB in relations[guestA]:
            if guestB not in guestOrder:
                guestOrder[-1] = guestB
                data = makeHappiness(relations, list(guestOrder), happiness + relations[guestA][guestB] + relations[guestB][guestA])
                if data[1] > maxHappiness:
                    maxHappiness = data[1]
                    maxOrder = data[0]
    else:
        guestOrder.append("")
        for guestA in relations:
            guestOrder[-1] = guestA
            data = makeHappiness(relations, list(guestOrder), happiness)
            if data[1] > maxHappiness:
                maxHappiness = data[1]
                maxOrder = data[0]


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

data = makeHappiness(relations, [], 0)
print("ANSWER:")
print(data[0], data[1])
