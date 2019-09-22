from src.game import Game

if __name__ == '__main__':
    
    game = Game()

    while game.ongoing:
       game.nextTurn()

    print('Game Over')