"""Inicio da aplicacao."""

from controllers.board_controller import BoardController
from models.move                  import Move
from models.board                 import Board

CONTROLLER = BoardController()
CONTROLLER.init_game()
