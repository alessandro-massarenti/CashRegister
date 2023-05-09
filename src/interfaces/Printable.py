from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def get_text(self):
        pass
