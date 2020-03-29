from abc import ABC, abstractmethod


class Interface (ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

    @abstractmethod
    def mul(self):
        pass

    @abstractmethod
    def truediv(self):
        pass
