grid_size = int(raw_input("Enter the grid size "))

grid = []

for i in range(0, grid_size + 1):
  l1 = []
  for j in range(0, grid_size + 1):
    l1.append(0)

  grid.append(l1)

for i in range(0, grid_size + 1):
  grid[i][grid_size] = 1
  grid[grid_size][i] = 1


for i in range(grid_size - 1, -1, -1):
  for j in range(grid_size - 1, -1, -1):
    grid[i][j] = grid[i+1][j] + grid[i][j+1]

print grid[0][0]


