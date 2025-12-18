"""
======================================
1. Создай две функции: inner() и outer().
В inner() вызови деление на ноль.
В outer() просто вызови inner().
Попробуй вызвать outer() без обработки ошибок и посмотри на стек вызовов.
======================================

"""

# def inner():
#     return 1/0
#
# def outer():
#     inner()
#
# outer()

"""

2. Добавь вокруг вызова outer() конструкцию try/except,
чтобы перехватить исключение и вывести сообщение
"Ошибка перехвачена на верхнем уровне".
======================================

"""

# def inner():
#     return 1 / 0
#
# def outer():
#     inner()
#
# try:
#     outer()
# except ZeroDivisionError:
#     print("Ошибка перехвачена на верхнем уровне")


"""

3. Перехвати исключение сразу в inner(), чтобы оно не поднималось дальше.
В случае ошибки возвращай строку "Ошибка в inner".
======================================

"""

# def inner():
#     try:
#         return 1 / 0
#     except ZeroDivisionError:
#         return "Ошибка в inner"
#
# def outer():
#     return inner()
#
# print(outer())

"""

4. Сделай так:
В inner() ошибка не перехватывается.
В outer() ошибка перехватывается через try/except.
В outer() при перехвате напечатай "Ошибка в outer".
======================================

"""

# def inner():
#     return 1 / 0
#
# def outer():
#     try:
#         inner()
#     except ZeroDivisionError:
#         print("Ошибка в outer")
#
#
# outer()


"""

5. Напиши функцию get_value(), которая кидает ValueError.
Напиши тестовую функцию test_get_value(), которая:

Вызывает get_value();
Ловит ValueError;
Завершает тест с assert False, если исключение поймано.
======================================
======================================

"""

def get_value():
    raise ValueError

def test_get_value():
    try:
        get_value()
    except ValueError:
        assert False

"""

6. Создай функцию divide(x, y).
Если y == 0, выбрасывай ZeroDivisionError через raise.
Иначе возвращай результат деления.
======================================

"""

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    else:
        return x / y


"""


7. Создай функцию sqrt(x), которая:
Вызывает raise NegativeNumberError (пользовательское исключение), если x < 0;
Иначе возвращает квадратный корень из x.
Проверь поведение функции через try/except.
======================================

"""
# import math
#
# def sqrt(x):
#     if x < 0:
#         raise NegativeNumberError("Число должно быть положительным")
#
#     return math.sqrt(x)
#
# class NegativeNumberError(Exception):
#     pass
#
# try:
#     print(sqrt(9))
#     print(sqrt(-4))
# except NegativeNumberError as e:
#     print("Поймано пользовательское исключение:", e)



"""

8. Создай базовый класс MathError.
От него унаследуй:
NegativeNumberError
DivisionByZeroError
В функции safe_divide(x, y) выбрасывай DivisionByZeroError, если y == 0.
Проверь в try/except обработку ошибок через базовый класс MathError.
======================================

"""

# class MathError(Exception):
#     pass
#
# class NegativeNumberError(MathError):
#     pass
#
# class DivisionByZeroError(MathError):
#     pass
#
# def safe_divide(x, y):
#     if y == 0:
#         raise DivisionByZeroError("Деление на ноль")
#     return x / y
#
# try:
#     safe_divide(2, 0)
# except MathError as e:
#     print(f"Поймана ошибка: {e}")

"""

9. Создай тестовую функцию test_sqrt(), которая:
вызывает sqrt(x) с отрицательным числом;
перехватывает NegativeNumberError;
завершает тест с assert False и сообщением
"Нельзя брать корень из отрицательного числа".
======================================


"""
# import math
#
# class NegativeNumberError(Exception):
#     pass
#
# def sqrt(x):
#     if x < 0:
#         raise NegativeNumberError("Нельзя брать корень из отрицательного числа")
#     return math.sqrt(x)
#
# def test_sqrt(x):
#     try:
#         res = sqrt(x)
#         print(res)
#     except NegativeNumberError:
#         assert False, "Нельзя брать корень из отрицательного числа"
#
# test_sqrt(22)

"""


======================================
10. Открой файл sample.txt, прочитай его содержимое и выведи на экран.
Обеспечь закрытие файла через with.
======================================

"""

# with open("sample.txt") as f:
#     for line in f:
#         print(line, end="")

"""

11. Создай класс BackupList, который:
делает копию списка при входе в with,
при выходе сохраняет изменения, если ошибок не было,
откатывает изменения при ошибке.
Проверь:
успешное изменение списка;
откат при ошибке.
======================================

"""
import copy

class BackupList:
    def __init__(self, data):
        self.data = data

    def __enter__(self):
        self._backup = copy.deepcopy(self.data)
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            return False
        else:
            self.data[:] = self._backup
            print("Произошла ошибка, изменения не сохранены")
            return False


"""

======================================
12. Создай декоратор-класс Timer,
который измеряет время выполнения функции и выводит результат.
"""

import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        res = self.func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения: {self.func.__name__}: {end - start:.6f} секунд")
        return res

@Timer
def slow_function():
    total = 0
    for i in range(1_000_000):
        total += 1
    return total

slow_function()