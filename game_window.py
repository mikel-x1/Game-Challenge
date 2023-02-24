# -*- coding: utf-8 -*-
import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import Form, FormBorderStyle, MenuStrip, ToolStripControlHost, ToolStripMenuItem
clr.AddReference('System.Drawing')
from System.Drawing import Size


class GameWindow(Form):
    def __init__(self, rows, columns):
        self.Text = 'Tic-tac-toe'
        self.FormBorderStyle = FormBorderStyle.Fixed3D
        self.CenterToScreen
        self._indent_top = 50
        self._indent_left = 10
        self._indent_right = 10
        self._indent_buttom = 10
        self._cell_side = 100
        self._cell_size = Size(self._cell_side, self._cell_side)
        self._cells = []
        self._rows = rows
        self._columns = columns
        self.Size = self._generate_window_size(rows, columns)
        self.ClientSize = self._generate_window_size(rows, columns)
        self._initialize_components()

    def _initialize_components(self):
        self._generate_menu_strip()

    def _generate_menu_strip(self):
        menu_strip = MenuStrip()
        menu_strip.Parent = self

        file_item = ToolStripMenuItem("File")
        menu_strip.Items.Add(file_item)

        new_game = ToolStripMenuItem("New game")
        file_item.DropDownItems.Add(new_game)

        self._exit = ToolStripMenuItem("Exit")
        file_item.DropDownItems.Add(self._exit)

    def _generate_window_size(self, rows, columns):
        width = self._indent_left + columns * self._cell_side + self._indent_right + 10
        height = self._indent_top + rows * self._cell_side + self._indent_buttom + 33
        return Size(width, height)


if __name__ == '__main__':
    game = GameWindow(3, 3)
    game.ShowDialog()
