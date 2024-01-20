from tkinter import Canvas
from grid import Cell
import time
import random

class Maze:
    def __init__(
            self,
            margin,
            x1=0,
            y1=0,
            num_rows=10,
            num_cols=10,
            canvas=None,
            seed=None,
            mode=None
        ):

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = margin
        self._cell_size_y = margin
        self._canvas: Canvas = canvas
        self._cells = None
        self.maze_done = False
        self._current_cell_indx = [0,0]
        self._dot_id = None
        self._mode = mode

        if seed:
            random.seed(seed)


    def create_maze(self):
        print("Creating Maze")
        if self._canvas:
            self._x1 += 10
            self._y1 += 10 
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        #self._draw_maze()
        if self._mode == "play":
            self._draw_dot(self._cells[0][0])
        print("Maze Created")

    def _draw_maze(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i,j)
                #self._animate() 
    
    def _create_cells(self):
        cells = []
        for i in range(self._num_rows):
            col = []
            for j in range(self._num_cols):
                cell = Cell(self._canvas)
                col.append(cell)
            cells.append(col)
        self._cells = cells

        for i in range(self._num_rows):
            for j in range(self._num_cols):
                if self._canvas:
                    self._draw_cell(i, j)
                    self._animate()

    def _draw_cell(self, i, j):
        x1 = self._x1 + self._cell_size_x * j
        y1 = self._y1 + self._cell_size_y * i
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        cell = self._cells[i][j]
        cell.draw(x1, y1, x2, y2)
         
    def _animate(self):
        self._canvas.update_idletasks()
        self._canvas.update()
        time.sleep(0.02)


    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        self._draw_cell(0,0)
        exit_cell = self._cells[self._num_rows-1][self._num_cols-1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(self._num_rows-1, self._num_cols-1)


    def _break_walls_r(self, start_i, start_j):
        stack = [(start_i, start_j)]

        while stack:
            i, j = stack[-1]
            current_cell = self._cells[i][j]
            current_cell.visited = True
            next_moves = self.get_moves(i, j)
            if len(next_moves) == 0:
                stack.pop()
                self._draw_cell(i, j)
                continue
            next_index = random.choice(next_moves)
            stack.append(next_index)
            next_cell = self._cells[next_index[0]][next_index[1]]
            if next_index[0] > i:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif next_index[0] < i:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif next_index[1] > j:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            elif next_index[1] < j:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            
            
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def remake_maze(self):
        self._create_cells()

    def _solve_r(self, i, j) -> bool:
        # Call the _animate method.
        self._animate()
        current = self._cells[i][j]
        current.visited = True
        # End of Maze
        if i == self._num_rows - 1 and j == self._num_cols -1 :
            return True
        next_moves = self.solver_directions(i, j)
        for r, c in next_moves:
            next_cell = self._cells[r][c]
            self._draw_move(current,next_cell)
            if self._solve_r(r,c):
                return True
            self._draw_move(current, next_cell, undo=True)
        return False

    def solve(self):
        return self._solve_r(0,0)

    def solver_directions(self, i, j):
        moves = []
        current_cell = self._cells[i][j]
        if i - 1 >= 0:
            next_cell = self._cells[i-1][j]
            if not next_cell.visited and not current_cell.has_top_wall and not next_cell.has_bottom_wall:
                moves.append((i-1, j))
        if i + 1 < self._num_rows:
            next_cell = self._cells[i+1][j]
            if not next_cell.visited and not current_cell.has_bottom_wall and not next_cell.has_top_wall:
                moves.append((i+1, j))
        if j - 1 >= 0:
            next_cell = self._cells[i][j-1]
            if not next_cell.visited and not current_cell.has_left_wall and not next_cell.has_right_wall:
                moves.append((i, j-1))
        if j + 1 < self._num_cols:
            next_cell = self._cells[i][j+1]
            if not next_cell.visited and not current_cell.has_right_wall and not next_cell.has_left_wall:
                moves.append((i, j+1))
        return moves
        
    def get_moves(self, i, j):
        moves = []
        if i + 1 < self._num_rows and not self._cells[i + 1][j].visited:
            moves.append([i + 1, j])
        if i - 1 >= 0 and not self._cells[i - 1][j].visited:
            moves.append([i-1, j])
        if j + 1 < self._num_cols and not self._cells[i][j + 1].visited:
            moves.append([i, j + 1])
        if j - 1 >= 0 and not self._cells[i][j-1].visited:
            moves.append([i, j - 1])
        return moves
    
    def _draw_move(self, from_cell, to_cell, undo=False):
        if undo:
            color = "white"
        else:
            color = "red"
        p1 = from_cell.get_center()
        p2 = to_cell.get_center()
        x1 = p1.x
        y1 = p1.y
        x2 = p2.x
        y2 = p2.y
        self._canvas.create_line(x1, y1, x2, y2, fill=color, width=2)
        self._canvas.pack(fill="both", expand=1)

    def _draw_dot(self, cell, size=5):
        if self._dot_id is not None:
            self._canvas.delete(self._dot_id)
        center = cell.get_center()
        x = center.x
        y = center.y
        self._dot_id =  self._canvas.create_oval(x - size, y - size, x + size, y + size, fill='black')
        self._canvas.pack(fill="both", expand=1)
    
    def _find_closest_cell(self, x, y):
        closest_cell = None
        closest_dist = float("Inf")
        closest_i = None
        closest_j = None
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                cell = self._cells[i][j]
                dist = cell.calculate_distance(x, y)
                if dist < closest_dist:
                    closest_cell = cell
                    closest_dist = dist
                    closest_i = i
                    closest_j = j
        return closest_cell, closest_i, closest_j
    
    def _get_adjacent_cells(self, i, j):
        moves = []
        current_cell = self._cells[i][j]
        if i + 1 < self._num_rows:
            next_cell = self._cells[i+1][j]
            if not current_cell.has_bottom_wall and not next_cell.has_top_wall:
                moves.append([i + 1, j])
        if i - 1 >= 0:
            next_cell = self._cells[i - 1][j]
            if not current_cell.has_top_wall and not next_cell.has_bottom_wall:
                moves.append([i-1, j])
        if j + 1 < self._num_cols:
            next_cell = self._cells[i][j + 1]
            if not current_cell.has_right_wall and not next_cell.has_left_wall:
                moves.append([i, j + 1])
        if j - 1 >= 0:
            next_cell = self._cells[i][j - 1]
            if not current_cell.has_left_wall and not next_cell.has_right_wall:
                moves.append([i, j - 1])
        return moves

    def valid_point(self, x, y):
        top_left_cell = self._cells[0][0]
        top_right_cell = self._cells[0][-1]
        bottom_left_cell = self._cells[-1][0]

        if x > top_right_cell._tr.x or x < top_left_cell._tl.x:
            return False
        if y < top_right_cell._tr.y or y > bottom_left_cell._bl.y:
            return False
        return True

    def get_current_cell(self):
        i, j = self._current_cell_indx
        return self._cells[i][j]

    def cell_clicked(self, x, y):
        new_x = x
        new_y = y
        print("clicked: ", new_x, new_y)
        if not self.valid_point(new_x, new_y):
            print("Invalid Point")
            return
        closest_cell, i, j = self._find_closest_cell(new_x, new_y)
        print("Closest Cell", i, j)
        if closest_cell is None:
            return 
        valid_moves = self._get_adjacent_cells(*self._current_cell_indx)
        print("Possible Moves", valid_moves)
        for move in valid_moves:
            if i == move[0] and j == move[1]:
                print(f"Moving to", i, j)
                current = self.get_current_cell()
                to_cell = self._cells[i][j]
                if to_cell.visited:
                    self._draw_move(current, to_cell, undo=True)
                    current.visited = False
                else:    
                    self._draw_move(current, to_cell)
                    current.visited = True
                self._draw_dot(to_cell)
                self._current_cell_indx = [i, j]
                if i == self._num_rows - 1 and j == self._num_cols - 1:
                    self.maze_done = True
        print(f"Invalid move from:", self._current_cell_indx, "To :", i, j)
        return