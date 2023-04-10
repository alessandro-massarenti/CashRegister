from Repositories import TabsRepository
from Models import Tabulation


class LocalTabsRepository(TabsRepository):

    def __init__(self):
        self._tabs: list[Tabulation] = []

    def get(self, client_name: str) -> Tabulation:
        for tab in self._tabs:
            if tab.client_name == client_name:
                return tab
        return None

    def get_all(self) -> list[Tabulation]:
        return self._tabs

    def add(self, tab: Tabulation):
        self._tabs.append(tab)

    def delete(self, client_name: str):
        for tab in self._tabs:
            if tab.client_name == client_name:
                self._tabs.remove(tab)
                return
