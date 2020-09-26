
"""Модуль для работы с VK_API

Это тестовый модуль. В нём отображаем друзей только для user_id=640666.
Программа запрашивает у пользователя логин и пароль для входа в VK.com
и выводит список друзей."""

import vk_api


# login: 8914XXXXXXX
login = input("Введите Логин VK.com: ")
# password: XXXXXXXXXXXXX
password = input("Введите Пароль от VK.com: ")

print("[+] Создаем сессию VK")
vk_session = vk_api.VkApi(login=login, password=password, api_version='5.122')

print("[+] Авторизуемся в VK")
# В случае ошибки, API возбуждает исключение
# TODO: Отловить исключение и показать пользователю в красивом виде
vk_session.auth()

# Позволяет обращаться к методам API как к обычным классам.
# Например vk.wall.get(...)
print("[+] Инициализация VK API")
vk = vk_session.get_api()

print("Выполнение API метода friends.get")
friends = vk.friends.get(user_id=640666)['items']

for friend in friends:
    t = vk.users.get(user_ids=friend)
    print('ID={}, {} {}'.format(t[0]['id'], t[0]['first_name'], t[0]['last_name']))

input("Нажмите ВВОД")
