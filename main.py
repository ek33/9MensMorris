from src.game import Game
from kivy.app import App
from kivy.uix.widget import Widget

from kivy.core.window import Window
Window.size = (950, 650)

class NineMenMorrisGame(Widget):
    pass

class NineMenMorrisApp(App):
    def build(self):
        self.title = "9 Men's Morris"
        return NineMenMorrisGame()

if __name__ == '__main__':
    NineMenMorrisApp().run()

    game = Game()

    while game.ongoing:
        game.nextTurn()

    print('Game Over')
