#read the input file
file = open("day5_input.txt", "r")


#------------------------------------------
minVowels = 3
minDoubles = 1
allowedInvalid = 0

vowels = "aeiou"
letters = "abcdefghijklmnopqrstuvwxyz"
invalidStrings = ["ab", "cd", "pq", "xy"]

total = 0
nice = 0

for line in file:
    total = total + 1

    #check the vowel requirement (3 vowels)
    vowelCount = 0
    for i in range(0, len(vowels)):
        vowelCount = vowelCount + line.count(vowels[i])
        if vowelCount >= minVowels:
            break
    if vowelCount < minVowels:
        continue    #not enough vowels, go to next string
    #check the double letter requirement (1 double)
    doubleCount = 0
    for i in range(0, len(letters)):
        doubleCount = doubleCount + line.count(letters[i] + letters[i])
        if doubleCount >= minDoubles:
            break
    if doubleCount < minDoubles:
        continue    #not enough doubles, go to next string

    #check the invalid strings
    invalidStringCount = 0
    for i in range(0, len(invalidStrings)):
        invalidStringCount = invalidStringCount + line.count(invalidStrings[i])
        if invalidStringCount > allowedInvalid:
            break
    if invalidStringCount > allowedInvalid:
        continue    #found an invalid string, go to next string
        
    nice = nice + 1

#display the result
print("There are ", nice, " nice strings on Santa's list ->> ", total, " (with V1)")


#------------------------------------------
file = open("day5_input.txt", "r")
nice = 0

for line in file:
    pairFound = False
    seperatedRepeatFound = False
    #check the double letter repeat (no overlap)
    for i in range(0, len(line)-3):
        pair = line[i] + line[i+1]
        for j in range(i+2, len(line)-1):
            otherPair = line[j] + line[j+1]
            if pair == otherPair:
                pairFound = True
                break
        if pairFound:
            break
    if not pairFound:
        continue

    #check the repeating letter seperated with a single letter
    for i in range(0, len(line)-2):
        if line[i] == line[i+2]:
            seperatedRepeatFound = True
            break
    if not seperatedRepeatFound:
        continue

    nice = nice + 1

#display the result
print("There are ", nice, " nice strings on Santa's list ->> ", total, " (with V2)")
