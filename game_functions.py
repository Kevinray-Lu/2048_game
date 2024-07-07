import random

def initialize_grid():
    return [[0]*4 for _ in range(4)]

def add_random_two(grid):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2

def compress(grid):
    new_grid = [[0]*4 for _ in range(4)]
    moved = False
    for i in range(4):
        pos = 0
        for j in range(4):
            if grid[i][j] != 0:
                new_grid[i][pos] = grid[i][j]
                if j != pos:
                    moved = True
                pos += 1
    return new_grid, moved

def merge(grid):
    moved = False
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i][j+1] = 0
                moved = True
    return grid, moved

def reverse(grid):
    new_grid = []
    for i in range(4):
        new_grid.append(list(reversed(grid[i])))
    return new_grid

def transpose(grid):
    new_grid = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_grid[i][j] = grid[j][i]
    return new_grid

def move(grid, direction):
    moved = False
    if direction == 'w':
        grid = transpose(grid)
        grid, moved1 = compress(grid)
        grid, moved2 = merge(grid)
        moved = moved1 or moved2
        grid, _ = compress(grid)
        grid = transpose(grid)
    elif direction == 's':
        grid = transpose(grid)
        grid = reverse(grid)
        grid, moved1 = compress(grid)
        grid, moved2 = merge(grid)
        moved = moved1 or moved2
        grid, _ = compress(grid)
        grid = reverse(grid)
        grid = transpose(grid)
    elif direction == 'a':
        grid, moved1 = compress(grid)
        grid, moved2 = merge(grid)
        moved = moved1 or moved2
        grid, _ = compress(grid)
    elif direction == 'd':
        grid = reverse(grid)
        grid, moved1 = compress(grid)
        grid, moved2 = merge(grid)
        moved = moved1 or moved2
        grid, _ = compress(grid)
        grid = reverse(grid)
    return grid, moved

def can_move(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return True
            if j < 3 and grid[i][j] == grid[i][j+1]:
                return True
            if i < 3 and grid[i][j] == grid[i+1][j]:
                return True
    return False

def print_grid(grid):
    for row in grid:
        print("\t".join(str(cell) if cell != 0 else "." for cell in row))
