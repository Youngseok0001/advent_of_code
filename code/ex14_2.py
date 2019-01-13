recipes_n = "330121"
recipes = "37"
cook_1 = 0
cook_2 = 1

while recipes_n not in recipes[-7:]: 
    new_recipes = str(int(recipes[cook_1]) + int(recipes[cook_2]))
    recipes += new_recipes
    cook_1 = (int(recipes[cook_1]) + cook_1 + 1) % len(recipes)
    cook_2 = (int(recipes[cook_2]) + cook_2 + 1) % len(recipes)
    if len(recipes) % 10000 == 0:
        print(len(recipes))
print(recipes.index(recipes_n))  
    
