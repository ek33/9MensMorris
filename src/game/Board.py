from src.game import Cell
from src.game import Mill
from kivy.app import App

class Board:
    cells = []
    selected = False
    prevWhiteMills = 0
    prevBlackMills = 0
    trashedWhite = 0
    trashedBlack = 0

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

    def getCellsFromMill(self, mill):
        cells = []

        for cell in self.cells:
            if mill.checkCell(cell.id):
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
                cell.setPiece(piece)
                placed = True

        return placed

    def remove(self, touch, color):
        point = {
            'x': touch.x - 25,
            'y': touch.y - 25
        }
        removed = False

        for cell in self.cells:
            if cell.close(point.get('x'), point.get('y')) and cell.pieceColor() == color:
                cell.trashPiece()
                if color == 'white':
                    self.trashedWhite += 1
                if color == 'black':
                    self.trashedBlack += 1
                removed = True

        return removed
     
    def select(self, touch, color):
        point = {
            'x': touch.x - 25,
            'y': touch.y - 25
        }

        for cell in self.cells:
            if cell.close(point.get('x'), point.get('y')) and not cell.empty and cell.pieceColor() == color:
                self.selected = cell
                return True

        self.selected = False
        return self.selected

    def move(self, touch, color):
        moved = False
        point = {
            'x': touch.x - 25,
            'y': touch.y - 25
        }


        if self.selected:
            if color == 'white':
                for neighbors in adjacent:
                    for neighbor in neighbors:
                        self.findById()
            if color == 'black':


            # if color == 'white':
                # neighborCells = []
                # if self.trashedWhite < 6:
                #     for mill in self.mills:
                #         if mill.checkCell(self.selected.id):
                #             neighborCells.append(self.findById(mill.id1))
                #             neighborCells.append(self.findById(mill.id2))
                #             neighborCells.append(self.findById(mill.id3))
                #
                # goodBoyCells = False
                # for cell in neighborCells:
                #     print(cell.id)
                #     if cell.close(point.get('x'), point.get('y')):
                #         goodBoyCells = True
                #
                # if not goodBoyCells:
                #     return False

            placed = self.place(self.selected.piece, touch)
            self.selected.removePiece()
            self.selected = False
            return placed

        else:
            return False

    def find(self, touch):
        point = {
            'x': touch.x - 25,
            'y': touch.y - 25
        }

        for cell in self.cells:
            if cell.close(point.get('x'), point.get('y')):
                return cell

        return False

    def findById(self, id):
        for cell in self.cells:
            if cell.id == id:
                return cell

        return False