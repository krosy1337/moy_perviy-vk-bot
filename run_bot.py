import random

import requests
import vk_api
from utility import *
from config import *

print("готов к работе")

# + str(long_poll))

while True:
    try:
        long_poll = requests.get(
            'https://{server}?act={act}&key={key}&ts={ts}&wait=500'.format(server=server,
                                                                            act ='a_check',
                                                                            key =key,
                                                                            ts =ts)).json()
        update = long_poll['updates']
        if update[0][0] == 4:
            upd = update[0][6].lower()
            if "прив" in upd:  # Если нам пишут привет
                user_id = update[0][3]
                msg = update[0][1]
                user_name = vk_bot.method('users.get', {'user_ids': user_id})
                write_msg(user_id, 'Привет, ' + (user_name[0]['first_name']))  # сообщение пользователю
                write_msg(user_id, 'Хочешь начать игру? ')
            elif update[0][1] == msg + 3:
                if upd == 'да' or upd == 'хочу':
                    user_id = update[0][3]
                    msg = update[0][1]
                    send_photo(user_id, 'photo-174113882_456239136',
                               'Ты в подземелье, тебе нужно из него выбраться. Выбери один из трёх путей.')
                elif upd == 'нет' or upd == 'не хочу':
                    write_msg(user_id, 'Хорошо, когда захочешь начать игру напиши мне "привет"')
            elif update[0][1] == msg + 2:
                slovo = upd
                print(slovo)
                if upd == 'a':
                    user_id = update[0][3]
                    send_photo(user_id, 'photo-174113882_456239137', 'Ты в комнате A')
                elif upd == 'b':
                    user_id = update[0][3]
                    send_photo(user_id, 'photo-174113882_456239149', 'Ты в комнате B')
                elif upd == 'c':
                    user_id = update[0][3]
                    send_photo(user_id, 'photo-174113882_456239153', 'Ты в комнате C')
                msg1 = update[0][1]
            elif update[0][1] == msg1 + 2:
                if slovo == 'a':
                    if upd == 'a':
                        user_id = update[0][3]
                        send_photo(user_id, 'photo-174113882_456239138', 'Ты в комнате AA')
                    elif upd == 'b':
                        user_id = update[0][3]
                        send_photo(user_id, 'photo-174113882_456239139', 'Ты в комнате AB')
                    elif upd == 'c':
                        user_id = update[0][3]
                        send_photo(user_id, 'photo-174113882_456239147', 'Ты в комнате AC')
                elif slovo == 'b':
                    if upd == 'a':
                        user_id = update[0][3]
                        send_photo(user_id, 'photo-174113882_456239150', 'Ты в комнате BA')
                    elif upd == 'b':
                        user_id = update[0][3]
                        send_photo(user_id, 'photo-174113882_456239151', 'Ты в комнате BB')
                    elif upd == 'c':
                        user_id = update[0][3]
                        send_photo(user_id, 'photo-174113882_456239152', 'Ты в комнате BC')
                elif slovo == 'c':
                    if upd == 'a':
                        user_id = update[0][3]
                        send_photo(user_id, 'photo-174113882_456239156', 'Ты в комнате CA')
                    elif upd == 'b':
                        user_id = update[0][3]
                        send_photo(user_id, 'photo-174113882_456239155', 'Ты в комнате CB')
                    elif upd == 'c':
                        user_id = update[0][3]
                        send_photo(user_id, 'photo-174113882_456239154', 'Ты в комнате CC')
                if upd == 'назад':
                    user_id = update[0][3]
                    send_photo(user_id, 'photo-174113882_456239136',
                               'Ты в подземелье, тебе нужно из него выбраться. Выбери один из трёх путей.')
                    msg = update[0][1]
                msg2 = update[0][1]
                slovo2 = upd
                print(slovo2)
                # print(slovo2)
            elif update[0][1] == msg2 + 2:
                if slovo == 'a':
                    if upd == 'назад':
                        user_id = update[0][3]
                        send_photo(user_id, 'photo-174113882_456239137', 'Ты в комнате A')
                        msg1 = update[0][1]
                    if slovo2 == 'a':
                        if upd == 'a':
                            user_id = update[0][3]
                            send_photo(user_id, 'photo-174113882_456239157', 'Ты в комнате AAA')
                        elif upd == 'b':
                            user_id = update[0][3]
                            send_photo(user_id, 'photo-174113882_456239159', 'Ты в комнате AAB')
                        elif upd == 'c':
                            user_id = update[0][3]
                            send_photo(user_id, 'photo-174113882_456239158', 'Ты в комнате AAC')
                    elif slovo2 == 'b':
                        if upd == 'a':
                            user_id = update[0][3]
                            send_photo(user_id, 'photo-174113882_456239161', 'Ты в комнате ABA')
                            slovo3 = upd
                        elif upd == 'b':
                            user_id = update[0][3]
                            send_photo(user_id, 'photo-174113882_456239162','Ты в комнате ABB')
                            slovo3 = upd
                        elif upd == 'c':
                            user_id = update[0][3]
                            send_photo(user_id, 'photo-174113882_456239160', 'Ты в комнате ABC.Молодец, ты нашёл выход!!!')
                            slovo3 = upd
                elif slovo == 'b':
                    if upd == 'назад':
                        user_id = update[0][3]
                        send_photo(user_id, 'photo-174113882_456239149', 'Ты в комнате B')
                        msg1 = update[0][1]
                    if slovo2 == 'a':
                        if upd == 'a':
                            user_id = update[0][3]
                            send_photo(user_id, 'photo-174113882_456239163', 'Ты в комнате BAA')
                        elif upd == 'b':
                            user_id = update[0][3]
                            send_photo(user_id, 'photo-174113882_456239162', 'Ты в комнате BAB')
                        elif upd == 'c':
                            user_id = update[0][3]
                            send_photo(user_id, 'photo-174113882_456239161', 'Ты в комнате BAC')
                    elif slovo2 == 'b':
                        if upd == 'a':
                            user_id = update[0][3]
                            send_photo(user_id, 'photo-174113882_456239158', 'Ты в комнате BBA')
                        elif upd == 'b':
                            user_id = update[0][3]
                            send_photo(user_id, 'photo-174113882_456239159', 'Ты в комнате BBB')
                        elif upd == 'c':
                            user_id = update[0][3]
                            send_photo(user_id, 'photo-174113882_456239161', 'Ты в комнате BBC')
                    elif slovo2 == 'c':
                        if upd == 'a':
                            user_id = update[0][3]
                            send_photo(user_id, 'photo-174113882_456239159', 'Ты в комнате BCA')
                        elif upd == 'b':
                            user_id = update[0][3]
                            send_photo(user_id, 'photo-174113882_456239164', 'Ты в комнате BCB')
                        elif upd == 'c':
                            user_id = update[0][3]
                            send_photo(user_id, 'photo-174113882_456239161', 'Ты в комнате BCC')
                elif slovo == 'c':
                    if upd == 'назад':
                        send_photo(user_id, 'photo-174113882_456239153', 'Ты в комнате C')
                        msg1 = update[0][1]
                    if slovo2 == 'a':
                        if upd == 'a':
                            send_photo(user_id,'photo-174113882_456239158', 'Ты в комнате CAA')
                        elif upd == 'b':
                            send_photo(user_id,'photo-174113882_456239159', 'Ты в комнате CAB')
                        elif upd == 'c':
                            send_photo(user_id, 'photo-174113882_456239161', 'Ты в комнате CAC')
                    elif slovo2 == 'b':
                        if upd == 'a':
                            send_photo(user_id,'photo-174113882_456239161', 'Ты в комнате CBA')
                        elif upd == 'b':
                            send_photo(user_id, 'photo-174113882_456239162', 'Ты в комнате CBB')
                        elif upd == 'c':
                            send_photo(user_id, 'photo-174113882_456239158', 'Ты в комнате CBC')
                msg3 = update[0][1]
            elif update[0][1] == msg3 + 2:
                if upd == 'назад':
                    if slovo == 'a':
                        if slovo2 == 'a':
                                send_photo(user_id, 'photo-174113882_456239138', 'Ты в комнате AA')
                        elif slovo2 == 'b':
                            if slovo3 == 'a'or slovo3 =='b':
                                send_photo(user_id, 'photo-174113882_456239139', 'Ты в комнате AB')
                                if slovo3 == 'c':
                                    send_photo(user_id,'','ТЫ вышел из одземелья, назад нельзя)')
                    elif slovo == 'b':
                        if slovo2 == 'a':
                            send_photo(user_id, 'photo-174113882_456239150', 'Ты в комнате BA')
                        elif slovo2 == 'b':
                            send_photo(user_id, 'photo-174113882_456239151', 'Ты в комнате BB')
                        elif slovo2 == 'c':
                            send_photo(user_id, 'photo-174113882_456239152', 'Ты в комнате BC')
                    elif slovo == 'c':
                        if slovo2 == 'a':
                            send_photo(user_id, 'photo-174113882_456239156', 'Ты в комнате CA')
                        elif slovo2 == 'b':
                            send_photo(user_id, 'photo-174113882_456239155', 'Ты в комнате CB')
                msg2 = update[0][1]
            elif 'цвет' in upd:
                user_id = update[0][3]
                group_id = -27022023
                post_name = vk_bot_user.method('wall.get', {'owner_id': group_id, 'count': 1, 'offset': random.randint(0, 2,) or random.randint(4,5) , 'filter': 'owner'})
                # print(post_name['items'][0]['attachments'][0]['type'])    # photo
                # print(post_name['items'][0]['attachments'][0]) #id photo
                attach = str(post_name['items'][0]['attachments'][random.randint(0, 5)]['type']) + str(group_id) + '_' + str(post_name['items'][0]['attachments'][random.randint(0, 5)]['photo']['id'])
                # print(post_name['items'][0]['attachments'][3])
                write_msg_attach(user_id, 'вот тебе цветы', attach)
    except KeyError:
        long_poll = vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
        key = long_poll['key']
    ts = long_poll['ts']
