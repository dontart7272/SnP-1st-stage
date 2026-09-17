'''
Дан список целых чисел. Необходимо разработать метод sort_list(list), который
поменяет местами все минимальные и максимальные элементы массива, а также
добавит в конец массива одно минимальное значение из него.
'''



def sort_list(lst: list[int]) -> list[int]:
    
    # Проверяю, что массив имеет хотя бы один элемент
    if len(lst) == 0:
        return []
    
    # Вычисляю максимальное и минимальное значения
    max_val = max(lst)
    min_val = min(lst)
    
    # Для удобства создаю таблицу замены
    replace_table = {max_val: min_val, min_val: max_val}
    
    # собираю результирующий массив
    res = [replace_table.get(item, item) for item in lst] + [min_val]
    
    return res



if __name__ == '__main__':
    assert sort_list([]) == []
    assert sort_list([2, 4, 6, 8]) == [8, 4, 6, 2, 2]
    assert sort_list([1]) == [1, 1]
    assert sort_list([1, 2, 1, 3]) == [3, 2, 3, 1, 1]
    print('Все тесты пройдены успешно')