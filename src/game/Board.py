from src.game import Cell
from kivy.app import App

class Board:
    cells = []

    def __init__(self, root):

        self.cells = [
            Cell(root.center_x - 325, root.center_y + 275, 'a1', True),
            Cell(root.center_x - 21, root.center_y + 275, 'a4', True),
            Cell(root.center_x + 275, root.center_y + 275, 'a7', True),
            Cell(root.center_x - 225, root.center_y + 175, 'b2', True),
            Cell(root.center_x - 21, root.center_y + 175, 'b4', True),
            Cell(root.center_x + 175, root.center_y + 175, 'b6', True),
            Cell(root.center_x - 125, root.center_y + 75, 'c3', True),
            Cell(root.center_x - 21, root.center_y + 75, 'c4', True),
            Cell(root.center_x + 75, root.center_y + 75, 'c5', True),
            Cell(root.center_x - 325, root.center_y - 20, 'd1', True),
            Cell(root.center_x - 225, root.center_y - 20, 'd2', True),
            Cell(root.center_x - 125, root.center_y - 20, 'd3', True),
            Cell(root.center_x + 75, root.center_y - 20, 'd5', True),
            Cell(root.center_x + 175, root.center_y - 20, 'd6', True),
            Cell(root.center_x + 275, root.center_y - 20, 'd7', True),
            Cell(root.center_x - 325, root.center_y - 323, 'g1', True),
            Cell(root.center_x - 21, root.center_y - 323, 'g4', True),
            Cell(root.center_x + 275, root.center_y - 323, 'g7', True),
            Cell(root.center_x - 225, root.center_y - 223, 'f2', True),
            Cell(root.center_x - 21, root.center_y - 223, 'f4', True),
            Cell(root.center_x + 175, root.center_y - 223, 'f6', True),
            Cell(root.center_x - 125, root.center_y - 123, 'e3', True),
            Cell(root.center_x - 21, root.center_y - 123, 'e4', True),
            Cell(root.center_x + 75, root.center_y - 123, 'e5', True)
        ]

    def place(self, piece, touch):
        point = {
            'x': touch.x - 25,
            'y': touch.y - 25
        }
        placed = False

        for cell in self.cells:
            if cell.close(point):
                piece.pos = point.get('x'), point.get('y')
                placed = True

        return placed




