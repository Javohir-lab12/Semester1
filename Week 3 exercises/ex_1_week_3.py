print('--- Movie Ticket Pricer ---')
age= int(input('How old are you? '))
if age < 13:
    print('You fall into the Children category.')
    print('Your ticket price is: $8')
elif age > 12 and age < 65:
    print('You fall into the Adult category')
    print("Yourticket price is: $15")
else:
    print("You fall into the Senior category.")
    print("Your ticket price $10")