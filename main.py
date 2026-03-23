from grid import build_manual_grid, get_manual_case_names
from search import bfs, dijkstra, print_path, find_start, find_end

def run_algorithm(name: str, algorithm, grid: list[list[int]]):
    start = find_start(grid)
    end = find_end(grid)

    result = algorithm(grid, start, end)

    print(f"\n{name}")
    print("-" * len(name))

    if result is None:
        print("No path found.")
        return None

    path, explored, cost = result
    print_path(grid, path)
    print(f"Explored nodes: {explored}")
    print(f"Total cost: {cost}")
    print(f"Path length: {len(path)}")

    return result

def compare_algorithms(case_name: str):
    grid = build_manual_grid(case_name)

    print("\n" + "=" * 50)
    print(f"TEST CASE: {case_name.upper()}")
    print("=" * 50)

    print("\nOriginal grid")
    print("-------------")
    print_path(grid, [])

    bfs_result = run_algorithm("BFS", bfs, grid)
    dijkstra_result = run_algorithm("Dijkstra", dijkstra, grid)

    if bfs_result is not None and dijkstra_result is not None:
        _, bfs_explored, bfs_cost = bfs_result
        _, dijkstra_explored, dijkstra_cost = dijkstra_result

        print("\nComparison")
        print("----------")
        print(f"BFS      -> explored: {bfs_explored}, cost: {bfs_cost}")
        print(f"Dijkstra -> explored: {dijkstra_explored}, cost: {dijkstra_cost}")

def main():
    for case_name in get_manual_case_names():
        compare_algorithms(case_name)

if __name__ == "__main__":
    main()