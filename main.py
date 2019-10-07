from src.game import Game
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (ObjectProperty, ReferenceListProperty)
from kivy.core.window import Window
Window.size = (970, 650)
Window.clearcolor = (94/256, 107/256, 98/256, 1)

class Piece(Widget):
    pass

class NineMenMorrisGame(Widget):
    i=0
    white1 = ObjectProperty(None)
    black1 = ObjectProperty(None)
    white2 = ObjectProperty(None)
    black2 = ObjectProperty(None)
    def on_touch_down(self, touch):
        if self.i == 0:
            self.white1.pos = touch.x - 25, touch.y - 25
        elif self.i == 1:
            self.black1.pos = touch.x - 25, touch.y - 25
        elif self.i == 2:
            self.white2.pos = touch.x - 25, touch.y - 25
        else:
            self.black2.pos = touch.x - 25, touch.y - 25

        self.i+=1




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
