from src.game import Player
from src.board import Board

class Game:
    ongoing = True
    players = []
    turn = 0

    def __init__(self, player1, player2):
        print('Starting Game')
        self.players.append(player1)
        self.players.append(player2)
	
    def nextTurn(self):
        print('turn {}'.format(self.turn))
        self.turn += 1
        if self.turn > 2:
            self.ongoing = False
  
    def transferTurn(self, name):
        for player in self.players:
        	player.turn = False
        	if player.name == name:
				player.turn = True
                return True
        # Needs to return false if name is wrong
