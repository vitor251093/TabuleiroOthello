"""View do jogo de Othelo."""

import Tkinter as Tkinter
import tkMessageBox as Alert
import ttk as Ttk

def realizar_proxima_jogada(event=None):
    """Permitir que a proxima jogada seja executada."""

    if ConsoleBoardView.partida_iniciada == 0:
        Alert.showerror('Erro', 'Nao e possivel avancar uma jogada antes de iniciar a partida.')
    else:
        ConsoleBoardView.controller.next_round()

class ConsoleBoardView(object):
    """Objeto de view do jogo de Othelo."""

    # Constantes mutaveis; podem ser mudadas para melhor visualizacao do tabuleiro
    WINDOW_NAME = 'Othelo'
    WINDOW_WIDTH = 720
    WINDOW_HEIGHT = 400

    TABULEIRO_X = 20
    TABULEIRO_Y = 20
    TABULEIRO_SIDE = 396
    TABULEIRO_COLOR = '#CCC'
    TABULEIRO_DISCO_MARGEM = 10

    # Constantes imutaveis; necessarias deste jeito para o funcionamento do app
    TABULEIRO_CASA_NUM = 9
    TABULEIRO_CASA_SIDE = TABULEIRO_SIDE/TABULEIRO_CASA_NUM

    # Variavel que define se a partida ja comecou ou nao
    partida_iniciada = 0

    # Inicia a janela do programa
    master = Tkinter.Tk()
    master.title(WINDOW_NAME)
    master.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    master.maxsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

    # Inicia o canvas usado para desenhar o tabuleiro
    canvas = Tkinter.Canvas(master, width=TABULEIRO_SIDE + TABULEIRO_X*2,
                            height=TABULEIRO_SIDE + TABULEIRO_Y*2)
    canvas.grid(row=0, rowspan=16, column=0, columnspan=6)

    # Desenhando as casas do tabuleiro
    for i in range(0, TABULEIRO_CASA_NUM-1):
        for j in range(0, TABULEIRO_CASA_NUM-1):
            canvas.create_rectangle(TABULEIRO_X + TABULEIRO_CASA_SIDE*i,
                                    TABULEIRO_Y + TABULEIRO_CASA_SIDE*j,
                                    TABULEIRO_X + TABULEIRO_CASA_SIDE*(i+1),
                                    TABULEIRO_Y + TABULEIRO_CASA_SIDE*(j+1),
                                    fill=TABULEIRO_COLOR, outline='#000', tag='tabuleiro')

    # Label de estado atual da partida
    state_label = Tkinter.Label(master, text="Escolha os jogadores", font=("Helvetica", 16))
    state_label.grid(row=1, column=7, columnspan=4)

    # Label "Black Player:"
    black_label = Tkinter.Label(master, text="Black player:")
    black_label.grid(row=2, column=7, columnspan=1)

    # Combobox "Black Player"
    black_box_value = ""
    black_box = Ttk.Combobox(master, textvariable=black_box_value)
    black_box.grid(row=2, column=8, columnspan=2)

    # Label "White Player:"
    white_label = Tkinter.Label(master, text="White player:")
    white_label.grid(row=3, column=7, columnspan=1)

    # Combobox "White Player"
    white_box_value = ""
    white_box = Ttk.Combobox(master, textvariable=white_box_value)
    white_box.grid(row=3, column=8, columnspan=2)

    # Adicionando botao de avancar
    action_button = Tkinter.Button(master, text="Avancar", command=realizar_proxima_jogada)
    action_button.grid(row=12, column=7, columnspan=3)
    master.bind('<Return>', realizar_proxima_jogada)


    def __init__(self, controller, board):
        ConsoleBoardView.controller = controller
        self.board = board

    def carregar_jogadores_possiveis(self, jogadores):
        """Carrega os nomes dos jogadores possiveis nos ComboBoxes."""
        ConsoleBoardView.black_box['values'] = jogadores
        ConsoleBoardView.black_box.current(0)

        ConsoleBoardView.white_box['values'] = jogadores
        ConsoleBoardView.white_box.current(0)

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
