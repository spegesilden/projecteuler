grid = [[i for i in range(0,21)] for k in range(0,21)]

for i in range(0,21):
    for j in range(0,21):
        if i == 0 and j == 0:
            grid[i][j] = 1
        elif i == 0 and j > 0:
            grid[i][j] = grid[i][j-1]
        elif j == 0 and i > 0:
            grid[i][j] = grid[i-1][j]
        elif i > 0 and i <= 20 and j > 0 and j <= 20:
            grid[i][j] = grid[i-1][j] + grid[i][j-1]

print(grid[20][20])
