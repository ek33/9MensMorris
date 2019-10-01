from src.game import Game
from kivy.app import App
from kivy.uix.widget import Widget

from kivy.core.window import Window
Window.size = (950, 650)
Window.clearcolor = (94/256, 107/256, 98/256, 1)

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
