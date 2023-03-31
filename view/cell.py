# -*- coding: utf-8 -*-
import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import Button, FlatStyle, MouseButtons, MouseEventArgs
clr.AddReference('System.Drawing')
from System.Drawing import Color


class Cell(Button):
    def __init__(self, y, x):
        self._y = y
        self._x = x
        self._typed = False
        self.Text = ''

    @property
    def y(self):
        return self._y

    @property
    def x(self):
        return self._x

    def set_value(self, value):
        self.Text = value

    @property
    def is_typed(self):
        return self._typed

    @property
    def is_X(self, value):
        if value == 'X':
            return True

    @property
    def is_O(self, value):
        if value == 'O':
            return True

    def OnGotFocus(self, *args):
        self.NotifyDefault(False)

    def change_view(self, value, is_X, is_O):
        if is_X:
            self.Text = 'X'
            self.BackColor = Color.FromArgb(255, 0, 0)
            self._checked = True
        if is_O:
            self.Text = 'O'
            self.BackColor = Color.FromArgb(0, 0, 255)
            self._checked = True
