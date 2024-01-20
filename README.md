# Maze Game

## Overview
This repository contains a Tkinter-based Maze Game, where users can interact with and solve mazes. The game includes features for creating mazes, solving them, and seeing the paths taken by the DFS algorithm to solve the maze. It is uses the Tkinter library for the graphical user interface.


## Features

- Interactive maze creation and solving.

- Play mode, a game where the user chooses directions to navigate through the maze.

- Auto Solve, mode to measure the time it takes to solve the randomly created Maze a using Depth-First search (DFS) strategy.

- Unit tests for validating the maze generation and solving logic

## Structure
The codebase is organized into several Python files:

- `main.py`: The entry point of the application. It initializes the Tkinter root and starts the game.
- `game.py`: Defines the `MazeGame` class, which sets up the main application window and manages different views.
- `grid.py`: Contains classes `Point` and `Cell`, used for representing points and cells in the maze.
- `maze.py`: Implements the `Maze` class, responsible for creating and managing the maze structure.
- `views.py`: Contains the `PlayView` and `CompareView` classes, which are responsible for the different views or modes in the game.
- `tests.py`: Includes unit tests for testing the functionality of the `Maze` class.

## Dependencies

- Python (3.x recommended)
- Tkinter (usually comes pre-installed with Python)

## Running the Application
To run the Maze Game, execute the `main.py` script using Python. Ensure that Python and Tkinter are installed on your system.

## To-Do's

- Add other solving algorithms, like breadth-first search or A*
- Add configurations in the app itself using Tkinter buttons and inputs to allow users to change maze size, speed, etc
- Make the visuals prettier, change the colors, etc
```bash
python main.py
```

## Screenshots

### Play Mode

![Play Mode Screenshot](/docs/play_mode.png)

### Auto Solve Mode
![Auto Mode Screenshot](/docs/auto_solve.png)
