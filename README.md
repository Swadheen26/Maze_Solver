# Maze Solver

This Python project generates a maze and provides a simple console-based interface for user interaction with the generated maze. The project includes features such as maze generation, maze display, pathfinding using Breadth-First Search (BFS), and user interaction through a menu-driven interface.

## Features

1. **Maze Generation**
   - The `mazeCreate` function generates an n x n maze, where n is provided by the user.
   - The start and end points are marked with "S" (green) and "E" (green), respectively.
   - Random walls are placed in the maze, represented by a full block (red).

2. **Maze Display**
   - The `printMaze` function is responsible for displaying the maze. It uses `colorama` for console text coloring.
   - Walls are displayed in red, open spaces in blue, the start and end points in green, and the path in green.

3. **Path Finding Algorithm**
   - The maze solving is implemented using a Breadth-First Search (BFS) algorithm.
   - The `path_finding` function finds the shortest path from the start to the end using BFS and marks the path with circles (green).
   - If a path is found, the maze with the marked path is displayed. Otherwise, a message is printed stating that no path exists.

4. **User Interaction**
   - The user is prompted to input the size of the maze initially and is presented with a menu for subsequent actions.
   - The user can choose to print the path, generate a new maze, or exit the program.
   - The program runs in a loop until the user chooses to exit.

5. **Error Handling**
   - The code includes basic error handling to ensure that the user enters valid choices.

6. **Code Organization**
   - The code is organized into functions for better readability and modularity.
   - The use of `colorama` makes the console output visually appealing.

7. **Reusability**
   - The code allows the user to generate a new maze, providing flexibility for different scenarios.

8. **Randomization**
   - The placement of random walls adds variety to each generated maze.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Swadheen26/Maze_Solver.git
   cd Maze_Solver

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    
Usage
```bash
python maze_solver.py
