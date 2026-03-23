# Rover Pathfinding

A Python project that simulates autonomous rover navigation on a 2D grid.  
The rover must move from a start position to an end position while avoiding obstacles and, depending on the algorithm, minimizing either the number of steps or the total traversal cost.

This project was built to practice grid-based pathfinding, algorithm design, and software structuring, with inspiration from autonomous navigation problems in space exploration.

## Features

- Random grid generation
- Start and end position detection
- Obstacles that cannot be crossed
- Multiple traversable terrain types with different costs
- Breadth-First Search (BFS)
- Dijkstra's algorithm
- Console visualization of the generated path

## Grid Representation

Each cell in the grid has a specific meaning:

- `START` → starting position of the rover
- `END` → destination
- `FREE` → normal terrain
- `SAND` → traversable terrain with higher cost
- `ROCK` → traversable terrain with even higher cost
- `OBSTACLE` → blocked cell, cannot be traversed

### Terrain Symbols

The grid is printed in the console using these symbols:

- `S` → Start
- `E` → End
- `-` → Free cell
- `~` → Sand
- `^` → Rock
- `#` → Obstacle
- `*` → Path found

## Terrain Costs

The traversal cost used in the project is:

- Start: `0`
- End: `0`
- Free: `1`
- Sand: `3`
- Rock: `5`

Obstacles are not traversable, so they are excluded from valid movements.

## Implemented Algorithms

### BFS

Breadth-First Search explores the grid level by level.  
It guarantees the path with the minimum number of steps when all moves are treated equally.

In this project, BFS:

- finds a valid path from start to end
- minimizes the number of moves
- does **not** optimize terrain cost
- still reports the total cost of the final path

### Dijkstra

Dijkstra’s algorithm explores cells according to the minimum accumulated cost.

In this project, Dijkstra:

- finds a valid path from start to end
- minimizes total traversal cost
- takes terrain types into account
- may choose a longer route in number of steps if it is cheaper overall

## Project Structure

```text
rover-pathfinding/
│
├── main.py
├── grid.py
├── search.py
└── README.md
```

## File Responsibilities

- **`main.py`**  
  Coordinates the execution of the program.

- **`grid.py`**  
  Handles grid generation, terrain definitions, valid movements, start/end discovery, path printing, and terrain costs.

- **`search.py`**  
  Contains the pathfinding algorithms (`bfs` and `dijkstra`).

## How It Works

1. A random grid is generated.
2. The program finds the start and end positions.
3. A search algorithm is executed.
4. The resulting path is reconstructed.
5. The final grid is printed with the path marked.
6. The program displays metrics such as:
   - number of explored nodes
   - total path cost

## Example Output

A possible output may look like this:

```text
- - - S * * * ~ ~ -
~ # - ^ ~ ~ * # - -
- - ^ ^ ^ ~ * ~ - -
- # # - ~ ~ * ^ ^ -
- - - - - ^ * * * E
```

## Learning Goals

This project was designed to practice:

- graph traversal on a grid
- BFS and Dijkstra
- path reconstruction using parent dictionaries
- priority queues with `heapq`
- clean separation between map logic and search logic
- comparing shortest path vs lowest-cost path

## Possible Improvements

Future extensions could include:

- A* search
- loading maps from files
- deterministic test maps instead of random generation
- graphical visualization
- statistics and comparison tables between algorithms
- additional terrain types
- energy constraints for the rover

## How to Run

Run the main file with Python:

```bash
python3 main.py
```

## Notes

This project uses a grid abstraction inspired by rover navigation problems.  
Although simplified, it reflects an important idea from autonomous systems: the shortest route is not always the best one if different terrains imply different traversal costs.