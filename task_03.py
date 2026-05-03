'''
Дан список элементов произвольной природы. Необходимо разработать метод
max_odd(array), который определит максимальный нечетный элемент (21.000 = 21 и
тоже считается нечетным элементом). Вернуть None, если таких элементов нет в
переданном массиве.
'''

from typing import Iterable


def max_odd(lst: list[object]) -> int | None:
    
    res: set = set() # В этом множесве буду хранит все неченые числа из lst
     
    for num in lst:
        # Отсекаю все, что не является числом (bool тоже, хоть и наследник int)
        if type(num) not in (int, float):
            continue
        
        # Выбираю только нечетные челые числа и добавляю в res
        if num % 2 == 1:
            res.add(num)

    return max(res) if res else None


if __name__ == '__main__':
    assert max_odd([1, 2, 3, 4, 4]) == 3
    assert max_odd([21.0, 2, 3, 4, 4]) == 21
    assert max_odd(['ololo', 2, 3, 4, [1, 2], None]) == 3
    assert max_odd(['ololo', 'fufufu']) is None
    assert max_odd([2, 2, 4]) is None