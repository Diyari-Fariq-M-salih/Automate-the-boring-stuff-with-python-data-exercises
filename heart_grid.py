grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def print_grid(grid):
    # Get the dimensions of the grid
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Iterate through columns first, then rows, to rotate the image
    for x in range(num_cols):
        for y in range(num_rows):
            print(grid[y][x], end='')
        print() # Move to the next line after printing all characters for a "column"

print_grid(grid)