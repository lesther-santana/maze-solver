import tkinter as tk
from tkinter import messagebox
from maze import Maze
from time import time


class PlayView:    
    def __init__(self, root) -> None:
        self._root = root
        self.canvas = None
        self._maze = None
        self._maze_solved = False
        self._nav_frame = None
        self._footer = None

    def build(self):
        self._nav_frame = tk.Frame(self._root,pady=30)
        self._nav_frame.grid_anchor("center")
        self._nav_frame.pack(fill=tk.X)

        
        tk.Label(self._nav_frame, text="Auto Solve Mode:").grid(row=0, column=0, pady=20)

        solve_btn = tk.Button(self._nav_frame, text="Solve Maze", padx=10, command=self.solve_maze)
        solve_btn.grid(row=0, column=1, padx=10)

        reset_btn = tk.Button(self._nav_frame, text="Reset Maze", padx=10, command=self.reset_maze)
        reset_btn.grid(row=0, column=2, padx=10)

        self._footer = tk.Frame(self._root)
        self._footer.grid_anchor("center")
        self._footer.pack(fill=tk.X)
        
        self._setup_maze()

    def _setup_maze(self):
        self.canvas = tk.Canvas(self._root)
        self._maze = Maze(margin=50, canvas=self.canvas)
        self._maze.create_maze()
        self._maze_solved = False
        self.canvas.pack(expand=True, fill="both")

    def _clear_footer(self):
        if self._footer:
            for widget in self._footer.winfo_children():
                widget.destroy()

    def solve_maze(self):
        self._clear_footer()
        if self._maze_solved:
            self.reset_maze()
            self.solve_maze()
            return
        start = time()
        self._maze_solved = self._maze.solve() 
        end = time()
        solve_time = round(end-start,2)
        tk.Label(self._footer, text="Maze done, reset or switch views!").pack(pady=20)
        message = f"Maze Solved in {solve_time} seconds"
        messagebox.showinfo(message=message)
        

    def reset_maze(self):
        print("Resetting Maze")
        self._clear_footer()
        self.canvas.destroy()
        self._setup_maze()


class CompareView:
    def __init__(self, root) -> None:
        self._root = root
        self.canvas = None
        self._maze = None
        self._maze_solved = False
        self._nav_frame = None
        self._footer = None

    def build(self):
        self._nav_frame = tk.Frame(self._root,pady=30)
        self._nav_frame.grid_anchor("center")
        self._nav_frame.pack(fill=tk.X)

        tk.Label(self._nav_frame, text="Play Mode:").grid(row=0, column=0, pady=20)

        reset_btn = tk.Button(self._nav_frame, text="Reset Maze", padx=10, command=self.reset_maze)
        reset_btn.grid(row=0, column=1, padx=10)

        self._footer = tk.Frame(self._root)
        self._footer.grid_anchor("center")
        self._footer.pack(fill=tk.X)

        self._setup_maze()

        tk.Label(self._footer, text="Click on a cell to move the dot and reach the end!").pack(pady=20)

    def _setup_maze(self):
        self.canvas = tk.Canvas(self._root)
        self._maze = Maze(margin=50, canvas=self.canvas, mode="play")
        self._maze.create_maze()
        self._maze_solved = False
        self.canvas.bind("<Button-1>", self._cell_clicked)
        self.canvas.pack(expand=True, fill="both")

    def reset_maze(self):
        self._clear_footer()
        print("Resetting Maze")
        self.canvas.destroy()
        self._setup_maze()

    def _cell_clicked(self, event):
        self._maze.cell_clicked(event.x, event.y)
        if self._maze.maze_done:
            self._clear_footer()
            tk.Label(self._footer, text="Maze done! Reset or switch views!").pack(pady=20)
            message = f"Congrats! Maze Solved!"
            messagebox.showinfo(message=message)
            self.canvas.unbind("<Button-1>")

    def _clear_footer(self):
        if self._footer:
            for widget in self._footer.winfo_children():
                widget.destroy()