"""View do jogo de Othelo."""
#import Tkinter as tk

class ConsoleBoardView(object):
    """Objeto de view do jogo de Othelo."""

    def __init__(self, board):
        self.board = board

    def update_view(self):
        """Atualiza a view do jogo."""
        print self.board
        