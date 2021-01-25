# task2
'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
 — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
 У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
 Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod


class Wear(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def consumption(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Coat(Wear):
    def __init__(self, size):
        super().__init__()
        self._size_of_coat = size

    @property
    def consumption(self):
        self._value = (self._size_of_coat / 6.5) + 0.5
        return self._value

    def __add__(self, other):
        return (self._value + other._value)


class Suit(Wear):
    def __init__(self, size):
        super().__init__()
        self._size_of_suit = size

    @property
    def consumption(self):
        self._value = (2 * self._size_of_suit + 0.3)
        return self._value

    def __add__(self, other):
        return (self._value + other._value)


suit = Suit(35)
coat = Coat(42)

print(round(suit.consumption, 2))
print(round(coat.consumption, 2))

print(round((suit + coat), 2))
