import math
from kivy.properties import (ObjectProperty)

class Cell:

    margin = 30
    piece = None

    def __init__(self, x, y, id, empty=True):
        self.x = x
        self.y = y
        self.id = id
        self.empty = empty

    def close(self, x, y):
        h_dist = (x - self.x) ** 2
        v_dist = (y - self.y) ** 2

        return math.sqrt(h_dist + v_dist) < self.margin

    def removePiece(self):
        self.piece.pos = 0, 0
        self.piece = ObjectProperty(None)
        self.empty = True

    def setPiece(self, piece):
        piece.pos = self.x, self.y
        self.piece = piece
        self.empty = False

    def pieceColor(self):
        if not self.empty:
            if 'black' in self.piece.source:
                return 'black'
            if 'white' in self.piece.source:
                return 'white'

        return False