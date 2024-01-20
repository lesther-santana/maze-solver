import unittest
from maze import Maze
from tkinter import Tk, Canvas

class TestMaze(unittest.TestCase):
    def setUp(self):
        # Set up a Tkinter root and Canvas for the tests
        self.root = Tk()
        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack()

    def tearDown(self):
        # Clean up after tests
        self.root.destroy()

    def test_maze_creation(self):
        maze = Maze(margin=50, canvas=self.canvas, num_rows=10, num_cols=10)
        maze.create_maze()
        self.assertEqual(len(maze._cells), 10)  # Check rows
        self.assertEqual(len(maze._cells[0]), 10)  # Check columns

    def test_entrance_and_exit(self):
        maze = Maze(margin=50, canvas=self.canvas, num_rows=10, num_cols=10)
        maze.create_maze()
        # Entrance should have no top wall
        self.assertFalse(maze._cells[0][0].has_top_wall)
        # Exit should have no bottom wall
        self.assertFalse(maze._cells[-1][-1].has_bottom_wall)

    def test_solve_function(self):
        maze = Maze(margin=50, canvas=self.canvas, num_rows=10, num_cols=10)
        maze.create_maze()
        solved = maze.solve()
        self.assertTrue(solved)

if __name__ == "__main__":
    unittest.main()