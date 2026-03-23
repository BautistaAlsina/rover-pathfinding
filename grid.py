import random
FREE = 1
OBSTACLE = 2
SAND = 3
ROCK = 5
START = 0
END = 10


#Very important to check the number of obstacles before calling this function to avoid filling the grid of them.
def build_grid(rows: int, columns: int, obstacles: int) -> list[list[int]]:
    grid = [[random.choice([FREE, SAND, ROCK]) for i in range(columns)] for _ in range(rows)]
    
    for i in range(obstacles):
        find_free = False
        while not find_free:
            obstacle_r = random.randint(1, rows - 2) #Avoid putting obstacles on the first and last row
            obstacle_c = random.randint(0, columns - 1)

            if grid[obstacle_r][obstacle_c] != OBSTACLE:
                grid[obstacle_r][obstacle_c] = OBSTACLE
                find_free = True
    
    start = random.randint(0, columns-1)
    grid[0][start] = START
    end = random.randint(0, columns-1)
    grid[rows - 1][end] = END 
    
    return grid

def print_grid(grid: list[list[int]]) -> None:
    rows = len(grid)
    columns = len(grid[0])
    
    for i in range(rows):
        converted_row = []
        for j in range(columns):
            if grid[i][j] == FREE:
                converted_row.append("-")
            elif grid[i][j] == SAND:
                converted_row.append("~")
            elif grid[i][j] == ROCK:
                converted_row.append("^")
            elif grid[i][j] == OBSTACLE:
                converted_row.append("#")
            elif grid[i][j] == START:
                converted_row.append("S")
            elif grid[i][j] == END:
                converted_row.append("E")
        print(" ".join(converted_row))
    return

grid = build_grid(10, 10, 5)
print_grid(grid)

def get_valid_movements(grid: list[list[int]], row: int, column: int) -> list[str]:
    n_rows = len(grid)
    n_columns = len(grid[0])

    posible_movements = []

    if (column + 1) < n_columns and grid[row][column + 1] != OBSTACLE:
        posible_movements.append((row, column + 1))
    if row + 1 < n_rows and grid[row + 1][column] != OBSTACLE:
        posible_movements.append((row + 1, column))
    if column - 1 >= 0 and grid[row][column - 1] != OBSTACLE:
        posible_movements.append((row, column - 1))
    if row - 1 >= 0 and grid[row - 1][column] != OBSTACLE:
        posible_movements.append((row - 1, column))

    return posible_movements

print(get_valid_movements(grid, 0, 4))

def get_value(grid, i, j):
    if grid[i][j] == START:
        return 0
    elif grid[i][j] == END:
        return 0
    elif grid[i][j] == FREE:
        return 1
    elif grid[i][j] == SAND:
        return 3
    elif grid[i][j] == ROCK:
        return 5