from abc import ABC, abstractmethod
from Models import Tabulation


class TabsRepository(ABC):

    @abstractmethod
    def get(self, client_name: str) -> Tabulation:
        pass

    @abstractmethod
    def get_all(self) -> list[Tabulation]:
        pass

    @abstractmethod
    def add(self, tab: Tabulation):
        pass

    @abstractmethod
    def delete(self, client_name: str):
        pass
