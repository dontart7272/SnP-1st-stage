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


    def update_time(self) -> None:
        '''Обновление временной метки при образении к классу'''
        self.saved_at = time.monotonic()




def cached(max_size: int | None = None, seconds: int | None = None):
    if not isinstance(max_size, int): max_size = None
    if not isinstance(seconds, int) or seconds < 0: seconds = None

    def decorator(func: Callable):
        cache_dict: dict[str, CacheValue] = {}

        @wraps(func)
        def wrapper(*args, **kwargs):

            key = (args, tuple(sorted(kwargs.items()))) # Формирую ключ для словаря кеша

            if key not in cache_dict:
                res = func(*args, **kwargs) # Сохраняю результат работы
                cache_dict[key] = CacheValue(result=res) # Создаю новую запись в кеше
            else:
                res = cache_dict[key]
                cache_dict[key].update_time() # Обновляю временную метку


            keys_to_delete = [k for k,v in cache_dict.items() if v.is_expired(seconds)]
            # Удаление кеша с истекшем временем жизни и тд
            for key in keys_to_delete:
                    del cache_dict[key]

            # Удаление старых записей для очистки кеша
            if max_size is not None:
                diff = len(cache_dict) - max_size

                if diff > 0:
                    oldest = sorted(cache_dict.items(), key=lambda kv: kv[1].saved_at)[:diff]

                    for key, _ in oldest:
                        del cache_dict[key]



            return res
        return wrapper
    return decorator
