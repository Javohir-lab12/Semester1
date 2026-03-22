print("--- Triangle Pattern Printer ---")
desired_height = int(input("Enter the desired height of the triangle: "))
for row_num in range (desired_height):
    for col_num in range(row_num + 1):
        print("* ", end="")
    print()