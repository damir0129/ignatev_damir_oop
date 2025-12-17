# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"call function: {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"Finished: {func.__name__}")
#         return result
#     return wrapper
#
# @logger
# def test_example():
#     print("Выполняется тест...")
#
# test_example()


class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"call function: {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"Finished: {self.func.__name__}")
        return result

@Logger
def test_example():
    print("Выполняется тест...")

test_example()

test_example = Logger(test_example)