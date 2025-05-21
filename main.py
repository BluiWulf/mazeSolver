from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.has_bottom_wall = False
    cell1.draw(10, 400, 10, 300)
    cell2 = Cell(win)
    cell2.draw(790, 400, 300, 10)
    cell3 = Cell(win)
    cell3.draw(400, 790, 590, 300)
    cell4 = Cell(win)
    cell4.has_top_wall = False
    cell4.draw(400, 10, 300, 590)
    cell1.draw_move(cell4)

    win.wait_for_close()

if __name__ == "__main__":
    main()