# -*- coding: utf-8 -*-
from model.field import Field
from view.game_window import GameWindow

import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import MouseButtons


class Game(object):
    def __init__(self):
        self._field = Field()
        self._game_window = GameWindow(3, 3)
        self._game_window.ShowDialog()
        self._typed_cells = 0

    def _mouse_button_down(self, cell, args):
        if cell.Text == '':
            if args.Button == MouseButtons.Left:
                self._left_click(cell)

    def _left_click(self, cell):
        cell.set_value('X')


if __name__ == '__main__':
    g = Game()
