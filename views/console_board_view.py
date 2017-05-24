"""View do jogo de Othelo."""

import Tkinter as Tkinter

class ConsoleBoardView(object):
    """Objeto de view do jogo de Othelo."""

    WINDOW_NAME = 'Othelo'
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 400

    TABULEIRO_X = 20
    TABULEIRO_Y = 20
    TABULEIRO_SIDE = 396

    TABULEIRO_CASA_NUM = 9
    TABULEIRO_CASA_SIDE = TABULEIRO_SIDE/TABULEIRO_CASA_NUM

    master = Tkinter.Tk()
    master.title(WINDOW_NAME)
    master.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    master.maxsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

    canvas = Tkinter.Canvas(master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.pack()

    for i in range(0, TABULEIRO_CASA_NUM-1):
        for j in range(0, TABULEIRO_CASA_NUM-1):
            canvas.create_rectangle(TABULEIRO_X + TABULEIRO_CASA_SIDE*i,
                                    TABULEIRO_Y + TABULEIRO_CASA_SIDE*j,
                                    TABULEIRO_X + TABULEIRO_CASA_SIDE*(i+1),
                                    TABULEIRO_Y + TABULEIRO_CASA_SIDE*(j+1),
                                    fill='#FFF', outline='#000')

    def __init__(self, board):
        self.board = board

    def update_view(self):
        """Atualiza a view do jogo."""
        print self.board
 
