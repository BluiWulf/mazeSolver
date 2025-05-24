import time
import random

from cell import Cell

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None
        ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []

        if seed:
            random.seed(seed)

        self.__create_cells()
        time.sleep(10)

        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self):
        for i in range(self.__num_cols):
            new_cells = []
            for j in range(self.__num_rows):
                new_cells.append(Cell(self.__win))
            self.__cells.append(new_cells)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        if self.__win is None:
            return
        
        cell_x1 = self.__x1 + (i * self.__cell_size_x)
        cell_x2 = cell_x1 + self.__cell_size_x
        cell_y1 = self.__y1 + (j * self.__cell_size_y)
        cell_y2 = cell_y1 + self.__cell_size_y

        self.__cells[i][j].draw(cell_x1, cell_x2, cell_y1, cell_y2)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            next_visits = []
            if 0 <= i < self.__num_cols - 1:
                if self.__cells[i + 1][j].visited == False:
                    next_visits.append((i + 1, j))
            if 0 < i <= self.__num_cols - 1:
                if self.__cells[i - 1][j].visited == False:
                    next_visits.append((i - 1, j))

            if 0 <= j < self.__num_rows - 1:
                if self.__cells[i][j + 1].visited == False:
                    next_visits.append((i, j + 1))
            if 0 < j <= self.__num_rows - 1:
                if self.__cells[i][j - 1].visited == False:
                    next_visits.append((i, j - 1))

            if len(next_visits) == 0:
                self.__draw_cell(i, j)
                return
            
            direction_index = random.randrange(len(next_visits))
            direction = next_visits[direction_index]
            if direction[0] < i:
                self.__cells[i][j].has_left_wall = False
                self.__cells[direction[0]][direction[1]].has_right_wall = False
            if direction[0] > i:
                self.__cells[i][j].has_right_wall = False
                self.__cells[direction[0]][direction[1]].has_left_wall = False
            if direction[1] < j:
                self.__cells[i][j].has_top_wall = False
                self.__cells[direction[0]][direction[1]].has_bottom_wall = False
            if direction[1] > j:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[direction[0]][direction[1]].has_top_wall = False
            self.__break_walls_r(direction[0], direction[1])

    def __reset_cells_visited(self):        
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self.__animate()
        self.__cells[i][j].visited = True
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True
        
        if (0 <= i < self.__num_cols - 1 and
            self.__cells[i][j].has_right_wall == False and
            self.__cells[i + 1][j].visited == False):
                self.__cells[i][j].draw_move(self.__cells[i + 1][j])
                if self._solve_r(i + 1, j):
                    return True
                else:
                    self.__cells[i][j].draw_move(self.__cells[i + 1][j], True)

        if (0 < i <= self.__num_cols - 1 and
            self.__cells[i][j].has_left_wall == False and
            self.__cells[i - 1][j].visited == False):
                self.__cells[i][j].draw_move(self.__cells[i - 1][j])
                if self._solve_r(i - 1, j):
                    return True
                else:
                    self.__cells[i][j].draw_move(self.__cells[i - 1][j], True)

        if (0 <= j < self.__num_rows - 1 and
            self.__cells[i][j].has_bottom_wall == False and
            self.__cells[i][j + 1].visited == False):
                self.__cells[i][j].draw_move(self.__cells[i][j + 1])
                if self._solve_r(i, j + 1):
                    return True
                else:
                    self.__cells[i][j].draw_move(self.__cells[i][j + 1], True)

        if (0 < j <= self.__num_rows - 1 and
            self.__cells[i][j].has_top_wall == False and
            self.__cells[i][j - 1].visited == False):
                self.__cells[i][j].draw_move(self.__cells[i][j - 1])
                if self._solve_r(i, j - 1):
                    return True
                else:
                    self.__cells[i][j].draw_move(self.__cells[i][j - 1], True)
        
        return False
        
