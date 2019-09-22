from src.game import Game

# Kivy Pong example
from kivy.app import App
from kivy.uix.widget import Widget

class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()

if __name__ == '__main__':

    PongApp().run()
    
    game = Game()

    while game.ongoing:
       game.nextTurn()

    print('Game Over')