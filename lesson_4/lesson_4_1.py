from datetime import datetime

class BankAccount:
    BANK_NAME = "3zap Bank" # атрибут класса
    MIN_BALANCE = 0 # атрибут класса

    def __init__(self, owner, balance):
        self.owner = owner # атрибут экземпляра
        self.balance = balance # атрибут экземпляра

    def __getattribute__(self, name):
        print(f"[LOG] "
              f"{datetime.now().strftime('%Y.%m.%d %H:%M:%S.%m')} "
              f"Доступ к атрибуту: {name}")
        return object.__getattribute__(self, name)

    def __setattr__(self, key, value):
        if key == 'balance' and value < self.MIN_BALANCE:
            raise ValueError(f"Баланс не может быть меньше, чем {self.MIN_BALANCE}")
        print(f"[LOG] "
              f"{datetime.now().strftime('%Y.%m.%d %H:%M:%S.%m')} "
              f"Изменение атрибута '{key}' на значение '{value}'")
        object.__setattr__(self, key, value)

    def __getattr__(self, name):
        print(f"[WARN] "
              f"{datetime.now().strftime('%Y.%m.%d %H:%M:%S.%m')} "
              f"Атрибут '{name}' не найден")
        return None

    def __delattr__(self, name):
        print(f"[LOG] "
              f"{datetime.now().strftime('%Y.%m.%d %H:%M:%S.%m')} "
              f"Удален атрибут '{name}'")
        object.__delattr__(self, name)

    @classmethod
    def set_min_balance(cls, value):
        cls.MIN_BALANCE = value

a1 = BankAccount("Damir", 10_000)
a2 = BankAccount("Ivan", 1_000)

a1.credit
del a1.balance

# a1.BANK_NAME
# a2.balance = 100
# a1.balance = 1_000_000
#
# BankAccount.set_min_balance(-100)
# a2.balance = -100
# a1.balance = -101
#
# print(a1.MIN_BALANCE)
# print(a2.MIN_BALANCE)
#
# print(a1.BANK_NAME)
# print(a2.BANK_NAME)
#
# print(a1.balance)
# print(a2.balance)
#
# print(a1.__dict__)
# print(a2.__dict__)