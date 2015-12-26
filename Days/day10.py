#read the input number string
startingNumber = open("day10_input.txt", "r").readline()

#---------------------------------------
maxIt = 50
number = startingNumber

#process the number string 'maxIt' times
for it in range(maxIt):
    print(it)
    count = 0
    curNum = ""
    newNumber = []
    #process each number in the number string
    for num in number:
        if num != curNum:   #if this is a different character, reset it to the new character
            if count > 0:   #but add it and its count to the new number string beforehand
                newNumber.append(str(count))
                newNumber.append(curNum)
            curNum = num
            count = 0
        #count the occurence
        count = count + 1
    #finish and set the new number string
    newNumber.append(str(count))
    newNumber.append(curNum)
    number = "".join(newNumber)

#print the results
print("The length of the final result is: ", len(number))
