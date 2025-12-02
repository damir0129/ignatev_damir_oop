# class BankAccount:
#     BANK_NAME = "3zap Bank"
#     MIN_BALANCE = 0
#
#     def __init__(self, owner, balance):
#         self.__owner = owner
#         self.__balance = balance
#
#     def get_balance(self):
#         return self.__balance
#
#     def set_balance(self, value):
#         self.__balance = value
#
# a1 = BankAccount("Damir", 1_000)
#
# print(a1.get_balance())
# a1.set_balance(200)
# print(a1.get_balance())

class BankAccount:
    BANK_NAME = "3zap Bank"
    MIN_BALANCE = 0

    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < self.MIN_BALANCE:
            raise ValueError(f"Баланс не может быть меньше, чем {self.MIN_BALANCE}")
        self.__balance = value

a1 = BankAccount("Damir", 1_000)
print(a1.balance)
a1.balance = 111
print(a1.balance)