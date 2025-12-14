# # class Telegram:
# #     def send(self, text):
# #         print(f"Sen message to Telegram: {text}")
# #
# #
# # class Email:
# #     def send(self, text):
# #         print(f"Send message to Email: {text}")
# #
# #
# # class SMS:
# #     def send(self, text):
# #         print(f"Send message via SMS: {text}")
# #
# # clients = [Telegram(), Email(), SMS()]
# #
# # for client in clients:
# #     client.send("Hello")
#
# class Notification:
#     def send(self, text):
#         print(f"Send notification...")
#
#
# class PushNotification(Notification):
#     def send(self, text):
#         super().send(text)
#         print(f"Push: {text}")
#
#
# class SMSNotification(Notification):
#     def send(self, text):
#         super().send(text)
#         print(f"SMS: {text}")
#
# clients = [PushNotification(), SMSNotification()]
#
# for client in clients:
#     client.send("Hello")

from abc import ABC, abstractmethod


class Sender(ABC):
    @abstractmethod
    def send(self, text):
        pass


class SMSSender(Sender):
    def __init__(self):
        print("Init SMSSender")


print(dir())