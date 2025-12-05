# """
# ======================================
# 1. Создай класс SecureData, который:
#
# имеет атрибут __secret, задаваемый в __init__;
# переопределяет __getattribute__, чтобы при попытке получить __secret извне выбрасывать ValueError;
# внутри класса доступ к __secret должен работать.
# Проверь:
# data = SecureData("пароль123")
# print(data.__secret)      # ошибка
# print(data.get_secret())  # "пароль123"
# ======================================
#
# """
# from datetime import datetime
#
#
# class SecureData:
#     def __init__(self, secret):
#         self.__secret = secret
#
#     def __getattribute__(self, name):
#         print("[LOG] "
#             f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
#             f"Доступ к атрибуту {name}"
#         )
#         if name == "_SecureData__secret":
#             raise ValueError("Access denied!")
#         return object.__getattribute__(self, name)
#
#     def get_secret(self):
#         return self.__secret
#
#     def __setattr__(self, key, value):
#         if key == "token":
#             raise ValueError("token can't be created")
#         object.__setattr__(self, key, value)
#
# data = SecureData("12345")
#
# data.other = "ok"      # работает
# print(data.other)
#
# # data.token = "abc123"  # вызывает ошибку
#
# """
# 2. Добавь в класс SecureData метод __setattr__,
# который запрещает создание любого атрибута с именем token.
#
# Проверь:
# data.token = "abc123"  # ❌ AttributeError
# data.other = "ok"      # ✅ работает
# ======================================
# 3. Создай класс SafeDict, в котором:
#
# нет атрибута default;
# реализован __getattr__, который возвращает "N/A" (это строка) при попытке получить несуществующий атрибут;
# реализован __delattr__, который пишет "Удалён атрибут <имя>" и действительно удаляет атрибут.
# Проверь:
# d = SafeDict()
# print(d.unknown)     # "N/A"
# d.key = 10
# del d.key            # "Удалён атрибут key"
#
# """
# class SafeDict:
#     def __getattr__(self, name):
#         print(f"[WARN] "
#               f"{datetime.now().strftime('%Y.%m.%d %H:%M:%S.%m')} "
#               f"Атрибут '{name}' не найден")
#         return None
#
#     def __delattr__(self, name):
#         print("[LOG] "
#               f"{datetime.now().strftime('%Y.%m.%d %H:%M:%S.%m')} "
#               f"Атрибут {name} был удален")
#         object.__delattr__(self, name)
#
# d = SafeDict()
# print(d.unknown)     # "N/A"
# d.key = 10
# del d.key            # "Удалён атрибут key"
# """
# ======================================
# 4. Создай класс Employee с приватными полями __name и __salary.
# Добавь @property для поля salary, а также сеттер с валидацией:
#
# зарплата должна быть положительным числом;
# если нет — выбрасывать ValueError.
# Проверь, что:
# e = Employee("Daniil", 5000)
# print(e.salary)   # 5000
# e.salary = 8000
# print(e.salary)   # 8000
# e.salary = -100   # ❌ ValueError
# ======================================
# """
# class Employee:
#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary
#
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary(self, value):
#         if not isinstance(value, int) or value < 0:
#             raise ValueError("salary should be more than 0")
#         self.__salary = value
#
#     @salary.deleter
#     def salary(self):
#         print("salary deleted")
#         del self.__salary
#
# e = Employee("Daniil", 5000)
# print(e.salary)   # 5000
# e.salary = 8000
# print(e.salary)   # 8000
# # e.salary = -100   # ❌ ValueError
#
# del e.salary
# print(e.__dict__)  # salary нет
#
# """
#
# 5. Добавь @deleter для поля salary, чтобы при удалении выводилось "зарплата удалена"
# и поле реально исчезало.
# Проверь:
#
# del e.salary
# print(e.__dict__)  # salary нет
# 6. Представь, что ты пишешь обёртку над HTML-формой.
# Создай класс LoginForm с полем username, которое реализовано через @property.
#
# Логика:
# геттер возвращает self._username
# сеттер добавляет лог "username изменён"
# Проверь, что:
# form = LoginForm()
# form.username = "admin"  # выводит лог
# print(form.username)     # "admin"
# ======================================
#
# """
# class LoginForm:
#     def __init__(self, username):
#         self.__username = username
#
#     @property
#     def username(self):
#         return self.__username
#
#     @username.setter
#     def username(self, value):
#         print("username is changed")
#         self.__username = value
#
#
# form = LoginForm("32")
# form.username = "admin"  # выводит лог
# print(form.username)     # "admin"
#
#
# """
#
# 7. Создай класс Card, где:
# поле __number хранит номер карты (строка);
# в @property возвращай номер с маской **** **** **** 1234;
# в @setter проверяй, что номер состоит из 16 цифр;
# в @deleter логируй удаление номера с текущим временем.
# Напиши тесты (через assert)
# проверку установки корректного номера;
# проверку исключения при вводе короткого номера;
# проверку вывода замаскированного номера.
# ======================================
#
# """
# class Card:
#     def __init__(self, number):
#         self.__number = number
#
#     @property
#     def number(self):
#         last4 = self.__number[-4:]
#         return f"**** **** **** {last4}"
#
#     @number.setter
#     def number(self, value):
#         if not isinstance(value, str) or not value.isdigit() or len(value) != 16:
#             raise ValueError("Номер карты должен быть строкой из 16 цифр")
#         self.__number = value
#
#     @number.deleter
#     def number(self):
#         print("[LOG] "
#               f"{datetime.now().strftime('%Y.%m.%d %H:%M:%S.%m')} "
#               f"Номер карты был удален")
#         del self.__number
# # 1. Установка корректного номера
# c = Card("1234567890123456")
# assert c.number == "**** **** **** 3456"
#
# # 2. Проверка исключения при неверном номере
# try:
#     c.number = "123"      # слишком короткий
#     assert False          # не должны попасть сюда
# except ValueError:
#     assert True
#
# # 3. Проверка маски
# c.number = "9999888877776666"
# assert c.number == "**** **** **** 6666"
#
# print("✅ Все тесты пройдены!")
# """
#
# 8. Создай класс UserData для API регистрации пользователя:
# email — строка, содержит @;
# age — целое число ≥ 18;
# is_active — bool;
# свойство .json возвращает словарь для запроса.
# Напиши тест (через assert)
# проверь, что при age = 15 выбрасывается ValueError;
# проверь, что email без @ вызывает ошибку;
# проверь, что json возвращает корректную структуру.
#
# """
class UserData:
    def __init__(self, email: str, age: int, is_active: bool):
        self.__email = email
        self.__age = age
        self.__is_active = is_active

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) and not "@" in value:
            raise ValueError("Должно быть строкой и содержать @")
        self.__email = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or not value >= 18:
            raise ValueError("Должно быть целым числом и больше или равно 18")
        self.__age = value

    @property
    def is_active(self):
        return self.__is_active

    @is_active.setter
    def is_active(self, value):
        if not isinstance(value, bool):
            raise ValueError("Значение может быть только булевым")

    @property
    def json(self):
        return {
            "email": self.email,
            "age": self.age,
            "is_active": self.is_active
        }

u = UserData("email@email.ru", 52, True)

u.age = 15

assert u