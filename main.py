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
    #HereStarts
    app = App.get_running_app()

    CellList=[Cell.Cells(app.root.center_x - 325, app.root.center_y + 275, 'a1', True),
              Cell.Cells(app.root.center_x - 21, app.root.center_y + 275, 'a4', True),
              Cell.Cells(app.root.center_x + 275, app.root.center_y + 275, 'a7', True),
              Cell.Cells(app.root.center_x - 225, app.root.center_y + 175, 'b2', True),
              Cell.Cells(app.root.center_x - 21, app.root.center_y + 175, 'b4', True),
              Cell.Cells(app.root.center_x + 175, app.root.center_y + 175, 'b6', True),
              Cell.Cells(app.root.center_x - 125, app.root.center_y + 75, 'c3', True),
              Cell.Cells(app.root.center_x - 21, app.root.center_y + 75, 'c4', True),
              Cell.Cells(app.root.center_x + 75, app.root.center_y + 75, 'c5', True),
              Cell.Cells(app.root.center_x - 325, app.root.center_y - 20, 'd1', True),
              Cell.Cells(app.root.center_x - 225, app.root.center_y - 20, 'd2', True),
              Cell.Cells(app.root.center_x - 125, app.root.center_y - 20, 'd3', True),
              Cell.Cells(app.root.center_x + 75, app.root.center_y - 20, 'd5', True),
              Cell.Cells(app.root.center_x + 175, app.root.center_y - 20, 'd6', True),
              Cell.Cells(app.root.center_x + 275, app.root.center_y - 20, 'd7', True),
              Cell.Cells(app.root.center_x - 325, app.root.center_y - 323, 'g1', True),
              Cell.Cells(app.root.center_x - 21, app.root.center_y - 323, 'g4', True),
              Cell.Cells(app.root.center_x + 275, app.root.center_y - 323, 'g7', True),
              Cell.Cells(app.root.center_x - 225, app.root.center_y - 223, 'f2', True),
              Cell.Cells(app.root.center_x - 21, app.root.center_y - 223, 'f4', True),
              Cell.Cells(app.root.center_x + 175, app.root.center_y - 223, 'f6', True),
              Cell.Cells(app.root.center_x - 125, app.root.center_y - 123, 'e3', True),
              Cell.Cells(app.root.center_x - 21, app.root.center_y - 123, 'e4', True),
              Cell.Cells(app.root.center_x + 75, app.root.center_y - 123, 'e5', True)
              ]
    #HereEnds
    
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
