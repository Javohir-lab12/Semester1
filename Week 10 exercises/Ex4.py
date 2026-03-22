recipe = {
    "flour": 500,
    "sugar": 200,
    "eggs": 3,
    "milk": 100,
    "vanilla": 5
}

pantry = {
    "flour": 400,       # We have some, but not enough (need 100 more)
    "eggs": 10,         # We have plenty (need 0)
    "milk": 100,        # We have exact amount (need 0)
    # sugar is missing completely (need 200)
    # vanilla is missing completely (need 5)
}
shopping_list = {}
for ingridient , amount_needed in recipe.items():
    amount_have = pantry.get(ingridient , 0)
    difference = amount_needed - amount_have
    if difference > 0:
        shopping_list[ingridient] = difference
print(shopping_list)