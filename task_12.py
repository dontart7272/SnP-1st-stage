'''
Создайте класс JellyBean, расширяющий класс Dessert (из Упражнения 11) новым
геттером и сеттером для атрибута flavor (все параметры являются не
обязательными). Измените метод is_delicious таким образом, чтобы он возвращал
false только в тех случаях, когда flavor равняется «black licorice».
'''

from task_11 import Dessert


class JellyBean( Dessert ):

    def __init__(self, name: str = 'default', calories: float = 0, flavor: str = 'default') -> None:
        super().__init__(name, calories)
        self.__flavor = flavor


    @property
    def flavor(self) -> str:
        return self.__flavor

    @flavor.setter
    def flavor(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError('Неверный тип данных')
        self.__flavor = value


    def is_delicious(self) -> bool:
        return self.flavor != 'black licorice'
