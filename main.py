from graphics import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(810, 610)
    Maze(5, 5, 30, 20, 40, 20, win)

    win.wait_for_close()

if __name__ == "__main__":
    main()