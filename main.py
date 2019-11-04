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
    lastPhase = 0
    phase = 0

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
        if self.turn % 2:
            print('black - phase {} ::: mill # = {}'.format(self.phase, self.board.blackMills()))

            self.board.prevBlackMills = self.board.blackMills()

            # Placement phase
            if self.phase == 0:
                pieceName = 'black' + str(int((self.turn + 1) / 2))
                piece = getattr(self, pieceName)
                self.validTurn = self.board.place(piece, touch)

            # Moving phase
            if self.phase == 1:
                if self.board.selected:
                    self.validTurn = self.board.move(touch, 'black')
                else:
                    self.board.select(touch, 'black')

            # Removing phase
            if self.phase == 2:
                self.validTurn = self.board.remove(touch, 'white')
                if self.validTurn:
                    self.phase = self.lastPhase



            # Check for new mills
            if self.board.blackMills() > self.board.prevBlackMills:
                print('black made a new mill')
                self.validTurn = False # still your turn
                self.lastPhase = self.phase #last phase
                self.phase = 2 # next click will be removal
                self.board.prevBlackMills = self.board.blackMills()


        else:
            print('black - phase {} ::: mill # = {}'.format(self.phase, self.board.blackMills()))
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
                self.phase = self.lastPhase

            # Check for new mills
            if self.board.whiteMills() > self.board.prevWhiteMills:
                print('white made a new mill')
                self.validTurn = False  # still your turn
                self.lastPhase = self.phase  # last phase
                self.phase = 2  # next click will be removal
                self.board.prevWhiteMills = self.board.whiteMills()


        if self.validTurn:
            self.turn += 1
            self.validTurn = False

        # if self.turn > 18:
        if self.turn > 5:
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
