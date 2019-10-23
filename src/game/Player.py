
class Player:
	name = ''
	peices = []
    turn = False
    
	def __init__(self, name, peices):
    	print('Init Player: {}'.format(name))
        self.name = name
        self.peices = peices
        
    def livePeices():
    	return self.peices.live
        
    def deadPeices():
    	return self.peices.dead
