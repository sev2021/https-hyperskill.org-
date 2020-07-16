pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

recipe_list = [pasta, apple_pie, ratatouille, chocolate_cake, omelette]
recipe_name_list = ["pasta", "apple pie", "ratatouille", "chocolate cake", "omelette"]
ingredient = input()

for i, _ in enumerate(recipe_list):
    if ingredient in recipe_list[i]:
        print(recipe_name_list[i] + " time!")
