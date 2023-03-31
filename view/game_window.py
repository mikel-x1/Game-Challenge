# -*- coding: utf-8 -*-
import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import (
    Form, FormBorderStyle, MenuStrip, Label,
    ToolStripMenuItem, TextRenderer
)
clr.AddReference('System.Drawing')
from System.Drawing import Size, Point
from cell import Cell


class GameWindow(Form):
    def __init__(self, rows, columns):
        self.Text = 'Tic-tac-toe'
        self.FormBorderStyle = FormBorderStyle.Fixed3D
        self.CenterToScreen
        self._indent_top = 50
        self._indent_left = 20
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
        self._create_buttons()

        self._result = Label()
        self._result.Parent = self
        self._result.Text = ''
        self._result.Size = TextRenderer.MeasureText(self._result.Text, self._result.DefaultFont)
        self._result.Location = Point(self.Size.Width / 2 - self._result.Size.Width / 2 - 5, 30)

    def _generate_menu_strip(self):
        menu_strip = MenuStrip()
        menu_strip.Parent = self

        file_item = ToolStripMenuItem("File")
        menu_strip.Items.Add(file_item)

        self._exit = ToolStripMenuItem("Exit")
        self._exit.Click += self._exit_game
        file_item.DropDownItems.Add(self._exit)

    def _create_buttons(self):
        for y in range(self._rows):
            row = []
            for x in range(self._columns):
                cell = Cell(y, x)
                cell.Text = ''
                cell.Parent = self
                cell.Size = self._cell_size
                cell.Location = Point(self._indent_left + x * self._cell_side,
                                      self._indent_top + y * self._cell_side)
                row.append(cell)
            self._cells.append(row)

    def set_cell_click_handler(self, handler):
        for row in self._cells:
            for cell in row:
                cell.MouseDown += handler

    def _generate_window_size(self, rows, columns):
        width = self._indent_left + columns * self._cell_side + self._indent_right + 10
        height = self._indent_top + rows * self._cell_side + self._indent_buttom + 33
        return Size(width, height)

    def set_final_message(self, message):
        self._result.Text = message
        self._result.Size = TextRenderer.MeasureText(self._result.Text, self._result.DefaultFont)
        self._result.Location = Point(self.Size.Width / 2 - self._result.Size.Width / 2 - 5, 30)

    def _exit_game(self, sender, args):
        self.Close()


if __name__ == '__main__':
    game = GameWindow(3, 3)
    game.ShowDialog()
