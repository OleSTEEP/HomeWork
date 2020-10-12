#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import timetable
import vk_api
import random

def send(token, chat_id):
    vk = vk_api.VkApi(token = token).get_api()
    message_id = vk.messages.send(chat_id = chat_id, message = timetable.pattern, random_id = random.randint(0, 2147483647)) # Отправка сообщения и запись его ID в переменную
    try:
        vk.messages.pin(peer_id = 2000000000 + chat_id, conversation_message_id = message_id) # Закрепление сообщения
    except:
        print('You not Admin on this chat!')

if __name__ == '__main__':
    send()