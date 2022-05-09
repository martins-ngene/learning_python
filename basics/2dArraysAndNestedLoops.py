
# Creating a 4X4 2D array
numbers = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 0, 1],
    [0]
]

# Nested Loops
for grid in numbers:
    print(grid)
    for col in grid:
        print(col)
