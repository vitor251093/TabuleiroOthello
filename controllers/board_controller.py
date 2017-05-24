"""Controlador de jogo de Othelo."""

import glob

from views.console_board_view import ConsoleBoardView
from models.board import Board

class BoardController(object):
    """Objeto do controlador de jogo de Othelo."""

    def __init__(self):
        self.board = Board(None)
        self.view = ConsoleBoardView(self, self.board)

        self.white_player = None
        self.black_player = None
        self.atual_player = None
        self.finish_game = 0

    def init_game(self):
        """Inicia a partida de Othelo em seu tabuleiro (board)."""
        self.white_player = self._select_player(Board.WHITE)
        self.black_player = self._select_player(Board.BLACK)
        self.atual_player = self.black_player

        self.view.atualizar_discos()
        self.view.put_view_in_main_loop()

    def next_round(self):
        """Permite que a IA realize a jogada seguinte."""
        if self.finish_game == 3:
            return

        atual_color = self.atual_player.color
        print 'Jogador: ' + atual_color
        if self.board.valid_moves(atual_color).__len__() > 0:
            self.board.play(self.atual_player.play(self.board.get_clone()), atual_color)
            self.view.atualizar_discos()
            self.finish_game = 0
        else:
            print 'Sem movimentos para o jogador: ' + atual_color
            self.finish_game += 1
        self.atual_player = self._opponent(self.atual_player)

        if self.finish_game == 2:
            self._end_game()

    def _end_game(self):
        score = self.board.score()
        if score[0] > score[1]:
            self.view.anunciar_vitorioso(self.white_player.__class__.__name__,
                                         self.black_player.__class__.__name__,
                                         score[0], score[1])
        elif score[0] < score[1]:
            self.view.anunciar_vitorioso(self.black_player.__class__.__name__,
                                         self.white_player.__class__.__name__,
                                         score[1], score[0])
        else:
            print ""
            print 'Jogo terminou empatado'
        self.finish_game = 3

    def _opponent(self, player):
        if player.color == Board.WHITE:
            return self.black_player

        return self.white_player

    def _select_player(self, color):
        players = glob.glob('./models/players/*_player.py')
        print 'Selecione um dos players abaixo para ser o jogador '+color

        for idx, player in enumerate(players):
            print idx.__str__() + " - " + player

        player = raw_input("Digite o numero do player que voce deseja: ")
        module_globals = {}
        execfile(players[int(player)], module_globals)
        print module_globals.keys()
        return module_globals[module_globals.keys()[len(module_globals.keys()) - 1]](color)
