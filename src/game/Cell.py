import math
class Cell:
    margin = 40

    def __init__(self, x, y, id, empty):
        self.x = x
        self.y = y
        self.id = id
        self.empty = empty

    def close(self, point):
        x2 = point.get('x')
        y2 = point.get('y')
        print('{}, {}'.format(x2, y2))

        h_dist = (x2 - self.x) ** 2
        v_dist = (y2 - self.y) ** 2

        return math.sqrt(h_dist + v_dist) < self.margin