class Mill:

    def __init__(self, id1, id2, id3):
        self.id1 = id1
        self.id2 = id2
        self.id3 = id3

    def checkCell(self, id):
        return id == self.id1 or id == self.id2 or id == self.id3