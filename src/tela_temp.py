from math import ceil
import tkinter as tk
from itertools import chain


class Tela:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.x_range = (-5, 5)
        self.y_range = (-5, 5)
        self.colore = "#000000"
        self.spessore = 1

    def w(self) -> int:
        return int(self.canvas.cget("width"))

    def h(self) -> int:
        return int(self.canvas.cget("height"))

    def linea(self, p1: tuple[int, int], p2: tuple[int, int]):
        self.canvas.create_line(*p1, *p2, fill=self.colore, width=self.spessore)

    def linee(self, points: list[tuple[int, int]]):
        if len(points) < 2:
            return
        self.canvas.create_line(*chain(points), fill=self.colore, width=self.spessore)

    def ellisse(self, p1: tuple[int, int], p2: tuple[int, int]):
        self.canvas.create_oval(*p1, *p2, outline=self.colore, width=self.spessore)

    def pulisci(self):
        self.canvas.delete("all")

    def disegna_sfondo(self):
        w = self.w()
        h = self.h()

        self.canvas.create_rectangle(0, 0, w, h, width=0, fill="#FFFFFF")

        min_x, max_x = self.x_range
        for x in range(int(ceil(min_x)), int(ceil(max_x))):
            x_canvas = self.x_piano_a_x_tela(x)
            self.canvas.create_line(x_canvas, 0, x_canvas, h, fill="#DDDDDD")

        min_y, max_y = self.y_range
        for y in range(int(ceil(min_y)), int(ceil(max_y))):
            y_canvas = self.y_piano_a_y_tela(y)
            self.canvas.create_line(0, y_canvas, w, y_canvas, fill="#DDDDDD")

        y_x_line = self.y_piano_a_y_tela(0)
        x_y_line = self.x_piano_a_x_tela(0)
        self.canvas.create_line(0, y_x_line, w, y_x_line, fill="#000000", arrow=tk.LAST)
        self.canvas.create_line(x_y_line, 0, x_y_line, h, fill="#000000", arrow=tk.FIRST)

    def disegna_numeri(self):
        pass

    def x_piano_a_x_tela(self, x):
        min_x, max_x = self.x_range
        if max_x == min_x:
            return 0
        return (x - min_x) / (max_x - min_x) * self.w()

    def y_piano_a_y_tela(self, y):
        min_y, max_y = self.y_range
        if max_y == min_y:
            return self.w()
        return ((y - min_y) / (min_y - max_y) + 1) * self.w()

    def x_tela_a_x_piano(self, xc):
        min_x, max_x = self.x_range
        if self.w() == 0:
            return min_x
        return xc / self.w() * (max_x - min_x) + min_x

    def y_tela_a_y_piano(self, yc):
        min_y, max_y = self.y_range
        if 0 == self.h():
            return min_y
        return (self.h() - yc) / self.h() * (max_y - min_y) + min_y
