from abc import ABC
import ui_func as ui


class Math(ui.Interface, ABC):
    def __init__(self, num1=None, num2=None):
        self.num1 = num1
        self.num2 = num2

    @property
    def add(self):
        return self.num1 + self.num2

    @property
    def sub(self):
        return self.num1 - self.num2

    @property
    def mul(self):
        return self.num1 * self.num2

    @property
    def truediv(self):
        return self.num1 / self.num2
