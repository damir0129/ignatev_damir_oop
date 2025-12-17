# # class Calculator:
# #     def divide(self, a, b):
# #         try:
# #             return a / b
# #         except ZeroDivisionError:
# #             print("Ошибка деления на ноль")
# #             return None
# #
# # calc = Calculator()
# # print("Начинаем вычисление")
# # res = calc.divide(10, 0)
# # print(f"Результат готов: {res}")
# # # assert res, "Ошибка"
#
#
# class APIClient:
#     def get_user(self, user_id):
#         raise ConnectionError("Сервер недоступен")
#
#
# class UserService:
#     def __init__(self):
#         self.client = APIClient()
#
#     def get_user_info(self, user_id):
#         return self.client.get_user(user_id)
#
#
# class TestUserAPI:
#     def test_get_user(self):
#         client = UserService()
#         try:
#             client.get_user_info(1)
#         except ConnectionError as e:
#             print(f"Ошибка подключения: {e}")
#             # assert False, "API не отвечает"
# #
# TestUserAPI().test_get_user()

class BaseAPIClient:
    def request(self, endpoint):
        try:
            return self._send(endpoint)
        except Exception as e:
            print(f"Лог ошибки: {e}")
            raise

    def _send(self, endpoint):
        raise NotImplementedError


class ProductClient(BaseAPIClient):
    def _send(self, endpoint):
        raise TimeoutError("Превышено время ожидания")


client = ProductClient()
client.request('/product')