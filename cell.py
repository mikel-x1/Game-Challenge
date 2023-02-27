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
