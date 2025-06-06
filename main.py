import sys

from graphics import Window
from cell import Cell
from maze import Maze

def main():
    sys.setrecursionlimit(10000)
    num_cols = 12
    num_rows = 10
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    m1 = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    solved = m1.solve()

    if solved:
        print("Maze solved")
    else:
        print("Failed maze")

    win.wait_for_close()

if __name__ == "__main__":
    main()