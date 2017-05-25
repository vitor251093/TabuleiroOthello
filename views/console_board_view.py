"""View do jogo de Othelo."""

import Tkinter as Tkinter
import tkMessageBox as Alert

def realizar_proxima_jogada(event=None):
    """Permitir que a proxima jogada seja executada."""

    if ConsoleBoardView.partida_iniciada == 0:
        Alert.showerror('Erro', 'Nao e possivel avancar uma jogada antes de iniciar a partida.')
    else:
        ConsoleBoardView.controller.next_round()

class ConsoleBoardView(object):
    """Objeto de view do jogo de Othelo."""

    WINDOW_NAME = 'Othelo'
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 400

    TABULEIRO_X = 20
    TABULEIRO_Y = 20
    TABULEIRO_SIDE = 396
    TABULEIRO_COLOR = '#CCC'

    TABULEIRO_CASA_NUM = 9
    TABULEIRO_CASA_SIDE = TABULEIRO_SIDE/TABULEIRO_CASA_NUM
    TABULEIRO_DISCO_MARGEM = 10

    partida_iniciada = 0

    master = Tkinter.Tk()
    master.title(WINDOW_NAME)
    master.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    master.maxsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

    canvas = Tkinter.Canvas(master, width=TABULEIRO_SIDE + TABULEIRO_X*2,
                            height=TABULEIRO_SIDE + TABULEIRO_Y*2)
    canvas.grid(row=0, rowspan=3, column=0, columnspan=2)

    for i in range(0, TABULEIRO_CASA_NUM-1):
        for j in range(0, TABULEIRO_CASA_NUM-1):
            canvas.create_rectangle(TABULEIRO_X + TABULEIRO_CASA_SIDE*i,
                                    TABULEIRO_Y + TABULEIRO_CASA_SIDE*j,
                                    TABULEIRO_X + TABULEIRO_CASA_SIDE*(i+1),
                                    TABULEIRO_Y + TABULEIRO_CASA_SIDE*(j+1),
                                    fill=TABULEIRO_COLOR, outline='#000', tag='tabuleiro')

    action_button = Tkinter.Button(master, text="Avancar", command=realizar_proxima_jogada)
    action_button.grid(row=2, column=2)
    master.bind('<Return>', realizar_proxima_jogada)


    def __init__(self, controller, board):
        ConsoleBoardView.controller = controller
        self.board = board

    def put_view_in_main_loop(self):
        """Coloca a view em loop principal quando o terminal para de ser usado."""
        ConsoleBoardView.master.mainloop()

    def anunciar_vitorioso(self, vencedor, perdedor, pontos_vencedor, pontos_perdedor):
        """Anuncia caso alguem venca a partida."""
        Alert.showinfo('Fim de jogo', vencedor + ' venceu a partida contra ' + perdedor +
                       ' (' + str(pontos_vencedor) + ' - ' + str(pontos_perdedor) + ')!')

    def _desenhar_disco(self, i, j, color):
        margem = ConsoleBoardView.TABULEIRO_DISCO_MARGEM
        pos_x0 = ConsoleBoardView.TABULEIRO_X + ConsoleBoardView.TABULEIRO_CASA_SIDE*(j-1) + margem
        pos_y0 = ConsoleBoardView.TABULEIRO_Y + ConsoleBoardView.TABULEIRO_CASA_SIDE*(i-1) + margem
        pos_x1 = ConsoleBoardView.TABULEIRO_X + ConsoleBoardView.TABULEIRO_CASA_SIDE*j - margem
        pos_y1 = ConsoleBoardView.TABULEIRO_Y + ConsoleBoardView.TABULEIRO_CASA_SIDE*i - margem

        if color == '@':
            ConsoleBoardView.canvas.create_oval(pos_x0, pos_y0, pos_x1, pos_y1,
                                                fill='#000', outline='#000', tag='discos')
        if color == 'o':
            ConsoleBoardView.canvas.create_oval(pos_x0, pos_y0, pos_x1, pos_y1,
                                                fill='#FFF', outline='#000', tag='discos')

    def atualizar_discos(self):
        """Atualiza a view do jogo."""
        ConsoleBoardView.partida_iniciada = 1
        ConsoleBoardView.canvas.delete('discos')

        for i in range(1, ConsoleBoardView.TABULEIRO_CASA_NUM):
            for j in range(1, ConsoleBoardView.TABULEIRO_CASA_NUM):
                self._desenhar_disco(i, j, self.board.get_square_color(i, j))

        print self.board
