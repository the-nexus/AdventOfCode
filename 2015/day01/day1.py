file = open('day1_input.txt', 'r')
text = file.read()

#------------------------------
#floors going up
up = text.count('(')
#floors going down
down = text.count(')')

#floor to go
print("Final floor: ", up-down)


#------------------------------
#loop through the elements
floor = 0

for i in range(0, len(text)):
    if text[i] == '(':
        floor = floor + 1
    elif text[i] == ')':
        floor = floor - 1
    if floor < 0:
        print("Goes to the basement at: ", i+1)
        break


