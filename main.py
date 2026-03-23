from grid import *
from search import *

def main():
    grid = build_grid(20, 20, 100)
    start = find_start(grid)
    end = find_end(grid)

    path_bfs, explored, length = bfs(grid, start, end)
    if not path_bfs:
        return "Error al encontrar el camino"
    
    print_path(grid, path_bfs)
    print(f"El costo del camino encontrado es {length}\nLa cantidad de nodos visitados es {explored}")

    path_dijkstra, explored_d, cost = dijkstra(grid, start, end)
    if not path_dijkstra:
        return "Error al encontrar camino con dijkstra"
    print_path(grid, path_dijkstra)
    print(f"El costo del camino encontrado es {cost}\nLa cantidad de nodos visitados es {explored_d}")

if __name__ == "__main__":
    main()