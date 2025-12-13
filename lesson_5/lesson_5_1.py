# # class Test:
# #     pass
# #
# # Test()
# # Test.__call__
#
# class AddToCartCounter:
#     def __init__(self):
#         self.count = 0
#
#     def __call__(self, product_name):
#         self.count += 1
#         print(f"{product_name} добавлен в корзину\n"
#               f"Всего товаров: {self.count}")
#         return self.count
#
# add_to_cart = AddToCartCounter()
#
# def test_add_products():
#     add_to_cart("Laptop")
#     add_to_cart("Earphones")
#     add_to_cart("Mouse")
#     assert add_to_cart.count == 3, (
#         "Неверное количество товаров в корзине\n"
#         f"Ожидаемое количество: 4\n"
#         f"Фактический результат: {add_to_cart.count}"
#     )
#
# test_add_products()

class Status:
    def __init__(self, code):
        self.code = code

    def __call__(self, response_code):
        if response_code == self.code:
            print(f"Статус код совпадает с ожидаемым: {self.code}")
            return True
        else:
            print(f"Статус код: {response_code} не совпадает с ожидаемым: {self.code}")
            return False

is_ok = Status(200)

assert is_ok(200)
assert is_ok(404)