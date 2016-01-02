def bestCookie(ingredients, maxTeaspoons):
    teaspoons = [0 for ingredient in ingredients]
    return bestRecursiveCookie(ingredients, teaspoons, maxTeaspoons, 0)

def bestRecursiveCookie(ingredients, teaspoons, teaspoonsLeft, currentIngredient):
    score = 0

    if currentIngredient == len(ingredients)-1:
        teaspoons[currentIngredient] = teaspoonsLeft
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        for i in range(0, len(ingredients)):
            capacity = capacity + teaspoons[i] * ingredients[i]["capacity"]
            durability = durability + teaspoons[i] * ingredients[i]["durability"]
            flavor = flavor + teaspoons[i] * ingredients[i]["flavor"]
            texture = texture + teaspoons[i] * ingredients[i]["texture"]
        if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
            score = 0
        else:
            score = capacity * durability * flavor * texture
        return (list(teaspoons), score)
    else:
        bestScore = -float("inf")
        bestTeaspoons = []
        for i in range(0, teaspoonsLeft + 1):
            teaspoons[currentIngredient] = i
            results = bestRecursiveCookie(ingredients, teaspoons, teaspoonsLeft - i, currentIngredient + 1)
            if results[1] > bestScore:
                bestScore = results[1]
                bestTeaspoons = results[0]
        return (bestTeaspoons, bestScore)


        
def bestCookieEvar(ingredients, maxTeaspoons, wantedCalories):
    teaspoons = [0 for ingredient in ingredients]
    return bestRecursiveCookieEvar(ingredients, teaspoons, maxTeaspoons, 0, wantedCalories)

def bestRecursiveCookieEvar(ingredients, teaspoons, teaspoonsLeft, currentIngredient, wantedCalories):
    score = 0

    if currentIngredient == len(ingredients)-1:
        teaspoons[currentIngredient] = teaspoonsLeft
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        calories = 0
        for i in range(0, len(ingredients)):
            capacity = capacity + teaspoons[i] * ingredients[i]["capacity"]
            durability = durability + teaspoons[i] * ingredients[i]["durability"]
            flavor = flavor + teaspoons[i] * ingredients[i]["flavor"]
            texture = texture + teaspoons[i] * ingredients[i]["texture"]
            calories = calories + teaspoons[i] * ingredients[i]["calories"]
        if capacity < 0 or durability < 0 or flavor < 0 or texture < 0 or calories != wantedCalories:
            score = 0
        else:
            score = capacity * durability * flavor * texture
        return (list(teaspoons), score)
    else:
        bestScore = -float("inf")
        bestTeaspoons = []
        for i in range(0, teaspoonsLeft + 1):
            teaspoons[currentIngredient] = i
            results = bestRecursiveCookieEvar(ingredients, teaspoons, teaspoonsLeft - i, currentIngredient + 1, wantedCalories)
            if results[1] > bestScore:
                bestScore = results[1]
                bestTeaspoons = results[0]
        return (bestTeaspoons, bestScore)

    

#get the lines from the input file
lines = open("day15_input.txt", "r").readlines()

maxTeaspoons = 100
wantedCalories = 500

#get the list of possible ingredients and their traits
ingredients = []
for line in lines:
    #remove the unwated characters
    line = line.replace(":", "")
    line = line.replace(",", "")
    data = line.split()
    #build the ingredient dictionnary (parameters)
    ingredient = {}
    ingredient["name"] = data[0]
    ingredient["capacity"] = int(data[2])
    ingredient["durability"] = int(data[4])
    ingredient["flavor"] = int(data[6])
    ingredient["texture"] = int(data[8])
    ingredient["calories"] = int(data[10])
    #insert into our list of ingredients
    ingredients.append(ingredient)

#-----------------------------------------------------------------------
#build the best cookie
results = bestCookie(ingredients, maxTeaspoons)

#display the results
print(results[0])
print("The best cookie has a score of", results[1], "points")


#-----------------------------------------------------------------------
#build the best cookie with 500 calories
results = bestCookieEvar(ingredients, maxTeaspoons, wantedCalories)

#display the results
print(results[0])
print("The best cookie has a score of", results[1], "points")
