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
        if "прив" in upd:  # Если нам пишут привет
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
        elif update[0][1] == msg + 3:
            # print(msg + 2)
            # print(update[0][1])
            if upd == 'да'or upd == 'хочу':
                user_id = update[0][3]
                msg = update[0][1]
                send_photo(user_id, 'photo-174113882_456239136',
                           'Ты в подземелье, тебе нужно из него выбраться. Выбери один из трёх путей.')
        elif update[0][1] == msg + 2:
            slovo = upd
            print(slovo)
            if upd == 'a':
                user_id = update[0][3]
                send_photo(user_id, 'photo-174113882_456239137', 'Ты в комнате A')
            elif upd == 'b':
                user_id = update[0][3]
                write_msg(user_id, 'Ты в комнате B')
            elif upd == 'c':
                user_id = update[0][3]
                write_msg(user_id, 'Ты в комнате C')
        elif update[0][1] == msg + 4:
            if slovo == 'a':
                if upd == 'a':
                    user_id = update[0][3]
                    send_photo(user_id, 'photo-174113882_456239138', 'Ты в комнате AA')
                elif upd == 'b':
                    user_id = update[0][3]
                    send_photo(user_id, 'photo-174113882_456239139', 'Ты в комнате AB')
                elif upd == 'c':
                    user_id = update[0][3]
                    write_msg(user_id, 'Ты в комнате AC')
            elif slovo == 'b':
                if upd == 'a':
                    user_id = update[0][3]
                    write_msg(user_id, 'Ты в комнате BA')
                elif upd == 'b':
                    user_id = update[0][3]
                    write_msg(user_id, 'Ты в комнате BB')
                elif upd == 'c':
                    user_id = update[0][3]
                    write_msg(user_id, 'Ты в комнате BC')
            elif slovo == 'c':
                if upd == 'a':
                    user_id = update[0][3]
                    write_msg(user_id, 'Ты в комнате CA')
                elif upd == 'b':
                    user_id = update[0][3]
                    write_msg(user_id, 'Ты в комнате CB')
                elif upd == 'c':
                    user_id = update[0][3]
                    write_msg(user_id, 'Ты в комнате CC')
            slovo2 = upd
            print(slovo2)
        elif update[0][1] == msg + 6:
            if slovo == 'a':
                if slovo2 == 'a':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате AAA')
                    elif upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате AAB')
                    elif upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате AAC')
                elif slovo2 == 'b':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате ABA')
                    elif upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате ABB')
                    elif upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате ABC')
                elif slovo2 == 'c':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате ACA')
                    elif upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате ACB')
                    elif upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате ACC')
            elif slovo == 'b':
                if slovo2 == 'a':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BAA')
                    elif upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BAB')
                    elif upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BAC')
                elif slovo2 == 'b':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BBA')
                    elif upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BBB')
                    elif upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BBC')
                elif slovo2 == 'c':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BCA')
                    elif upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BCB')
                    elif upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате BCC')
            elif slovo == 'c':
                if slovo2 == 'a':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CAA')
                    elif upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CAB')
                    elif upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CAC')
                elif slovo2 == 'b':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CBA')
                    elif upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CBB')
                    elif upd == 'c':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CBC')
                elif slovo2 == 'c':
                    if upd == 'a':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CCA')
                    elif upd == 'b':
                        user_id = update[0][3]
                        write_msg(user_id, 'Ты в комнате CCB')
                    elif upd == 'c':
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
