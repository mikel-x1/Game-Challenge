# -*- coding: utf-8 -*-
from model.field import Field
from view.game_window import GameWindow

import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import MouseButtons


class Game(object):
    def __init__(self):
        self._model = None
        self._view = None
        self._is_game_over = False
        self._closed_cells = 0
