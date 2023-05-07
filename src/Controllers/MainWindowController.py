from Controllers import Controller
from interfaces import ObservableSubject


class MainWindowController(Controller):

    def __init__(self):
        super().__init__()

    def set_view(self, view):
        self.__view = view

    def update(self, observable: ObservableSubject) -> None:
        pass
