#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from timetables import timetables
from datetime import datetime
from homework import homework
import date

if datetime.today().weekday() == 6:   # Если сегодня воскресенье
    classes = timetbles.monday
elif datetime.today().weekday() == 0: # Если сегодня понедельник
    classes = timetables.tuesday
elif datetime.today().weekday() == 1: # Если сегодня вторник
    classes = timetables.wednesday
elif datetime.today().weekday() == 2: # Если сегодня среда
    classes = timetables.thursday
elif datetime.today().weekday() == 3: # Если сегодня четверг
    classes = timetables.friday
elif datetime.today().weekday() == 4: # Если сегодня пятница
    classes = timetables.saturday

if datetime.today().weekday() == 6:   # Если сегодня воскресенье
    homeworks = homework.monday
elif datetime.today().weekday() == 0: # Если сегодня понедельник
    homeworks = homework.tuesday
elif datetime.today().weekday() == 1: # Если сегодня вторник
    homeworks = homework.wednesday
elif datetime.today().weekday() == 2: # Если сегодня среда
    homeworks = homework.thursday
elif datetime.today().weekday() == 3: # Если сегодня четверг
    homeworks = homework.friday
elif datetime.today().weekday() == 4: # Если сегодня пятница
    homeworks = homework.saturday  

pattern = f'''{date.Date.WeakDay()}, {date.Date.Day()}.{date.Date.Mount()}:

1. {classes[0]} - {homeworks[0]}

2. {classes[1]} - {homeworks[1]}

3. {classes[2]} - {homeworks[2]}
 
4. {classes[3]} - {homeworks[3]}

5. {classes[4]} - {homeworks[4]}

6. {classes[5]} - {homeworks[5]}

7. {classes[6]} - {homeworks[6]}

8. {classes[7]} - {homeworks[7]}
'''