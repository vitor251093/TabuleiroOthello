#import Tkinter as tk

class ConsoleBoardView:
    def __init__(self, board):
        self.board = board

    def update_view(self):
        print self.board