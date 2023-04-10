from abc import ABC
from interfaces import Observer


class ObservableSubject(ABC):

    def __init__(self):
        self.__observers: list[Observer] = []

    def register(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        self.__observers.append(observer)

    def unregister(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        self.__observers.remove(observer)

    def _notify_observers(self) -> None:
        """
        Notify all observers about an event.
        """
        for observer in self.__observers:
            observer.update(self)
