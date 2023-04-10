from abc import ABC, abstractmethod
from interfaces import ObservableSubject


class Observer(ABC):
    @abstractmethod
    def update(self, observable: ObservableSubject) -> None:
        """
        Update the observer, when the observable changes.
        """
        pass
