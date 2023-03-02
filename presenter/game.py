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
        if not cell.is_typed:
            if args.Button == MouseButtons.Left:
                self._left_click(cell)

    def _left_click(self, cell):
        self._closed_cells += 1
        value = self._field[cell.y][cell.x]
        if value == 0:
            value = self._give_value()
            cell.set_value(value)

    def _give_value(self):
        if self._field.count('X') > self._field.count('O'):
            return 'O'
        else:
            return 'X'


if __name__ == '__main__':
    g = Game()
