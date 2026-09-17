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

    if priority_dict == dict1:
        for k,v in dict2:
            if v < 10 or k in priority_dict.keys():
                continue
            priority_dict[k] = v

    elif priority_dict == dict2:
        for k,v in dict1:
            if v < 10 or k in priority_dict.keys():
                continue
            priority_dict[k] = v

    return priority_dict
