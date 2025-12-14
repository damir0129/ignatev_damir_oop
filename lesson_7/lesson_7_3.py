from http.client import responses

try:
    pass
    """Вызывается код в котором может быть ошибка"""
except ValueError as a:
    pass
    """Отлавливает ошибки ValueError"""
except TypeError as a:
    pass
    """Отлавливает ошибки TypeError"""
else:
    pass
    """Выполнится, если ошибок нет (не попало в except)"""
finally:
    pass
    """Выполняется всегда, если не было raise или return"""


import requests

BASE_URL = "http://api.hh.ru"
def get_vacancies(base_url):
    try:
        response = requests.get(f"{base_url}/vacancies")
        response.raise_for_status()
        response_json = response.json()

    except requests.exceptions.HTTPError as e:
        print(f"Возникла ошибка: {e}")
    except ValueError:
        print(f"Не удалось получить json")
    else:
        try:
            resp_for_return = response_json['items']
        except:
            pass
        else:
            return response_json


resp = get_vacancies(BASE_URL)


print(resp)
# print(resp.json())
# print(resp.status_code)

"""
Все наслудется от BaseException

ValueError, TypeError - неверные данные/типы
IndexError, KeyError - не нашли индекс/ключ
FileNotFoundError, PermissionError - файловые операции
requests исключения: Timeout, ConnectionError, HTTPError
KeyboardInterrupt - остановка руками
"""