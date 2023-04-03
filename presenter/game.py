# -*- coding: utf-8 -*-
from model.field import Field
from view.game_window import GameWindow

import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import MouseButtons


class Game(object):
    def __init__(self):
        self._view = None
        self._model = None
        self._typed_cells = 0

    def start(self):
        self._model = Field()
        self._view_initialize()
        self._view.ShowDialog()

    def _view_initialize(self):
        self._view = GameWindow(3, 3)
        self._view.set_cell_click_handler(self._mouse_button_down)

    def _mouse_button_down(self, cell, args):
        if cell.Text == '':
            if args.Button == MouseButtons.Left:
                self._left_click(cell)

    def _left_click(self, cell):
        if self._typed_cells % 2 == 0:
            self._model.set_X(cell.x, cell.y)
            cell.set_value('X')
            self._typed_cells += 1
        else:
            self._model.set_O(cell.x, cell.y)
            cell.set_value('0')
            self._typed_cells += 1
        if self.game_status('0') == '0':
            self._view.set_final_message('0 Win!')
            self._disabled_cells()
        else:
            if self._typed_cells == 9:
                self._view.set_final_message('NOBODY Win!')
                self._disabled_cells()
        if self.game_status('X') == 'X':
            self._view.set_final_message('X Win!')
            self._disabled_cells()
        else:
            if self._typed_cells == 9:
                self._view.set_final_message('NOBODY Win!')
                self._disabled_cells()

    def game_status(self, p):
        m = self._model.field
        for i in m:
            if i == [p, p, p]:
                return p
        for i in list(zip(*m)):
            if i == (p, p, p):
                return p
        if [m[0][0], m[1][1], m[2][2]] == [p, p, p]:
            return p
        if [m[0][2], m[1][1], m[2][0]] == [p, p, p]:
            return p

    def _disabled_cells(self):
        for row in self._view._cells:
            for cell in row:
                if cell.Enabled:
                    cell.Enabled = False

if __name__ == '__main__':
    g = Game()
