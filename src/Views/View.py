import tkinter as tk
from abc import ABC

from Controllers import Controller


class View(ABC):

    def __init__(self, parent, controller: Controller):
        self._frame = tk.Frame(parent)
        self._controller = controller

    def show(self):
        self._frame.pack()

    def frame(self):
        return self._frame
