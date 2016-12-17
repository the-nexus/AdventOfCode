#alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

#function that increments the letters in a password
def incrementPass(password):
    incrementPrevious = True
    i = len(password) - 1
    while incrementPrevious and i >= 0:
        if password[i] == "z":
            incrementPrevious = True
        else:
            incrementPrevious = False
        password[i] = alphabet[(alphabet.index(password[i]) + 1) % len(alphabet)]
        i = i - 1

#unction that returns a new password based on the input string
def newPassword(oldPass):
    #split the letters into a list
    newPass = list(oldPass)
    
    #increment the password while it isn't valid
    validPass = False
    while not validPass:
        incrementPass(newPass)
        
        #check the increasing alphabet character
        for i in range(len(newPass)-2):
            index = alphabet.index(newPass[i])
            if index < len(alphabet) - 2 and newPass[i + 1] == alphabet[index + 1] and newPass[i + 2] == alphabet[index + 2]:
                validPass = True
                break
        #increment if check failed    
        if not validPass:
            continue
        validPass = False
        #check the invalid letters and increment if check failed
        if "i" in newPass or "o" in newPass or "l" in newPass:
            continue
        #check if it contains 2 set of double letters (non overlapping (a.k.a 'aaa'))
        i = 0
        doubleCount = 0
        while doubleCount < 2 and i < len(newPass) - 1:
            if newPass[i] == newPass[i + 1]:
                doubleCount = doubleCount + 1
                i = i + 1
            i = i + 1
        if doubleCount >= 2:
            validPass = True
        
        
    #merge the letter list into a string
    newPass = "".join(newPass)
    return newPass

#-----------------------------------------------------------------
#read the input file to get the old password
oldPass = open("day11_input.txt", "r").readline()

newPass1 = newPassword(oldPass)
newPass2 = newPassword(newPass1)

#print the result
print("Santa's first new password is: ", newPass1)
print("Santa's second new password is: ", newPass2)
