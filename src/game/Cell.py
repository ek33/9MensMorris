import math
class Cell:
    margin = 10
    def __init__(self, x, y, id, empty):
        self.x = x
        self.y = y
        self.id = id
        self.empty = empty

    def close(self, x, y):
        h_dist = (x - self.x) ** 2
        v_dist = (y - self.y) ** 2

        return math.sqrt(h_dist + v_dist) < self.margin
