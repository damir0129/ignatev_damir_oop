from abc import ABC, abstractmethod

"""
======================================
1. Создай три класса: Cat, Dog, Duck.
В каждом реализуй метод speak(), возвращающий уникальную строку.
Создай список из экземпляров этих классов и вызови метод speak()
в цикле.
======================================

"""

class Cat:
    def speak(self):
        return "Мяу"

class Dog:
    def speak(self):
        return "Гав"

class Duck:
    def speak(self):
        return "Кря"

speaks = [Cat(), Dog(), Duck()]
for animals in speaks:
    print(animals.speak())

"""
2. Создай базовый класс Shape
Создай три класса-наследника: Square, Rectangle, Triangle,
в каждом реализуй метод get_pr().
Проверь, что список shapes = [Square(...), Rectangle(...), Triangle(...)]
можно обойти в цикле и вызвать get_pr() у каждого.
======================================

"""

class Shape(ABC):

    @abstractmethod
    def get_pr(self):
        pass


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_pr(self):
        return 2 * (self.a + self.b)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


shapes = [Square(4), Rectangle(3, 5), Triangle(3, 4, 5)]

for shape in shapes:
    print(shape.get_pr())

"""

3. Сделай класс Shape абстрактным.
Переопредели get_pr() как @abstractmethod.
Попробуй создать объект класса Shape напрямую и убедись, что будет TypeError.
======================================

"""

# s = Shape()


"""

4. Создай классы A, B, C, в каждом — свой __init__() с print("init A/B/C").
Наследуй D(A, B, C) и вызови super().__init__() в каждом __init__.
Выведи D.__mro__ и посмотри, в каком порядке вызываются инициализаторы.
======================================

"""

class A:
    def __init__(self):
        print("init A")
        super().__init__()


class B:
    def __init__(self):
        print("init B")
        super().__init__()


class C:
    def __init__(self):
        print("init C")
        super().__init__()


class D(A, B, C):
    def __init__(self):
        print("init D")
        super().__init__()

print(D.__mro__)

"""

5. Создай MixinLog (как в уроке).
Создай класс бронирования гостиницы (методы и атрибуты на свое усмотрение).
Создай класс, который наследует оба класса. Создай экземпляр этого класса.
======================================

"""

import datetime


class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.price}, {self.weight}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("Init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id} продан в {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

class Notebook(Goods, MixinLog):
    pass

n = Notebook("Acer", 1.5, 50_000)
n.print_info()
n.save_sell_log()

print(Notebook.__mro__)
"""

6. В Goods и MixinLog реализуй print_info().
Создай NoteBook(Goods, MixinLog) и проверь, какой метод вызывается.
Измени порядок наследования — изменилась ли логика?
======================================
======================================
Далее задания можете сделать через классы, функции или без них.
======================================
======================================
7. Напиши программу, которая запрашивает (из консоли) два числа и делит первое на второе.
Если второе число равно нулю — обработай ошибку (как называется ошибка найди сам)
и выведи сообщение: "На ноль делить нельзя!"
======================================

"""

# class Divider:
#     def divide(self):
#         try:
#             a, b = map(int, input("Введите числа a и b через пробел: ").split())
#             print(a / b)
#         except ZeroDivisionError as e:
#             print("На ноль делить нельзя!")
#             print("Текст ошибки:", e)
#         except ValueError as e:
#             print("Ошибка ввода: введите два числа через пробел")
#             print("Текст ошибки:", e)
#         except Exception as e:
#             print("Произошла неизвестная ошибка")
#             print("Текст ошибки:", e)
#
#
# d = Divider()
# d.divide()


"""

8. Расширь программу из Задания 1:
Добавь обработку ошибки (как называется ошибка найди сам),
если пользователь ввёл не числа, а текст.
Выведи сообщение: "Ошибка ввода: введите два числа через пробел"
======================================
9. Модифицируй код так, чтобы после обработки конкретных ошибок
был ещё один общий except, который перехватывает все остальные ошибки и выводит:
"Произошла неизвестная ошибка"
======================================
10. При перехвате исключений из 7 и 8 заданий,
сохрани ошибку в переменную e и выведи её текст:
======================================
11. Создай код, который ловит арифметические ошибки (ArithmeticError) в одном блоке.
Попробуй специально сделать ошибку деления на ноль или другую арифметическую ошибку.
======================================

"""

# try:
#     a = 10
#     b = 0
#     print(a / b)   # деление на ноль
# except ArithmeticError as e:
#     print("Арифметическая ошибка:", e)


"""

12. Запроси у пользователя два числа и выполни деление.
Если деление прошло успешно без ошибок — выведи
"Деление выполнено успешно" через (но не в блоке try)
======================================

"""

# try:
#     a = int(input("Введите a: "))
#     b = int(input("Введите b: "))
#     result = a / b
# except (ValueError, ZeroDivisionError):
#     print("Ошибка при выполнении деления")
# else:
#     print("Деление выполнено успешно")


"""


13. Расширь код из Задания 12:
Добавь блок, в котором будет выводиться
"Работа программы завершена", независимо от успеха деления.
======================================
"""
# try:
#     a = int(input("Введите a: "))
#     b = int(input("Введите b: "))
#     result = a / b
# except (ValueError, ZeroDivisionError):
#     print("Ошибка при выполнении деления")
# else:
#     print("Деление выполнено успешно")
# finally:
#     print("Работа программы завершена")
"""

14. Реализуй две вложенные конструкции:
Внешний try/except обрабатывает неверный ввод (строки вместо чисел);
Внутренний try/except ловит деление на ноль.
======================================

"""

# try:
#     a = int(input("Введите a: "))
#     b = int(input("Введите b: "))
#     try:
#         print(a / b)
#     except ZeroDivisionError:
#         print("На ноль делить нельзя!")
# except ValueError:
#     print("Ошибка ввода: введите числа")

"""

15. Вынеси обработку деления в отдельную функцию divide(x, y)
с собственным try/except.
Во внешнем коде обработай только ошибку ввода.
"""

# def divide(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError:
#         print("На ноль делить нельзя!")
#         return None
#
#
# try:
#     a = int(input("Введите a: "))
#     b = int(input("Введите b: "))
#     result = divide(a, b)
#     if result is not None:
#         print(result)
# except ValueError:
#     print("Ошибка ввода: введите числа")
