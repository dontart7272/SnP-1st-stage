'''
Написать метод multiply_numbers(inputs), который вернет произведение цифр,
входящих в inputs.
'''

from collections.abc import Iterable
from math import prod


def multiply_numbers(input: str | float | Iterable | None = None) -> int | None:

    # Перевожу input в строку и пробегаюсь по каждому элементу
    # если элемент - цифра, то заношу в массив digits, предварительно переведя в тип int
    digits = [int(d) for d in str(input) if d.isdigit()]

    # возрващаю произведение чисел, если они есть в данных, иначе None
    return prod(digits) if digits else None




if __name__ == '__main__':
    assert multiply_numbers() is None
    assert multiply_numbers('ss') is None
    assert multiply_numbers('1234') == 24
    assert multiply_numbers('sssdd34') == 12
    assert multiply_numbers(2.3) == 6
    assert multiply_numbers([5, 6, 4])  == 120

    print('Все тесты пройдены успешно')
