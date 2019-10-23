from src.game import Player
from src.board import Board

class Game:
    board
    players = []
	ongoing = True

    def __init__(self, board, player1, player2):
        print('Starting Game')
        self.board = board
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
