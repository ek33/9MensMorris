from src.game import Game
from kivy.app import App
from src.game import Board
from kivy.uix.widget import Widget
from kivy.properties import (ObjectProperty)
from kivy.core.window import Window
Window.size = (970, 650)
Window.clearcolor = (94/256, 107/256, 98/256, 1)

class Piece(Widget):
    pass

class NineMenMorrisGame(Widget):
    turn = 1
    validTurn = False

    #app = App.get_running_app()



    white1 = ObjectProperty(None)
    white2 = ObjectProperty(None)
    white3 = ObjectProperty(None)
    white4 = ObjectProperty(None)
    white5 = ObjectProperty(None)
    white6 = ObjectProperty(None)
    white7 = ObjectProperty(None)
    white8 = ObjectProperty(None)
    white9 = ObjectProperty(None)

    black1 = ObjectProperty(None)
    black2 = ObjectProperty(None)
    black3 = ObjectProperty(None)
    black4 = ObjectProperty(None)
    black5 = ObjectProperty(None)
    black6 = ObjectProperty(None)
    black7 = ObjectProperty(None)
    black8 = ObjectProperty(None)
    black9 = ObjectProperty(None)

    def on_touch_down(self, touch):
        #self.app = App.get_running_app()
        #self.board=Board(self.app.root)
        self.board = Board(App.get_running_app().root)

        if (self.turn % 2):
            # black
            print('black')
            pieceName = 'black' + str(int((self.turn + 1) / 2))
            piece = getattr(self, pieceName)
            self.validTurn = self.board.place(piece, touch)
        else:
            # white
            print('white')
            pieceName = 'white' + str(int(self.turn / 2))
            piece = getattr(self, pieceName)
            self.validTurn = self.board.place(piece, touch)

        if (self.validTurn):
            self.turn += 1
            self.validTurn = False





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
