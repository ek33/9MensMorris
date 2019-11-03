from src.game import Cell
from src.game import Mill
from kivy.app import App

class Board:
    cells = []
    selected = False

    def __init__(self, root):
        self.mills = [
            Mill('a1', 'a4', 'a7'),
            Mill('b2', 'b4', 'b6'),
            Mill('c3', 'c4', 'c5'),
            Mill('d1', 'd2', 'd3'),
            Mill('d5', 'd6', 'd7'),
            Mill('e3', 'e4', 'e5'),
            Mill('f2', 'f4', 'f6'),
            Mill('g1', 'g4', 'g7'),
            Mill('a1', 'd1', 'g1'),
            Mill('b2', 'd2', 'f2'),
            Mill('c3', 'd3', 'e3'),
            Mill('a4', 'b4', 'c4'),
            Mill('e4', 'f4', 'g4'),
            Mill('c5', 'd5', 'e5'),
            Mill('b6', 'd6', 'f6'),
            Mill('a7', 'd7', 'g7')
        ]
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
            if cell.close(point.get('x'), point.get('y')) and cell.empty:
                print('{} : {}'.format(cell.id, cell.empty))
                cell.setPiece(piece)
                placed = True

        return placed
     
    def select(self, touch):
        point = {
            'x': touch.x - 25,
            'y': touch.y - 25
        }

        for cell in self.cells:
            if cell.close(point.get('x'), point.get('y')) and not cell.empty:
                print('{} : {}'.format(cell.id, cell.empty))
                self.selected = cell
                return True

        self.selected = False
        return self.selected

    def move(self, touch):
        if self.selected:
            placed = self.place(self.selected.piece, touch)
            self.selected.removePiece()
            self.selected = False
            return placed
        else:
            return False