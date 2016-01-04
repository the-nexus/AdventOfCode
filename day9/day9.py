#function that returns the shortest trip path
def shortestTrip(distances, visitedCities, length):
    #if all cities have been visited, return the path and the length
    if visitedCities and len(visitedCities) == len(distances):
        #print(" -> ".join(visitedCities), length)
        return (" -> ".join(visitedCities), length)
    
    #else go through each unvisited city to continue the trip
    shortestPath = ""
    shortestDist = float("inf")
    #if this is the first city that will be visited
    if not visitedCities:
        visitedCities = [""]
        for city in distances.keys():
            if city not in visitedCities:
                visitedCities[0] = city
                trip = shortestTrip(distances, list(visitedCities), length)
                if trip[1] < shortestDist:
                    shortestDist = trip[1]
                    shortestPath = trip[0]
    #if this isn't the first city to be visited
    else:
        visitedCities.append("")
        for city in distances.keys():
            if city not in visitedCities and distances[visitedCities[-2]][city] < float("inf"):
                visitedCities[-1] = city
                trip = shortestTrip(distances, list(visitedCities), length + distances[visitedCities[-2]][city])
                if trip[1] < shortestDist:
                    shortestDist = trip[1]
                    shortestPath = trip[0]
    return (shortestPath, shortestDist)



#function that returns the shortest trip path
def longestTrip(distances, visitedCities, length):
    #if all cities have been visited, return the path and the length
    if visitedCities and len(visitedCities) == len(distances):
        #print(" -> ".join(visitedCities), length)
        return (" -> ".join(visitedCities), length)
    
    #else go through each unvisited city to continue the trip
    longestPath = ""
    longestDist = -1
    #if this is the first city that will be visited
    if not visitedCities:
        visitedCities = [""]
        for city in distances.keys():
            if city not in visitedCities:
                visitedCities[0] = city
                trip = longestTrip(distances, list(visitedCities), length)
                if trip[1] > longestDist:
                    longestDist = trip[1]
                    longestPath = trip[0]
    #if this isn't the first city to be visited
    else:
        visitedCities.append("")
        for city in distances.keys():
            if city not in visitedCities and distances[visitedCities[-2]][city] < float("inf"):
                visitedCities[-1] = city
                trip = longestTrip(distances, list(visitedCities), length + distances[visitedCities[-2]][city])
                if trip[1] > longestDist:
                    longestDist = trip[1]
                    longestPath = trip[0]
    return (longestPath, longestDist)



#get the lines in the input file
lines = open("day9_input.txt", "r").readlines()

#list the cities
cities = []
for line in lines:
    data = line.split()
    if data[0] not in cities:
        cities.append(data[0])
    if data[2] not in cities:
        cities.append(data[2])

#create the distance table
distances = {}
for departure in cities:
    distances[departure] = {}
    for destination in cities:
        distances[departure][destination] = float("inf")

for line in lines:
    data = line.split()
    distances[data[0]][data[2]] = int(data[4])
    distances[data[2]][data[0]] = int(data[4])

shortest = shortestTrip(distances, [], 0)
longest = longestTrip(distances, [], 0)

#print the results
print("The shortest trip is ", shortest[0], " which has a length of ", shortest[1])
print("The longest trip is ", longest[0], " which has a length of ", longest[1])
