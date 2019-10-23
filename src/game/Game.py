from src.game import Player

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
            
    def activePlayer(self):
    	for player in self.players:
        	if(player.turn)
            	return player
