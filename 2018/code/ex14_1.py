def generate(recipes, cook_1, cook_2):

    new_recipes = [int(r) for r in str(recipes[cook_1] + recipes[cook_2])]
    recipes += new_recipes
    cook_1 = (recipes[cook_1] + cook_1 + 1) % len(recipes)
    cook_2 = (recipes[cook_2] + cook_2 + 1) % len(recipes)
    return recipes, cook_1, cook_2

recipes_n = 330121 
recipes = [3,7]
cook_1 = 0
cook_2 = 1

while True:
   recipes, cook_1, cook_2 = generate(recipes, cook_1, cook_2)
   if len(recipes) > recipes_n + 9:
        print("".join([str(i) for i in recipes[recipes_n:recipes_n+10]]))
        break
    
