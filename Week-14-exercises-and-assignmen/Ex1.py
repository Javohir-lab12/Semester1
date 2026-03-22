def check_ingredients(pantry_list, recipe_list):
    pantry_list = [c.lower() for c in pantry_list]
    recipe_list = [s.lower() for s in recipe]
    recipe_list.sort()
    pantry_list.sort()
    set1 = set(pantry_list)
    set2 = set(recipe_list)
    missing = list(set2 - set1)
    available = list(set1 & set2)
    return missing, available

pantry = ["Eggs", "flour", "Milk", "eggs", "salt"]
recipe = ["flour", "milk", "Sugar", "Eggs", "butter"]

missing, available = check_ingredients(pantry, recipe)

print(f"Need to buy: {missing}")
print(f"Already have: {available}")