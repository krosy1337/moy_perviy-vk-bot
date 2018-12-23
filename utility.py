import json
import random

import vk_api
from config import *
vk_bot = vk_api.VkApi(token=TOKEN)
vk_bot_user = vk_api.VkApi(token=ACCESS_TOKEN)
long_poll = vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']

msg = -1
msg1 = -15
msg2 = -5
msg3 = -6

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

keyboard = {
    "one_time": False,
    "buttons": [

    [get_button(label="A", color="positive")],
    [get_button(label="B", color="negative")],
    [get_button(label="C", color="primary")],
    [get_button(label="Назад", color="default")]

    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))


endkey = {
    "one_time": False,
    "buttons": []}

endkey = json.dumps(endkey, ensure_ascii=False).encode('utf-8')
endkey = str(endkey.decode('utf-8'))

def send_photo_key(user_id, photo, messag, keyb):
    vk_bot.method('messages.send',
                  {'user_id': user_id, 'attachment': photo, 'message': messag, 'keyboard':keyb, 'random_id': random.randint(0, 1000)})




def write_msg(user_id, text):
    vk_bot.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': random.randint(0, 1000)})


def send_photo(user_id, photo, messag):
    vk_bot.method('messages.send',
                  {'user_id': user_id, 'attachment': photo, 'message': messag, 'random_id': random.randint(0, 1000)})


# def get_last_post(owner_id, count, offset, filter):
#     response = vk_bot_user.method('wall.get',
#                                   {'owner_id': owner_id, 'count': count, 'offset': offset, 'filter': filter})
#     return response['items'][0]['id']


def write_msg_attach(user_id, text, attach):
    vk_bot.method('messages.send',
                  {'user_id': user_id, 'attachment': attach, 'message': text, 'random_id': random.randint(0, 1000)})
# def frwd_msg(user_id, messag, text):
#     vk_bot.method('messages.send', {'user_id': user_id, 'forward_messages': messag, 'message': text,
#                                     'random_id': random.randint(0, 1000)})