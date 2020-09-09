import vk_api


# vk_session = vk_api.VkApi(login='89141760725', password='vk_online4Igor', api_version='5.122')
login = input("Введите Логин VK.com: ")
password = input("Введите Пароль от VK.com: ")

print("[+] Создаем сессию")
vk_session = vk_api.VkApi(login=login, password=password, api_version='5.122')
print("[+] Авторизуемся")
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
