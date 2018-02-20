import requests

APP_ID = '6380403'
TOKEN = 'ВСТАВИТЬ ЗДЕСЬ СВОЙ ТОКЕН'
VERSION = '5.73'
URL = 'https://api.vk.com/method/friends.get'


def get_friends_by_id(user_id):
    params = {
            'v': VERSION,
            'access_token': TOKEN,
            'user_id': user_id
    }
    friends = requests.get(URL, params)
    return friends.json()['response']['items']


id_input = input('Введите идентификаторы пользователей через запятую: ')
id_list = id_input.split(',')

friend_sets = []
for user_id in id_list:
    friend_sets.append(set(get_friends_by_id(user_id)))

mutual_friends = set.intersection(*friend_sets)

result = {}
for friend in mutual_friends:
    result[friend] = 'https://vk.com/id' + str(friend)

print('Общие друзья:')
print(result)
