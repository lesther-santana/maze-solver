from tkinter import Canvas
import math


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Cell:
    def __init__(self, win, **kwargs):
        self._win: Canvas = win
        self._tl = None
        self._tr = None
        self._bl = None
        self._br = None
        self.has_left_wall: bool = kwargs.get("has_left_wall", True)
        self.has_right_wall: bool = kwargs.get("has_right_wall", True)
        self.has_top_wall: bool = kwargs.get("has_top_wall", True)
        self.has_bottom_wall: bool = kwargs.get("has_bottom_wall", True)
        self.visited = False
        self._line_color = self._win.cget("bg")                                                                                                                  

    def draw(self, x1, y1, x2, y2):
        
        self._tl = Point(x1, y1)
        self._tr = Point(x2, y1)
        self._bl = Point(x1, y2)
        self._br = Point(x2, y2)
        
        
        if self.has_bottom_wall:
            self._draw_wall(self._bl, self._br, "black")
        else:
            self._draw_wall(self._bl, self._br, fill_color=self._line_color)
        if self.has_top_wall:
            self._draw_wall(self._tl, self._tr, "black")
        else:
            self._draw_wall(self._tl, self._tr, fill_color=self._line_color)
        if self.has_left_wall:
            self._draw_wall(self._tl, self._bl, "black")
        else:
            self._draw_wall(self._tl, self._bl, fill_color=self._line_color)
        if self.has_right_wall:
            self._draw_wall(self._tr, self._br, "black")
        else:
            self._draw_wall(self._tr, self._br, fill_color=self._line_color)

    def _draw_wall(self, p1, p2, fill_color="white", width=1):
        x1 = p1.x
        y1 = p1.y
        x2 = p2.x
        y2 = p2.y
        self._win.create_line(x1, y1, x2, y2, fill=fill_color, width=width)
        self._win.pack(fill="both", expand=1)

    def get_center(self) -> (int, int):
        center_x = (self._tl.x + self._tr.x + self._bl.x + self._br.x) / 4
        center_y = (self._tl.y + self._tr.y + self._bl.y + self._br.y) / 4
        return Point(center_x, center_y)
    
    def calculate_distance(self, x1, y1):
        """
        Calculate the distance between the cell's center and the provided coordinates.
        """
        center = self.get_center()
        x0 = center.x
        y0 = center.y
        return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)