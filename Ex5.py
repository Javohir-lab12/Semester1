grid = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

"""First way"""
for i in range(len(grid)):
   grid[i] = list(map(lambda n: n+10 if n+10 <= 255 else 255, grid[i]))

"""Second way"""
grid = [[n+10 if n+10 <=255 else 255 for n in row] for row in grid]

"""Third way"""
for i in range(len(grid)):
    for j in range(len(grid[i])):
         if grid[i][j] + 10 <= 255:
            grid[i][j] += 10
         else:
            grid[i][j] = 255

print(grid)