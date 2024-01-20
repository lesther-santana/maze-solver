import tkinter as tk
from tkinter import N, W, S, E, CENTER
from views import PlayView, CompareView

class MazeGame:
    def __init__(self, root: tk.Tk) -> None:
        self._root = root
        self._root.title("A Maze Game")

        # Main frame
        self._main_frame = tk.Frame(self._root)
        self._main_frame.pack(fill=tk.BOTH, expand=True)

        # Frames
        self._nav_frame = tk.Frame(self._main_frame, borderwidth=5, relief="ridge", padx=20, pady=10)
        self._content_frame = tk.Frame(self._main_frame, borderwidth=5, relief="ridge", padx=20, pady=10)
        self._play_view = PlayView(self._content_frame)  # Assuming this is defined elsewhere
        self._compare_view = CompareView(self._content_frame)

        # Setup
        self._setup_mainframe()
        
    def _setup_mainframe(self):
        self._setup_nav_bar()
        self._setup_content()

    def _setup_content(self):
        self._content_frame.pack(fill=tk.BOTH, expand=True, anchor="center")
        self._show_play()

    def _setup_nav_bar(self):
        # Buttons
        self._nav_frame.grid_anchor(CENTER)
        self._nav_frame.pack(fill=tk.X)

        button1 = tk.Button(self._nav_frame, text="Auto Solve", padx=10, command=self._show_play)
        button1.grid(row=0, column=0, padx=10)

        button2 = tk.Button(self._nav_frame, text="Play", padx=10, command=self._show_compare)
        button2.grid(row=0, column=1, padx=10)

        button3 = tk.Button(self._nav_frame, text="About", padx=10)
        button3.grid(row=0, column=2)


    def _show_play(self):

        for widget in self._content_frame.winfo_children():
            widget.destroy()
        # Create the play view if it does not exist
        if self._play_view is None:
            self._play_view = PlayView(root=self._content_frame)
        self._play_view.build()

    def _show_compare(self):
        # Clear the content frame
        for widget in self._content_frame.winfo_children():
            widget.destroy()
        # Create the play view if it does not exist
        if self._play_view is None:
            self._compare_view = CompareView(root=self._content_frame)
        self._compare_view.build()

    def _clear_content_frame(self):
        for widget in self._content_frame.winfo_children():
            widget.destroy()
        
    def start(self):
        self._root.mainloop()

