#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import time

class Date():
    def WeakDay():
        from datetime import datetime
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
        import datetime
        day = datetime.datetime.today() + datetime.timedelta(days = 1)
        day = day.strftime('%d')
        return day

    def Mount():
        from datetime import datetime
        mount = datetime.today().strftime('%m')
        return mount
