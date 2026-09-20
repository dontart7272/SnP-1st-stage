'''
Анаграмма — литературный приём, состоящий в перестановке букв или звуков
определённого слова (или словосочетания), что в результате даёт другое слово
или словосочетание.
Разработайте метод combine_anagrams(words_array), который принимает на вход
массив слов и разбивает их в группы по анаграммам, регистр букв не имеет
значения при определении анаграмм.
'''


def combine_anagrams(words_array: list[str]) -> list[list[str]]:

    # Словарь для удобства хранения данных
    groups: dict[str, list[str]] = {}

    # перебираем все элементы массива
    for word in words_array:
        # Ключ слловаря - отсортированная по возрпастанию строка
        key = ''.join(sorted(word.lower()))
        # Если ключ уже есть, то, добавляем слово в список связанный с ключем, есмли нет, то создаем новую пару ключ-значение
        groups.setdefault(key, []).append(word)

    return sorted(groups.values())



if __name__ == '__main__':
    assert combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]) == sorted([ ["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"], ["creams", "scream"] ])
