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
    
def build_manual_grid(case_name: str) -> list[list[int]]:
    if case_name == "simple":
        return [
            [FREE, FREE, START, FREE, FREE],
            [FREE, FREE, FREE, FREE, FREE],
            [FREE, FREE, FREE, FREE, FREE],
            [FREE, FREE, FREE, FREE, FREE],
            [FREE, FREE, END, FREE, FREE],
        ]

    elif case_name == "detour":
        return [
            [FREE, FREE, START, FREE, FREE],
            [FREE, OBSTACLE, OBSTACLE, OBSTACLE, FREE],
            [FREE, FREE, FREE, OBSTACLE, FREE],
            [FREE, OBSTACLE, FREE, FREE, FREE],
            [FREE, FREE, END, OBSTACLE, FREE],
        ]

    elif case_name == "no_path":
        return [
            [FREE, FREE, START, FREE, FREE],
            [OBSTACLE, OBSTACLE, OBSTACLE, OBSTACLE, OBSTACLE],
            [FREE, FREE, FREE, FREE, FREE],
            [FREE, OBSTACLE, FREE, OBSTACLE, FREE],
            [FREE, FREE, END, FREE, FREE],
        ]

    elif case_name == "weighted":
        return [
            [FREE, FREE, FREE, START, FREE, FREE, FREE],
            [OBSTACLE, OBSTACLE, FREE, SAND, FREE, OBSTACLE, OBSTACLE],
            [FREE, FREE, FREE, SAND, FREE, FREE, FREE],
            [FREE, OBSTACLE, OBSTACLE, SAND, OBSTACLE, OBSTACLE, FREE],
            [FREE, OBSTACLE, OBSTACLE, SAND, OBSTACLE, OBSTACLE, FREE],
            [FREE, FREE, FREE, SAND, FREE, FREE, FREE],
            [FREE, FREE, FREE, END, FREE, FREE, FREE],
        ]
    
    elif case_name == "huge":
        rows = 60
        cols = 60
        grid = [[FREE for _ in range(cols)] for _ in range(rows)]

        # Start and end
        grid[0][5] = START
        grid[rows - 1][cols - 6] = END

        # Vertical sand corridor near the center
        for i in range(1, rows - 1):
            grid[i][cols // 2] = SAND

        # Horizontal rock bands with small gaps
        for r in range(8, rows - 8, 8):
            for c in range(cols):
                grid[r][c] = ROCK
            gap = (r * 7) % (cols - 10) + 5
            for k in range(gap, min(gap + 4, cols)):
                grid[r][k] = FREE

        # Obstacle blocks to force detours
        for r in range(10, rows - 10, 12):
            for c in range(10, cols - 10):
                if c % 9 not in (0, 1, 2):
                    grid[r][c] = OBSTACLE

        # Keep a left corridor mostly cheap
        for r in range(rows):
            for c in range(0, 4):
                if grid[r][c] != START and grid[r][c] != END:
                    grid[r][c] = FREE

        # Keep a bottom corridor mostly cheap
        for c in range(cols):
            if grid[rows - 2][c] != END:
                grid[rows - 2][c] = FREE

        # Make sure start/end surroundings are open
        for dr in range(0, 2):
            for dc in range(-1, 2):
                nr, nc = dr, 5 + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != START:
                    grid[nr][nc] = FREE

        for dr in range(-1, 1):
            for dc in range(-1, 2):
                nr, nc = rows - 1 + dr, cols - 6 + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != END:
                    grid[nr][nc] = FREE

        return grid

    else:
        raise ValueError(f"Unknown test case: {case_name}")

def get_manual_case_names() -> list[str]:
    return ["simple", "detour", "no_path", "weighted", 'huge']