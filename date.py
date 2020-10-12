#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from datetime import datetime
import time

class Date():
    def WeakDay():
        week_day = datetime.today().weekday()
        if week_day == 6:
            week_day = 'ПОНЕДЕЛЬНИК'
        elif week_day == 0:
            week_day = 'ВТОРНИК'
        elif week_day == 1:
            week_day = 'СРЕДА'
        elif week_day == 2:
            week_day = 'ЧЕТВЕРГ'
        elif week_day == 3:
            week_day = 'ПЯТНИЦА'
        elif week_day == 4:
            week_day = 'СУББОТА'
        return week_day

    def Day():
        day = datetime.today().strftime('%d')
        day = int(day) + 1 # Добавляем к сегодняшнему числу 1 (Будет небольшая путаница с Февралём)
        return day

    def Mount():
        mount = datetime.today().strftime('%m')
        return mount