'''
Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором,
принимающим на вход name и calories (не обязательные параметры), а также двумя
методами is_healthy (возвращает true при условии калорийности десерта менее
200) и is_delicious (возвращает true для всех десертов).
'''

class Dessert:

    def __init__(self, name: str = 'default', calories: float = 0.0) -> None:
        self.__name = name
        self.__calories = calories


    @property
    def name(self) -> str:
        return self.__name


    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError('Неверный тип данных')
        self.__name = value



    @property
    def calories(self) -> float:
        return self.__calories


    @calories.setter
    def calories(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError('Неверный тип данных')
        elif value < 0:
            raise ValueError('Неверное значение')
        self.__calories = float(value)


    def is_healthy(self) -> bool:
        return self.calories < 200


    def is_delicious(self) -> bool:
        return True
