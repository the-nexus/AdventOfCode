#open the input file
lines = open("day14_input.txt", "r").readlines()

duration = 1000 #seconds

#list the reindeers and their traits
reindeers = []
for line in lines:
    data = line.split()
    reindeer = {}
    reindeer["name"] = data[0]
    reindeer["speed"] = int(data[3])
    reindeer["flytime"] = int(data[6])
    reindeer["resttime"] = int(data[13])
    reindeer["points"] = 0
    reindeers.append(reindeer)



#---------------------------------------------------------------------------------------
#check which reindeer has the lead (and distance it travelled) at 2503s

def distance(reindeer, racetime):
    cycles = racetime / (reindeer["flytime"] + reindeer["resttime"])
    crumbs = (cycles - int(cycles)) * (reindeer["flytime"] + reindeer["resttime"])
    dist = int(cycles)*reindeer["flytime"] * reindeer["speed"]
    if reindeer["flytime"] < crumbs:
        dist = dist + reindeer["flytime"] * reindeer["speed"]
    else:
        dist = dist + crumbs * reindeer["speed"]
    return dist

def raceDistance(racetime):
    leadName = ""
    leadDist = 0
    for reindeer in reindeers:
        dist = distance(reindeer, racetime)
        if dist > leadDist:
            leadDist = dist
            leadName = reindeer["name"]
    return (leadName, leadDist)

lead = raceDistance(duration)

#print the results
print("The leading reindeer is", lead[0], "at", lead[1], "m")



#---------------------------------------------------------------------------------------
#check which reindeer has the most points at 2503s

def racePoints(racetime):
    for time in range(1, racetime+1):
        leader = raceDistance(time)
        for reindeer in reindeers:
            reindeerDist = distance(reindeer, time)
            if reindeerDist == leader[1]:
                reindeer["points"] = reindeer["points"] + 1
    leadName = ""
    leadPoints = 0
    for reindeer in reindeers:
        print(reindeer)
        if reindeer["points"] > leadPoints:
            leadPoints = reindeer["points"]
            leadName = reindeer["name"]
    return (leadName, leadPoints)

lead = racePoints(duration)

#print the results
print("The leading reindeer is", lead[0], "at", lead[1], "points")
