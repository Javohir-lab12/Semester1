print("--- Running Total Calculator ---")
print("Enter numbers to add them up. Type 'done' to see the total.")
total = 0
while True:
    user_input = input("Enter a number or 'done': ")
    if user_input =="done":
       print("--- Final Calculation ---")
       print(f"The final sum of all numbers is: {total} ")
       break
    else:
        total = total + float(user_input)
        print(f"Current total: {total}")