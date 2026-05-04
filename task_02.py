'''
Дан список list и числовой диапазон range. Разработайте метод coincidence(list,
range) для определения элементов из массива list, значения которого входят в
указанный диапазон range. Если не передан хотя бы один из параметров, то
должен вернуться пустой массив.
'''

from typing import Iterable



def coincidence(lst: Iterable[int | str | float | None] | None = None, 
                rng: range | None = None
                ) -> Iterable[int]:
    
    # проверяю, что переданы все аргументы
    if not all((lst, rng)):
        return []
    
    res = [] 
    
    # пробегаюсь по по списку и добавляю в результирующий массив если выполняются все условия
    # элемент строки - число
    # его значение не меньше поля start в диапазоне
    # его значение меньше поля stop в диапазоне
    for obj in lst:
        if isinstance(obj, (float, int)) and obj >= rng.start and obj < rng.stop:
            res.append(obj)
    
    return res




if __name__ == '__main__':
    assert coincidence([1, 2, 3, 4, 5], range(3, 6)) == [3, 4, 5]
    assert coincidence() == []
    assert coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)) == [1, 2, 2.5]