"""View do jogo de Othelo."""

import Tkinter as Tkinter

class ConsoleBoardView(object):
    """Objeto de view do jogo de Othelo."""

    WINDOW_NAME = 'Othelo'
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600

    master = Tkinter.Tk()
    master.title(WINDOW_NAME)
    master.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    master.maxsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

    canvas = Tkinter.Canvas(master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.pack()

    canvas.create_rectangle(30, 30, 10, 10, fill='#000')

    def __init__(self, board):
        self.board = board

    def update_view(self):
        """Atualiza a view do jogo."""
        print self.board
 
