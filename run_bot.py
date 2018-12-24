import requests
from utility import *

def masaga(slovko, user_id, photo, messag, user_idb , photob, messagb, user_idc, photoc, messagc):
    if slovo == slovko:
        if upd == 'a':
            vk_bot.method('messages.send',
                            {'user_id': user_id, 'attachment': photo, 'message': messag,
                            'random_id': random.randint(0, 1000)})
        elif upd == 'b':
                vk_bot.method('messages.send',
                            {'user_id': user_idb, 'attachment': photob, 'message': messagb,
                            'random_id': random.randint(0, 1000)})
        elif upd == 'c':
                vk_bot.method('messages.send',
                            {'user_id': user_idc, 'attachment': photoc, 'message': messagc,
                            'random_id': random.randint(0, 1000)})

def masags(hah, user_id, photos, messags,keyboard, user_idb, photosb, messagsb, keyboardb,user_idc,photosc, messagsc, keyboardc):
    if slovo2 == hah:
        if upd == 'a':
            send_photo_key(user_id,photos, messags, keyboard)
        elif upd == 'b':
            send_photo_key(user_idb,photosb, messagsb, keyboardb)
        elif upd == 'c':
            send_photo_key(user_idc,photosc, messagsc, keyboardc)



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
            user_id = update[0][3]
            ind = update[0][1]
            upd = update[0][6].lower()
            if "прив" in upd:  # Если нам пишут привет
                user_id = update[0][3]
                msg = ind
                user_name = vk_bot.method('users.get', {'user_ids': user_id})
                write_msg(user_id, 'Привет, ' + (user_name[0]['first_name']))  # сообщение пользователю
                write_msg(user_id, 'Хочешь начать игру? ')
            elif ind == msg + 3:
                if upd == 'да' or upd == 'хочу':
                    msg = ind
                    send_photo_key(user_id, 'photo-174113882_456239136',
                               'Ты в подземелье, тебе нужно из него выбраться. Выбери один из трёх путей.',keyboard)
                elif upd == 'нет' or upd == 'не хочу':
                    write_msg(user_id, 'Хорошо, когда захочешь начать игру напиши мне "привет"')
            elif ind == msg + 2:
                slovo = upd
                slovo2 = -1
                print(slovo)
                if upd == 'a':
                    send_photo(user_id, 'photo-174113882_456239137', 'Ты в комнате A')
                elif upd == 'b':
                    send_photo(user_id, 'photo-174113882_456239149', 'Ты в комнате B')
                elif upd == 'c':
                    send_photo(user_id, 'photo-174113882_456239153', 'Ты в комнате C')
                msg1 = update[0][1]
            elif ind == msg1 + 2:
                masaga('a', user_id, 'photo-174113882_456239138', 'Ты в комнате AA',
                       user_id, 'photo-174113882_456239139', 'Ты в комнате AB',
                       user_id, 'photo-174113882_456239147', 'Ты в комнате AC')
                masaga('b', user_id, 'photo-174113882_456239150', 'Ты в комнате BA',
                       user_id, 'photo-174113882_456239151', 'Ты в комнате BB',
                       user_id, 'photo-174113882_456239152', 'Ты в комнате BC')
                masaga('c', user_id, 'photo-174113882_456239156', 'Ты в комнате CA',
                       user_id, 'photo-174113882_456239155', 'Ты в комнате CB',
                       user_id, 'photo-174113882_456239154', 'Ты в комнате CC')
                if upd == 'назад':
                    send_photo(user_id, 'photo-174113882_456239136',
                               'Ты в подземелье, тебе нужно из него выбраться. Выбери один из трёх путей.')
                    msg = update[0][1]
                msg2 = update[0][1]
                slovo2 = upd
                print(slovo2)
            elif ind == msg2 + 2:
                if upd == 'назад':
                    if slovo == 'a':
                        send_photo(user_id, 'photo-174113882_456239137', 'Ты в комнате A')
                    if slovo == 'b':
                        send_photo(user_id, 'photo-174113882_456239149', 'Ты в комнате B')
                    if slovo == 'c':
                        send_photo(user_id, 'photo-174113882_456239153', 'Ты в комнате C')
                    msg1 = ind
                if slovo == 'a':
                    masags('a', user_id, 'photo-174113882_456239157', 'Ты в комнате AAA', keyboard,
                           user_id, 'photo-174113882_456239159', 'Ты в комнате AAB', keyboard,
                           user_id, 'photo-174113882_456239158', 'Ты в комнате AAC', keyboard)
                    masags('b', user_id, 'photo-174113882_456239161', 'Ты в комнате ABA', keyboard,
                           user_id, 'photo-174113882_456239162', 'Ты в комнате ABB', keyboard,
                           user_id, 'photo-174113882_456239160', 'Ты в комнате ABC.Молодец, ты нашёл выход!!!', endkey)
                elif slovo == 'b':
                    masags('a',user_id, 'photo-174113882_456239163', 'Ты в комнате BAA', keyboard,
                           user_id, 'photo-174113882_456239162', 'Ты в комнате BAB', keyboard,
                           user_id, 'photo-174113882_456239161', 'Ты в комнате BAC', keyboard)
                    masags('b',user_id, 'photo-174113882_456239158', 'Ты в комнате BBA', keyboard,
                           user_id, 'photo-174113882_456239159', 'Ты в комнате BBB', keyboard,
                           user_id, 'photo-174113882_456239161', 'Ты в комнате BBC', keyboard)
                    masags('c',user_id, 'photo-174113882_456239159', 'Ты в комнате BCA', keyboard,
                           user_id, 'photo-174113882_456239164', 'Ты в комнате BCB', keyboard,
                           user_id, 'photo-174113882_456239161', 'Ты в комнате BCC', keyboard)
                elif slovo == 'c':
                    masags('a',user_id,'photo-174113882_456239158', 'Ты в комнате CAA', keyboard,
                           user_id, 'photo-174113882_456239159', 'Ты в комнате CAB', keyboard,
                           user_id, 'photo-174113882_456239161', 'Ты в комнате CAC', keyboard)
                    masags('b',user_id,'photo-174113882_456239161', 'Ты в комнате CBA', keyboard,
                           user_id, 'photo-174113882_456239162', 'Ты в комнате CBB', keyboard,
                           user_id, 'photo-174113882_456239158', 'Ты в комнате CBC', keyboard)
                slovo3 = upd
                print(upd)
                msg3 = ind
            elif ind == msg3 + 2:
                if upd == 'назад':
                    if slovo == 'a':
                        if slovo2 == 'a':
                                send_photo(user_id, 'photo-174113882_456239138', 'Ты в комнате AA')
                        elif slovo2 == 'b':
                            if slovo3 == 'a' or slovo3 == 'b':
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
                    msg2 = ind




            elif 'цвет' in upd:
                group_id = -27022023
                post_name = vk_bot_user.method('wall.get', {'owner_id': group_id, 'count': 1, 'offset': random.randint(0, 2,) or random.randint(4,5) , 'filter': 'owner'})
                # print(post_name['items'][0]['attachments'][0]['type'])    # photo
                # print(post_name['items'][0]['attachments'][0]) #id photo
                attach = str(post_name['items'][0]['attachments'][random.randint(0, 5)]['type']) + str(group_id) + '_' + str(post_name['items'][0]['attachments'][random.randint(0, 5)]['photo']['id'])
                # print(post_name['items'][0]['attachments'][3])
                write_msg_attach(user_id, 'вот тебе цветы', attach)
            if 'конец' in upd:
                send_photo_key(user_id, '', 'Игра закончена.',
                               endkey)
            if 'цвет' in upd:
                group_id = -27022023
                post_id = get_last_post(group_id,1,1,'owner')
                attach = 'wall' + str(group_id) + '_' + str(post_id)
                write_msg_attach(user_id, '', attach)

    except KeyError:
        long_poll = vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
        key = long_poll['key']
    ts = long_poll['ts']
