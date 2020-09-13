import vk_api
import pprint

vk_session = vk_api.VkApi(login='8914XXXXXXX', password='XXXXXXXXXX', api_version='5.122')
vk_session.auth()

# Позволяет обращаться к методам API как к обычным классам.
# Например vk.wall.get(...)
vk = vk_session.get_api()

friends = vk.friends.get(user_id=267000500, fields='domain, bdate, city')['items']
pprint.pprint(friends)
exit()

for friend in friends:
    t = vk.users.get(user_ids=friend)
    print('ID={}, {} {}'.format(t[0]['id'], t[0]['first_name'], t[0]['last_name']))
