# -*- coding: utf-8 -*-
class Field(object):
    def __init__(self):
        self._rows = 3
        self._columns = 3
        self._field = [[0 for j in range(self._columns)] for i in range(self._rows)]

    def set_X(self, x, y):
        self._field[y][x] = 'X'

    def set_O(self, x, y):
        self._field[y][x] = '0'

    @property
    def field(self):
        return self._field


if __name__ == '__main__':
    f = Field()
    print f.field
