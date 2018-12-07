import random

import requests
import vk_api
from config import *


def write_msg(user_id, text):
    vk_bot.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': random.randint(0, 1000)})


def send_photo(user_id, photo):
    vk_bot.method('messages.send', {'user_id': user_id, 'attachment': photo, 'random_id': random.randint(0, 1000)})


PHOTO_2 = 'photo324207419_456239051'
PHOTO_1 = 'photo-174113882_456239031'
random_photo = random.randint(1, 2)


def frwd_msg(user_id, messag, text):
    vk_bot.method('messages.send', {'user_id': user_id, 'forward_messages': messag, 'message': text,
                                    'random_id': random.randint(0, 1000)})


vk_bot = vk_api.VkApi(token=TOKEN)
ACCESS_KEY = ACCESS_TOKEN
long_poll = vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']
print("готов к работе")

# + str(long_poll))

while True:
    long_poll = requests.get(
        'https://{server}?act={act}&key={key}&ts={ts}&wait=9999999999999999'.format(server=server,
                                                                       act='a_check',
                                                                       key=key,
                                                                       ts=ts)).json()
    update = long_poll['updates']
    if update[0][0] == 4:
        if update[0][6].lower() == "привет":
            print(update)
            user_id = update[0][3]
            user_name = vk_bot.method('users.get', {'user_ids': user_id})
            print(user_name)
            write_msg(user_id, 'Привет, ' + (user_name[0]['first_name']))  # сообщение пользователю
            print(str(user_name[0]['first_name']) + ' ' +
                  str(user_name[0]['last_name']) + ' написал(а) боту - ' + str(update[0][6]))  # соообщение нам
        elif update[0][6].lower() == "кто молодец?":
            # print(update[0][6])
            user_id = update[0][3]
            write_msg(user_id, 'Ты молодец')
            print(str(user_name[0]['first_name']) + ' ' + str(user_name[0]['last_name']) + ' написал(а) боту - ' + str(
                update[0][6]))
        elif update[0][6].lower() == "как дела?":
            # print(update[0][6])
            user_id = update[0][3]
            user_name = vk_bot.method('users.get', {'user_ids': user_id})
            write_msg(user_id, 'Отлично, ' + (user_name[0]['first_name']))
            print(str(user_name[0]['first_name']) + ' ' + str(user_name[0]['last_name']) + ' написал(а) боту - ' + str(
                update[0][6]))
        elif update[0][6].lower() == "пока":
            user_id = update[0][3]
            write_msg(user_id, 'Пока')
            print(str(user_name[0]['first_name']) + ' ' + str(user_name[0]['last_name']) + ' написал(а) боту - ' + str(
                update[0][6]))
        elif update[0][6].lower() == 'картинка':
            user_id = update[0][3]
            send_photo(user_id, PHOTO_1)
        elif update[0][6].lower() == 'перешли':
            user_id = update[0][3]
            print(update)
            frwd_msg(user_id, update[0][1] - 2, 'держи')
        else:
            # print(update)
            user_id = update[0][3]
            write_msg(user_id, 'Нет такой команды')

    #  Меняем ts для следующего запроса
    ts = long_poll['ts']
