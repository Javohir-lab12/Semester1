def find_saddle_point_coordinates(grid):
    row_min = []
    for i in range(len(grid)):
        row_min.append(min(grid[i]))
    saddle_point = max(row_min)
    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            column_max = max([grid[r][col_index] for r in range(len(grid))])
            if saddle_point == grid[row_index][col_index] and saddle_point == column_max:
                return [(row_index, col_index)]
    return None

grid1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(find_saddle_point_coordinates(grid1))

grid2 = [
 [-1, -2, 0], 
 [ 1, -5, 3], 
 [-4, -3, -6]
 ]
print(find_saddle_point_coordinates(grid2))

grid3 =[
 [1, 2, 3], 
 [8, 5, 9], 
 [4, 6, 7]
 ]
print(find_saddle_point_coordinates(grid3))

grid4 = [
 [5, 6, 7], 
 [4, 2, 1], 
 [3, 0,-1]
 ]
print(find_saddle_point_coordinates(grid4))