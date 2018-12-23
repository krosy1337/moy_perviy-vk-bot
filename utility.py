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