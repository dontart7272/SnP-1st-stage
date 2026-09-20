'''
Необходимо разработать метод connect_dicts(dict1, dict2), который соединит два
переданных словаря, значениями ключей в которых являются числа, и вернет
новый словарь, полученный по следующим правилам:

• приоритетными являются ключи того словаря, сумма значений ключей
которого больше (если суммы значений ключей будут равны, то второй
словарь считается более приоритетным)
• ключи со значениями меньше 10 не должны попасть в финальный
словарь
• получившийся словарь должен вернуться упорядоченным по значениям
ключей в порядке возрастания.
'''


def connect_dicts(dict1: dict[str, int], dict2: dict[str, int]) -> dict[str, int]:

    priority_dict = dict1 if sum(dict1.values()) > sum(dict2.values()) else dict2
    minor_dict = dict2 if priority_dict is dict1 else dict1

    result = {k: v for k, v in priority_dict.items() if v >= 10}

    for k, v in minor_dict.items():
        if v < 10 or k in result:
            continue
        result[k] = v


    return dict(sorted(result.items(), key=lambda kv: kv[1]))


if __name__ == '__main__':
    assert connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }) == { "c": 11, "b": 12 }
    assert connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }) == { 'd': 11, "c": 12, "a": 13 }
    assert connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }) == { "c": 11, "b": 12, "a": 15 }
