'''
Реализуйте класс EvenNumbers, который в конструкторе принимает целое число n
— количество чётных чисел для генерации. Итератор должен выдавать числа по
порядку, начиная с 0: 0, 2, 4, ..., 2*(n-1).
'''
from collections.abc import Iterator


class EvenNumbers:

    def __init__(self, n: int) -> None:
        self.__n = n
        self.__current_value = -2


    @property
    def n(self) -> int:
        return self.__n

    @n.setter
    def n(self, value: int) -> None:
        if type(value) != int:
            raise TypeError('Передан неверный тип даннх')
        elif value < 0:
            raise ValueError('Переданный аргумент должн быть не меньше нуля')
        self.__n = value


    def __iter__(self) -> Iterator:
        self.__current_value = -2
        return self


    def __next__(self) -> int:
        next_value = self.__current_value + 2

        if next_value >= 2 * self.n:
            raise StopIteration

        self.__current_value = next_value
        return self.__current_value



if __name__ == '__main__':
    evens = EvenNumbers(5)
    for num in evens:
        print(num) # Должно вывести 0, 2, 4, 6, 8'
