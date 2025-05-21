from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg = "white", height = height, width = width)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.__running = True

        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        # x = 0 is the left of the screen
        # y = 0 is the top of the screen
        self.x = x
        self.y = y

class Line:
    def __init__(self, pt_A, pt_B):
        self.pt_A = pt_A
        self.pt_B = pt_B

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.pt_A.x, self.pt_A.y, self.pt_B.x, self.pt_B.y, fill = fill_color, width = 2
        )

