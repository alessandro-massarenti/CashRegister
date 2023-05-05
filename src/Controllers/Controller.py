from abc import ABC, abstractmethod

from Views import View
from interfaces import Observer


class Controller(Observer):

    def __init__(self):
        self.__view: View = None

    def set_view(self, view: View):
        self.__view = view
