class BasePage:
    def open(self, url: str):
        print(f"Открываем страницу {url}")

    def click(self, element_name: str):
        print(f"Клик по элементу {element_name}")


class LoginPage(BasePage):
    def login(self, username: str, password: str):
        print(f"Вход в аккаунт:\nЛогин: {username}\nПароль: {password}")

    def click(self, element_name: str):
        print(f"Клик по элементу на странице Входа {element_name}")


class CartPage(BasePage):
    def checkout(self):
        print("Оформление заказа")

login_page = LoginPage()

login_page.open("google.com")
login_page.click("Log In")
login_page.login("login", "password")

cart_page = CartPage()

cart_page.open("/cart")
cart_page.checkout()