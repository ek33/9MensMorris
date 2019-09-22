class Game:
    ongoing = True
    players = []
    turn = 0

    def __init__(self):
        print('Starting Game')

    def nextTurn(self):
        print('turn {}'.format(self.turn))
        self.turn += 1
        if self.turn > 2:
            self.ongoing = False