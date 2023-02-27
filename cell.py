# -*- coding: utf-8 -*-
import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import Button
clr.AddReference('System.Drawing')


class Cell(Button):
    def __init__(self, y, x):
        self._y = y
        self._x = x

    @property
    def y(self):
        return self._y

    @property
    def x(self):
        return self._x

    def set_value(self, value):
        self.Text = value

    @property
    def is_X(self, value):
        if value == 1:
            return True

    @property
    def is_O(self, value):
        if value == 2:
            return True
