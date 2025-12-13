class BasePage:
    def open(self, url: str):
        print(f"Открываем страницу {url}")

    def click(self, element_name: str):
        print(f"Клик по элементу {element_name}")


class LoginPage(BasePage):
    def login(self, username: str, password: str):
        print(f"Вход в аккаунт:\nЛогин: {username}\nПароль: {password}")


"""

LoginPage -> BasePage -> object

"""
# print(issubclass(LoginPage, BasePage))
#
# lp = LoginPage()
#
# print(isinstance(lp, LoginPage))
# print(isinstance(lp, object))

# print(issubclass(int, object))

class Str(str):
    def __str__(self):
        return "Это строка: " + self

s1 = str("kwqem")
print(s1)

s2 = Str("kqwem")
print(s2)