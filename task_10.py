'''
Разработайте функцию count_words(string), которая будет возвращать словарь со
статистикой частоты употребления входящих в неё слов.
'''

from string import punctuation


def count_words(value: str) -> dict[str, int]:

    splited_data = value.lower().split(' ')
    splited_data = [w.strip(punctuation) for w in splited_data]
    res = { word : splited_data.count(word) for word in splited_data if word }
    return res



if __name__ == '__main__':
    assert count_words("A man, a plan, a canal -- Panama") == {"a": 3, "man": 1,"canal": 1, "panama": 1, "plan": 1}
    assert count_words("Doo bee doo bee doo") == {"doo": 3, "bee": 2}
