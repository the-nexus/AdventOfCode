import hashlib
data = open("day4_input.txt", "r").readline()

#initialize the key iterations
i = 0
key = data + str(i)
hashString = hashlib.md5(key.encode('utf-8'))

#-------------------------------------------------------------
#Find the hash that starts with 5 '0's

#iterate through the key endings
while not hashString.hexdigest().startswith("00000"):
    i = i + 1
    key = data + str(i)
    hashString = hashlib.md5(key.encode('utf-8'))

#print the results
print("The missing key part is: ", i)

#-------------------------------------------------------------
#Find the hash that starts with 6 '0's

#iterate through the key endings from the one with 5 '0's
while not hashString.hexdigest().startswith("000000"):
    i = i + 1
    key = data + str(i)
    hashString = hashlib.md5(key.encode('utf-8'))

#print the results
print("The missing key part is: ", i)
