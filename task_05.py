'''
Разработать метод date_in_future(integer), который вернет дату через integer дней.
Если integer не является целым числом, то метод должен вывести текущую дату.
Формат возвращаемой методом даты должен иметь следующий вид '24-03-2001
22:33:44'.
'''

from datetime import datetime, timedelta


def date_in_future(integer: int) -> str:

    # Проверяю, если параметр integer - целое число
    if type(integer) is not int:
        integer = 0

    now = datetime.now().astimezone() # Запоминаю текущую дату
    delta = timedelta(days=integer) # Создаю отрезок времени длинною в integer дней

    # Из условия не совcем понятно, функция должна возвращать объект datetime или строку
    # я решил возвращать строку в указанном в задании формате
    return (now + delta).strftime('%d-%m-%Y %H:%M:%S')



if __name__ == '__main__':
    print(f'Текущая дата: {date_in_future([])}')
    print(f'текущая дата + 2 дня: {date_in_future(2)}')
