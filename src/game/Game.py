from src.game import Player

class Game:
    players = []
    ongoing = True

    def __init__(self, player1, player2):
        print('Starting Game')
        self.players.append(player1)
        self.players.append(player2) 		 
   
    # def transferTurn(self, name):
    #     for player in self.players:
    #         player.turn = False
    #         if player.name == name:
    #             player.turn = True
    #             return True
        # Needs to return false if name is wrong
        
	# def gameOver(self):
        # if any player has < 3 peices
        # if no more moves
        # ect...
        # return True
        
    def winner(self):
        # return winner
        return self.players[0]