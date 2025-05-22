from graphics import Point, Line

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, x2, y1, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            pt1 = Point(min(self.__x1, self.__x2), min(self.__y1, self.__y2))
            pt2 = Point(min(self.__x1, self.__x2), max(self.__y1, self.__y2))
            wall = Line(pt1, pt2)            
            self.__win.draw_line(wall, "black")

        if self.has_right_wall:
            pt1 = Point(max(self.__x1, self.__x2), min(self.__y1, self.__y2))
            pt2 = Point(max(self.__x1, self.__x2), max(self.__y1, self.__y2))
            wall = Line(pt1, pt2)            
            self.__win.draw_line(wall, "black")

        if self.has_top_wall:
            pt1 = Point(min(self.__x1, self.__x2), min(self.__y1, self.__y2))
            pt2 = Point(max(self.__x1, self.__x2), min(self.__y1, self.__y2))
            wall = Line(pt1, pt2)            
            self.__win.draw_line(wall, "black")

        if self.has_bottom_wall:
            pt1 = Point(min(self.__x1, self.__x2), max(self.__y1, self.__y2))
            pt2 = Point(max(self.__x1, self.__x2), max(self.__y1, self.__y2))
            wall = Line(pt1, pt2)            
            self.__win.draw_line(wall, "black")

    def draw_move(self, to_cell, undo = False):
        x_from = (self.__x1 + self.__x2) / 2
        y_from = (self.__y1 + self.__y2) / 2
        x_to = (to_cell.__x1 + to_cell.__x2) / 2
        y_to = (to_cell.__y1 + to_cell.__y2) / 2
        print(f"x1: {x_from} y1: {y_from} x2: {x_to} y2: {y_to}")
        move = Line(Point(x_from, y_from), Point(x_to, y_to))
        color = "gray" if undo else "red"
        self.__win.draw_line(move, color)

