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
MRO
"""