def navigate_robot(grid, commands):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                start = (i, j)
            else:
                continue
    a, b =start
    for command in commands:
        if not grid[a][b] == "X":
            grid[a][b] = "*"
        if a < 0:
            a += 1
        if b < 0:
            b += 1
        if command == "R":
            if not grid[a][b+1] == "X":
                b += 1
            else:
                continue
        elif command == "L":
            if not grid[a][b-1] == "X":
                b -= 1
            else:
                continue
        elif command == "U":
            if not grid[a-1][b] == "X":
                a -= 1
            else:
                continue
        elif command == "D":
            if not grid[a+1][b] == "X":
                a += 1
            else:
                continue
        else:
            continue
    return (a, b)

warehouse = [
    [".", ".", "X", ".", "."],
    [".", "S", ".", "X", "."],
    [".", ".", ".", ".", "."],
    ["X", "X", "X", ".", "."]
]
moves = "RRDDRU" 
final_pos = navigate_robot(warehouse, moves)
for row in warehouse:
    print(row)
print(f"Final Position: {final_pos}")