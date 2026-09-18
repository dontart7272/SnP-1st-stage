'''
Напишите декоратор @cached, который кэширует результаты функции, чтобы
избежать повторных вычислений для одних и тех же аргументов. Декоратор
должен поддерживать:

• ограничение размера кэша: при превышении максимально хранимого
количества записей (max_size) удаляются самые старые записи:
• если max_size=None, то размер кэша не ограничен
• если max_size не соответствует целому числу, то также
инициализировать его как None
• время жизни записей: автоматически удалять результаты, сохранённые
более seconds назад:
• если seconds=None, то записи не устаревают
• размер кэша не ограничен, если seconds не соответствует целому
числу, то также инициализировать его как None
• декоратор должен учитывать как позиционные (*args), так и
именованные аргументы (**kwargs)
'''
from asyncio import ReadTransport
import time
from collections.abc import Callable
from functools import wraps


class CacheValue:
    '''Вспомогательный класс для удобного хранения значений кеша.'''

    def __init__(self, result) -> None:
        self.result = result    # Результат функции
        self.saved_at = time.monotonic()    # временная метка последнего обращения к значению фунции


    def is_expired(self, seconds: int | None) -> bool:
        '''Проверка, что время жизни кеша не истекло'''
        return seconds is not None and (time.monotonic() - self.saved_at) >= seconds




def cached(max_size: int | None = None, seconds: int | None = None):
    # Валидация переданных аргументов
    if type(max_size) != int: max_size = None
    if type(seconds) != int or seconds < 0: seconds = None

    def decorator(func: Callable):
        cache_dict: dict[str, CacheValue] = {}

        @wraps(func)
        def wrapper(*args, **kwargs):

            key = repr((args, sorted(kwargs.items()))) # Формирую ключ для словаря кеша

            value = cache_dict.get(key)

            # Уддалените кеша, если его время жизни истекло
            if value is not None:
                if value.is_expired(seconds=seconds):
                    del cache_dict[key]
                else:
                    return value.result

            result = func(*args, **kwargs)

            if max_size != 0:
                cache_dict[key] = CacheValue(result=result)

            # Удаление старейших записей при пререполнении кеша
            if max_size is not None:
                while len(cache_dict) > max_size:
                    oldest_key = min(cache_dict, key=lambda k: cache_dict[k].saved_at)
                    del cache_dict[oldest_key]

            return result
        return wrapper
    return decorator



if __name__ == '__main__':

    @cached(max_size=3, seconds=10)
    def slow_function(x):
        print(f"Вычисляю для {x}...")
        res = 0
        for i in range(x):
            res += i
        return res

    # Первый вызов — вычисляется
    print(slow_function(1000000000)) # Вывод: "Вычисляю для 2..." → 4
    # Повторный вызов с теми же аргументами — берётся из кэша
    print(slow_function(1000000000)) # Вывод: 4 (без вычисления)
    # Через 15 секунд кэш устареет, и будет новое вычисление
    time.sleep(15)
    print(slow_function(1000000000)) # Вывод: "Вычисляю для 2..." → 4
