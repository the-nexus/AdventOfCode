def countCombinations(containers, usedContainers, requiredVolumeLeft):
    #if all the volume was contained this is a combination
    if requiredVolumeLeft == 0:
        return (1, len(usedContainers))
    else:
        #check if at least one unused conatainer can contain the remaining volume
        count = 0
        minContainers = float("inf")
        lastContainer = 0
        if len(usedContainers) > 0:
            lastContainer = usedContainers[-1]
        usedContainers.append(-1)
        for i in range(lastContainer, len(containers)):
            if i not in usedContainers and containers[i] <= requiredVolumeLeft:
                usedContainers[-1] = i
                results = countCombinations(containers, list(usedContainers), requiredVolumeLeft - containers[i])
                count = count + results[0]
                if results[1] < minContainers:
                    minContainers = results[1]
        return (count, minContainers)

def countMinimumCombinations(containers, minimumAmount, usedContainers, requiredVolumeLeft):
    #print the current data
    #print(usedContainers)
    #if all the volume was contained this is a combination
    if requiredVolumeLeft == 0 and len(usedContainers) == minimumAmount:
        return 1
    elif requiredVolumeLeft == 0:
        return 0
    else:
        #check if at least one unused conatainer can contain the remaining volume
        count = 0
        lastContainer = 0
        if len(usedContainers) > 0:
            lastContainer = usedContainers[-1]
        usedContainers.append(-1)
        for i in range(lastContainer, len(containers)):
            if i not in usedContainers and containers[i] <= requiredVolumeLeft:
                usedContainers[-1] = i
                results = countMinimumCombinations(containers, minimumAmount, list(usedContainers), requiredVolumeLeft - containers[i])
                count = count + results
        return count

#get the lines from the input file
lines = open("day17_input.txt", "r").readlines()
requiredVolume = 150 #Liters
containers = []
for line in lines:
    containers.append(int(line))


#-------------------------------------------------------------------------------------------
#count the combinations and the minimum amount of containers
results = countCombinations(containers, [], requiredVolume)
#print the results
print("There are", results[0], "combinations possible, with a minimum of", results[1], "containers")


#-------------------------------------------------------------------------------------------
#count the combinations using the minimum amount of containers
results = countMinimumCombinations(containers, results[1], [], requiredVolume)
#print the results
print("There are", results, "combinations possible using the minimum amount of containers")
