'''
Разработайте метод is_palindrome(string), который будет определять, является ли
параметр string палиндромом (строкой, которая читается одинаково как сначала
так и с конца), при условии игнорирования пробелов, знаков препинания и
регистра.
'''
from string import punctuation

# Формирую словарь вида {unicode : None} для каждого удаляемого симола
REPLACE_TABLE = str.maketrans('', '', punctuation + ' ')


def is_palindrome(val: str | float | None) -> bool:

    # Проверяю на none
    if val is None:
        return False

    val = str(val).lower() # привожу к строке
    val = val.translate(REPLACE_TABLE) # Удаляю все символы с кодами в ключах в REPLACE_TABLE

    return val == val[::-1]




if __name__ == '__main__':
    assert is_palindrome("A man, a plan, a canal -- Panama") is True
    assert is_palindrome("Madam, I'm Adam!") is True
    assert is_palindrome(333) is True
    assert is_palindrome(None) is False
    assert is_palindrome("Abracadabra") is False
