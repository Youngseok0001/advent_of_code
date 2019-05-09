recipes_n = "330121"
recipes = "37"
cook_1 = 0
cook_2 = 1


class game:

    def __init__(self, recipes, cook_1, cook_2):

        self.recipes = recipes
        self.cook_1 = cook_1
        self.cook_2 = cook_2

    @property
    def change(self):
        new_recipes = str(int(self.recipes[self.cook_1]) + int(self.recipes[self.cook_2]))
        self.recipes = self.recipes + new_recipes
        self.cook_1 = (int(self.recipes[self.cook_1]) + self.cook_1 + 1) % len(self.recipes)
        self.cook_2 = (int(self.recipes[self.cook_2]) + self.cook_2 + 1) % len(self.recipes)
        return self

game_1 = game(recipes, cook_1, cook_2)
while recipes_n not in game_1.recipes[-7:]: 
    game_1.change
    if len(game_1.recipes) % 10000 == 0:
        print(len(game_1.recipes))
print(game_1.recipes.index(recipes_n))  
    
