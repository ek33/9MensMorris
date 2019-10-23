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
   
    def transferTurn(self, name):
        for player in self.players:
        	player.turn = False
        	if player.name == name:
				player.turn = True
                return True
        # Needs to return false if name is wrong
        
	def gameOver(self):
    	# if any player has < 3 peices
        # if no more moves
        # ect...
        
    def winner(self):
    	# return winner
        return self.players[0]