from grid import *
import heapq
from queue import Queue

def bfs(grid: list[list[int]], start: tuple, end: tuple):
    
    visited = set()
    fathers = {}
    explored = 0

    search_queue = Queue()
    x = start
    search_queue.put(x)
    visited.add(x)
    explored += 1

    found = False
    while not search_queue.empty():
        x = search_queue.get()
        if x == end:
            found = True
            break
        else:
            neighbors = get_valid_movements(grid, x[0], x[1])
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    explored += 1
                    fathers[neighbor] = x
                    search_queue.put(neighbor)
    
    if not found:
        return None
    
    path = []
    current = end
    while current != start:
        path.append(current)
        current = fathers[current]
    path.append(start)

    path.reverse()
    cost = 0
    for celd in path:
        i, j = celd
        cost += get_value(grid, i, j)
    return path, explored, cost

def dijkstra(grid: list[list[int]], start: tuple, end: tuple):
    
    fathers = {}
    weights = {}
    explored = 0

    min_heap = []
    current = (0, start)
    weights[start] = 0
    heapq.heappush(min_heap, current)

    found = False
    while len(min_heap) != 0:
        curr_cost, curr_pos = heapq.heappop(min_heap)
        if curr_cost != weights[curr_pos]:
            continue
        explored += 1
        if curr_pos == end:
            found = True
            break
        else:
            neighbors = get_valid_movements(grid, curr_pos[0], curr_pos[1])
            for neighbor in neighbors:
                new_cost = weights[curr_pos] + get_value(grid, neighbor[0], neighbor[1])
                if neighbor not in weights:
                    weights[neighbor] = float('inf')
                if new_cost < weights[neighbor]:
                    weights[neighbor] = new_cost
                    fathers[neighbor] = curr_pos
                    heapq.heappush(min_heap, (new_cost, neighbor))
    
    if not found:
        return None
    
    path = []
    current = end
    while current != start:
        path.append(current)
        current = fathers[current]
    path.append(start)

    path.reverse()
    cost = weights[end]
    return path, explored, cost

def print_path(grid, path):
    n_rows = len(grid)
    n_columns = len(grid[0])
    for i in range(n_rows):
        converted_row = []
        for j in range(n_columns):
            if grid[i][j] == START:
                converted_row.append("S")
            elif grid[i][j] == END:
                converted_row.append("E")
            elif (i, j) in path:
                converted_row.append("*")
            elif grid[i][j] == FREE:
                converted_row.append("-")
            elif grid[i][j] == SAND:
                converted_row.append("~")
            elif grid[i][j] == ROCK:
                converted_row.append("^")
            elif grid[i][j] == OBSTACLE:
                converted_row.append("#")
        print(" ".join(converted_row))

def find_start(grid):
    n_columns = len(grid[0])
    for i in range(n_columns):
        if grid[0][i] == START:
            return (0, i)

def find_end(grid):
    n_rows = len(grid)
    n_columns = len(grid[0])
    for i in range(n_columns):
        if grid[n_rows - 1][i] == END:
            return (n_rows - 1, i)       
