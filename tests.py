import unittest

from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def test_maze(self):
        num_cols = 12
        num_rows = 10
        margin = 50
        screen_x = 800
        screen_y = 600
        cell_size_x = (screen_x - 2 * margin) / num_cols
        cell_size_y = (screen_y - 2 * margin) / num_rows
        win = Window(screen_x, screen_y)
        m1 = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
        for i in range(num_rows):
            for j in range(num_rows):
                self.assertEqual(
                    m1._Maze__cells[0][0].visited,
                    False,
                )

if __name__ == "__main__":
    unittest.main()