class BasePage:
    def __init__(self):
        self.base_url = "https://google.com"
        print("Инициализация BasePage")


    def open(self, url: str):
        print(f"Открываем страницу {url}")

    def click(self, element_name: str):
        print(f"Клик по элементу {element_name}")


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        print("Инициализация LoginPage")

    def login(self, username: str, password: str):
        print(f"Вход в аккаунт:\nЛогин: {username}\nПароль: {password}")

    def click(self, element_name: str):
        super().click(element_name)
        print(f"Клик по элементу на странице Входа {element_name}")

lp = LoginPage()
lp.click("Кнопка")
print(lp.base_url)