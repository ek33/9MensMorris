from kivy.app import App
from src.game import Board
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.properties import (ObjectProperty)
from kivy.core.window import Window
Window.size = (970, 650)
Window.clearcolor = (94/256, 107/256, 98/256, 1)


class Piece(Widget):
    pass

class NineMenMorrisGame(Widget):


    def callback(instance):
        if instance.text == "Person":
            print('p')
            NineMenMorrisGame.against="person"
        elif instance.text=="AI":
            print('a')
            NineMenMorrisGame.against="ai"
        NineMenMorrisGame.phase = 0
        NineMenMorrisGame.popup.dismiss()



    box = BoxLayout(orientation='vertical', padding=(10))
    box.add_widget(Label(text="Play against a person or AI?",font_size=13))
    popup = Popup(title='Select Opponent', title_size=(30),
                  title_align='center', content=box,
                  size_hint=(None, None), size=(200, 200),
                  auto_dismiss=False)
    box.add_widget(Button(text="Person", on_press=callback))
    box.add_widget(Button(text="AI", on_press=callback))
    popup.open()

    phase = 2
    against = "none"
    turn = 1
    validTurn = False
    lastPhase = 0


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

    def setup(self, app_root):
        self.board = Board(app_root)



    def on_touch_down(self, touch):
        # Black turn
        if not self.turn % 2:
            print('phase {}'.format(self.phase))
            self.board.prevBlackMills = self.board.blackMills()
            #Human Player for Black Pieces
            # Placement phase for person
            if self.against == "person" and self.phase == 0:
                pieceName = 'black' + str(int((self.turn + 1) / 2))
                piece = getattr(self, pieceName)
                self.validTurn = self.board.place(piece, touch)

            # Moving phase for person
            if self.against == "person" and self.phase == 1:
                if self.board.selected:
                    self.validTurn = self.board.move(touch, 'black')
                else:
                    self.board.select(touch, 'black')

            # Removing phase for person
            if self.against == "person" and self.phase == 2:
                self.validTurn = self.board.remove(touch, 'white')
                if self.validTurn:
                    self.phase = self.lastPhase

            # AI Player for Black Pieces
            # Placement phase for ai
            if self.against == "ai" and self.phase == 0:
                pieceName = 'black' + str(int((self.turn + 1) / 2))
                piece = getattr(self, pieceName)
                #self.validTurn = self.board.place(piece, touch)
                self.validTurn = self.board.placeAI(piece)

            # Moving phase for ai
            if self.against == "ai" and self.phase == 1:
                if self.board.selected:
                    self.validTurn = self.board.moveAI('black')
                else:
                    self.board.selectAI('black')

            # Removing phase for ai
            if self.against == "ai" and self.phase == 2:
                #self.validTurn = self.board.remove(touch, 'white')
                self.validTurn = self.board.removeAI('white')
                if self.validTurn:
                    self.phase = self.lastPhase



            # Check for new mills
            if self.board.blackMills() > self.board.prevBlackMills:
                print('black made a new mill')
                self.validTurn = False  # still your turn
                self.lastPhase = self.phase  # last phase
                self.phase = 2  # next click will be removal

        else:
            print('phase {}'.format(self.phase))
            self.board.prevWhiteMills = self.board.whiteMills()

            # Placement phase
            if self.phase == 0:
                pieceName = 'white' + str(int((self.turn + 1) / 2))
                piece = getattr(self, pieceName)
                self.validTurn = self.board.place(piece, touch)

            # Moving phase
            if self.phase == 1:
                if self.board.selected:
                    self.validTurn = self.board.move(touch, 'white')
                else:
                    self.board.select(touch, 'white')

            # Removing phase
            if self.phase == 2:
                self.validTurn = self.board.remove(touch, 'black')
                if self.validTurn:
                    self.phase = self.lastPhase

            # Check for new mills
            if self.board.whiteMills() > self.board.prevWhiteMills:
                print('white made a new mill')
                self.validTurn = False  # still your turn
                self.lastPhase = self.phase  # last phase
                self.phase = 2  # next click will be removal

        if self.validTurn:
            self.turn += 1
            self.validTurn = False
            if self.turn % 2:
                print('black - phase {} - mills {}'.format(self.phase, self.board.blackMills()))
            else:
                print('white - phase {} - mills {}'.format(self.phase, self.board.whiteMills()))

        if self.turn > 18 and self.phase != 2:
            self.phase = 1

        if self.board.trashedBlack >= 7 or self.board.trashedWhite >= 7:
            print('game over')



class NineMenMorrisApp(App):
    def build(self):
        self.title = "9 Men's Morris"
        self.game = NineMenMorrisGame()
        return self.game

    def on_start(self):
        self.game.setup(self.get_running_app().root)



if __name__ == '__main__':
    # Run App
    NineMenMorrisApp().run()
    
    # Create players
    # black =Player('white')
    # white =Player('black')
    #
    # # Give players peices
    #
    # # Choose who goes first
    # if choice == 'white':
    #     white.turn = True
    # if choice == 'black':
    #     black.turn = True

    # Create board
    # self.board = Board(App.get_running_app().root)
    #
    # # Create game
    # # game = Game(board, white, black)
    #
    # # Start game
    # while game.ongoing:
    # game.nextTurn()
    #
    # print('Game Over')
