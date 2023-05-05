import tkinter as tk
from abc import ABC

from Controllers import Controller


class View(ABC):

    def __init__(self, parent, controller: Controller):
        self._frame = tk.Frame(parent)
        self.__controller = controller

    def show(self):
        self._frame.pack()

    @property
    def _controller(self):
        return self.__controller

    def frame(self):
        return self._frame
