from src.game import Cell
from kivy.app import App

class Board:
    cells = []
    selected = False
    prevWhiteMills = 0
    prevBlackMills = 0
    currentWhiteMills = 0
    currentBlackMills = 0

    def __init__(self, root):
        self.mills = []
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

    def getCellsFromMill(self, mill):
        cells = []

        for cell in self.cells:
            if mill.check(cell.id):
                cells.append(cell)

        return cells

    def whiteMills(self):
        count = 0

        for mill in self.mills:
            cells = self.getCellsFromMill(mill)
            whiteCells = 0
            for cell in cells:
                if cell.pieceColor() == 'white':
                    whiteCells = whiteCells + 1

            if whiteCells == 3:
                count = count + 1

        return count

    def blackMills(self):
        count = 0

        for mill in self.mills:
            cells = self.getCellsFromMill(mill)
            blackCells = 0
            for cell in cells:
                if cell.pieceColor() == 'black':
                    blackCells = blackCells + 1

            if blackCells == 3:
                count = count + 1

        return count

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

    def remove(self, touch):
        point = {
            'x': touch.x - 25,
            'y': touch.y - 25
        }
        removed = False

        for cell in self.cells:
            if cell.close(point.get('x'), point.get('y')):
                cell.removePiece()
                removed = True

        return removed
     
    def select(self, touch):
        point = {
            'x': touch.x - 25,
            'y': touch.y - 25
        }

        for cell in self.cells:
            if cell.close(point.get('x'), point.get('y')):
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