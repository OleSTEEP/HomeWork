#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from datetime import datetime
import time
import date
import os

#Options
#-----------------------------------------------------
chat_id = 'your_chat_id (int)' # ID вашей беседы ВК (Целое число)
needtime = '15:30' # Время в которое будет осуществлена синхронизация и отправлено сообщение
token = 'your_kate_mobile_tocken (https://vkhost.github.io/)' # Токен для авторизации, как Kate Mobile
homework_id = 'drive_file_id' # ID файла с домашним заданием
timetable_id = 'drive_file_id' # ID файла с расписанием
saturday = False # Считать ли субботу за учебный день?
#-----------------------------------------------------

def Sending():
    from homework import homework_sync
    from timetables import timetables_sync

    print('Synchronization with Google Drive...              ')
    
    homework_sync.Sync(homework_id)
    timetables_sync.Sync(timetable_id)
    
    import timetable
    import vk_script
    
    vk_script.send(token, chat_id)

    print('Sended timetable to VK')
    print('Waiting 1 minute...')
    time.sleep(60.0)

    os.system('cls' if os.name == 'nt' else 'clear') # Очистка консоли (Рабает как на Linux, так и на Windows)

while 0 == 0: # Вечный цикл
    timenow = str(datetime.now().strftime("%H:%M"))
    if timenow == needtime:
        if saturday == True:
            if datetime.today().weekday() == 5:
                print('Ignoring sending - tomorrow is a day off          ')
                print('Waiting 1 minute...')
                time.sleep(60.0)
            else:
            	Sending()
        else:
            if datetime.today().weekday() == 4 or datetime.today().weekday() == 5:
                print('Ignoring sending - tomorrow is a day off          ')
                print('Waiting 1 minute...')
                time.sleep(60.0)
            else:
               Sending()

    print(f'Waiting for the right time... ({datetime.now().strftime("%H:%M:%S")}) / ({needtime})                           ', end='\r')
    time.sleep(1.0)