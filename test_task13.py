"""Временный тест-скрипт для task_13: проверяет исходный и исправленный @cached."""
import time
from collections.abc import Callable
from functools import wraps

from task_13 import cached as cached_original


# ------------------- исправленная версия (предложение из чата) -------------------

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

    def write_cache(func: Callable):
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
    return write_cache


# --------------------------------- тесты ---------------------------------

def run_suite(title: str, cached_impl) -> None:
    print(f"\n=== {title} ===")
    results = []

    def check(title: str, fn) -> None:
        try:
            ok, detail = fn()
            status = "PASS" if ok else "FAIL"
        except Exception as e:
            status, detail = "ERROR", f"{type(e).__name__}: {e}"
        results.append((status, title, detail))

    def counter():
        state = {"n": 0}

        def f(*a, **k):
            state["n"] += 1
            return sum(a) + sum(k.values())

        return f, state

    def t_basic_hit():
        f, s = counter()
        f = cached_impl()(f)
        f(1)
        f(1)
        return s["n"] == 1, f"вычислений: {s['n']}, ожидалось 1"

    def t_args_distinct():
        f, s = counter()
        f = cached_impl()(f)
        f(1)
        f(2)
        return s["n"] == 2, f"вычислений: {s['n']}, ожидалось 2"

    def t_kwargs_distinct_from_args():
        f, s = counter()
        f = cached_impl()(f)
        f(1, 2)
        f(1, y=2)
        return s["n"] == 2, f"вычислений: {s['n']}, ожидалось 2"

    def t_kwargs_order():
        f, s = counter()
        f = cached_impl()(f)
        f(a=1, b=2)
        f(b=2, a=1)
        return s["n"] == 1, f"вычислений: {s['n']}, ожидалось 1"

    def t_max_size_fifo():
        f, s = counter()
        f = cached_impl(max_size=2)(f)
        f(1)
        f(2)
        f(3)  # запись (1,) вытесняется
        f(1)  # -> должна пересчитаться
        return s["n"] == 4, f"вычислений: {s['n']}, ожидалось 4"

    def t_ttl_expired():
        f, s = counter()
        f = cached_impl(seconds=1)(f)
        f(1)
        time.sleep(1.2)
        f(1)
        return s["n"] == 2, f"вычислений: {s['n']}, ожидалось 2"

    def t_ttl_fresh():
        f, s = counter()
        f = cached_impl(seconds=5)(f)
        f(1)
        f(1)
        return s["n"] == 1, f"вычислений: {s['n']}, ожидалось 1"

    def t_invalid_params():
        f, s = counter()
        f = cached_impl(max_size="10", seconds="abc")(f)
        for i in range(10):
            f(i)
        f(0)
        return s["n"] == 10, f"вычислений: {s['n']}, ожидалось 10"

    def t_purge_expired():
        f, s = counter()
        f = cached_impl(seconds=1)(f)
        f(1)
        time.sleep(1.2)
        f(2)  # во время этого вызова запись (1,) уже протухла
        return s["n"] == 2, f"вычислений: {s['n']}, ожидалось 2"

    check("T1 повторный вызов берётся из кэша", t_basic_hit)
    check("T2 разные args — разные записи", t_args_distinct)
    check("T3 f(1,2) и f(1,y=2) — разные ключи", t_kwargs_distinct_from_args)
    check("T4 порядок kwargs не важен", t_kwargs_order)
    check("T5 max_size=2 вытесняет старейшую", t_max_size_fifo)
    check("T6 seconds=1 запись протухает", t_ttl_expired)
    check("T7 seconds=5 свежая запись в кэше", t_ttl_fresh)
    check("T8 нецелые max_size/seconds -> None", t_invalid_params)
    check("T9 удаление протухших не ломает цикл", t_purge_expired)

    for status, title, detail in results:
        print(f"  [{status:^5}] {title} — {detail}")


run_suite("ИСХОДНОЕ РЕШЕНИЕ (task_13.cached)", cached_original)
