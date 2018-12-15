import random

import requests
import vk_api
from config import *


def write_msg(user_id, text):
    vk_bot.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': random.randint(0, 1000)})


def send_photo(user_id, photo, messag):
    vk_bot.method('messages.send',
                  {'user_id': user_id, 'attachment': photo, 'message': messag, 'random_id': random.randint(0, 1000)})


def get_last_post(owner_id, count, offset, filter):
    response = vk_bot_user.method('wall.get',
                                  {'owner_id': owner_id, 'count': count, 'offset': offset, 'filter': filter})
    return response['items'][0]['id']


def write_msg_attach(user_id, text, attach):
    vk_bot.method('messages.send',
                  {'user_id': user_id, 'attachment': attach, 'message': text, 'random_id': random.randint(0, 1000)})


PHOTO_2 = 'photo324207419_456239051'
msg = -1


def frwd_msg(user_id, messag, text):
    vk_bot.method('messages.send', {'user_id': user_id, 'forward_messages': messag, 'message': text,
                                    'random_id': random.randint(0, 1000)})


vk_bot = vk_api.VkApi(token=TOKEN)
vk_bot_user = vk_api.VkApi(token=ACCESS_TOKEN)
long_poll = vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']
print("готов к работе")

# + str(long_poll))

while True:
    long_poll = requests.get(
        'https://{server}?act={act}&key={key}&ts={ts}&wait=500'.format(server=server,
                                                                       act='a_check',
                                                                       key=key,
                                                                       ts=ts)).json()
    update = long_poll['updates']
    if update[0][0] == 4:
        upd = update[0][6].lower()
        print(update)
        if "прив" in update[0][6]:  # Если нам пишут привет
            # print(update)
            user_id = update[0][3]
            msg = update[0][1]
            # print(msg)
            user_name = vk_bot.method('users.get', {'user_ids': user_id})
            # print(user_name)
            write_msg(user_id, 'Привет, ' + (user_name[0]['first_name']))  # сообщение пользователю
            write_msg(user_id, 'Хочешь начать игру? ')
            # print(str(user_name[0]['first_name']) + ' ' +
            #       str(user_name[0]['last_name']) + ' написал(а) боту - ' + str(update[0][6]))  # соообщение нам
        if update[0][1] == msg + 3:
            # print(msg + 2)
            # print(update[0][1])
            if upd == 'да':
                user_id = update[0][3]
                msg = update[0][1]
                send_photo(user_id, 'photo-174113882_456239125',
                           'Ты в подземелье, тебе нужно из него выбраться. Выбери один из трёх путей.')
        if update[0][1] == msg + 2:
            slovo = upd
            print(slovo)
            if upd == 'a':
                user_id = update[0][3]
                send_photo(user_id, 'photo-174113882_456239126', 'Ты в комнате A')
            if upd == 'b':
                user_id = update[0][3]
                write_msg(user_id, 'Ты в комнате B')
            if upd == 'c':
                user_id = update[0][3]
                write_msg(user_id, 'Ты в комнате C')
        if update[0][1] == msg + 4:
            if slovo == 'a':
                if upd == 'a':
                    user_id = update[0][3]
                    write_msg(user_id, 'Ты в комнате AA')
                if upd == 'b':
                    user_id = update[0][3]
                    write_msg(user_id, 'Ты в комнате AB')
                if upd == 'c':
                    user_id = update[0][3]
                    write_msg(user_id, 'Ты в комнате AC')
            if slovo == 'b':
                if upd == 'a':
                    user_id = update[0][3]
                    write_msg(user_id, 'Ты в комнате BA')
                if upd == 'b':
                    user_id = update[0][3]
                    write_msg(user_id, 'Ты в комнате BB')
                if upd == 'c':
                    user_id = update[0][3]
                    write_msg(user_id, 'Ты в комнате BC')
            if slovo == 'c':
                if upd == 'a':
                    user_id = update[0][3]
                    write_msg(user_id, 'Ты в комнате CA')
                if upd == 'b':
                    user_id = update[0][3]
                    write_msg(user_id, 'Ты в комнате CB')
                if upd == 'c':
                    user_id = update[0][3]
                    write_msg(user_id, 'Ты в комнате CC')
            slovo2 = upd
            print(slovo2)
        if update[0][1] == msg + 6:
            if slovo == 'a':
                if slovo2 == 'a':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате AAA')
                    if upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате AAB')
                    if upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате AAC')
                if slovo2 == 'b':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате ABA')
                    if upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате ABB')
                    if upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате ABC')
                if slovo2 == 'c':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате ACA')
                    if upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате ACB')
                    if upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате ACC')
            if slovo == 'b':
                if slovo2 == 'a':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BAA')
                    if upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BAB')
                    if upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BAC')
                if slovo2 == 'b':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BBA')
                    if upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BBB')
                    if upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BBC')
                if slovo2 == 'c':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BCA')
                    if upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BCB')
                    if upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BCC')
            if slovo == 'c':
                if slovo2 == 'a':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CAA')
                    if upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CAB')
                    if upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CAC')
                if slovo2 == 'b':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CBA')
                    if upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CBB')
                    if upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CBC')
                if slovo2 == 'c':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CCA')
                    if upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CCB')
                    if upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CCC')


        elif 'цвет' in upd:
            user_id = update[0][3]
            group_id = -27022023
            post_name = vk_bot_user.method('wall.get', {'owner_id': group_id, 'count': 1, 'offset': random.randint(0, 2,) or random.randint(4,5) , 'filter': 'owner'})
            # print(post_name['items'][0]['attachments'][0]['type'])    # photo
            # print(post_name['items'][0]['attachments'][0]) #id photo
            attach = str(post_name['items'][0]['attachments'][random.randint(0, 5)]['type']) + str(group_id) + '_' + str(post_name['items'][0]['attachments'][random.randint(0, 5)]['photo']['id'])
            # print(post_name['items'][0]['attachments'][3])
            write_msg_attach(user_id, 'вот тебе цветы', attach)

    #  Меняем ts для следующего запроса
    ts = long_poll['ts']
