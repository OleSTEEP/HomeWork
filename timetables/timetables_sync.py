#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import urllib.request

def Sync(timetable_id):
    timetable_file = urllib.request.urlopen(f'https://drive.google.com/uc?id={timetable_id}&export=download').read()

    f = open('timetables/timetables.py', 'wb')
    f.write(timetable_file)
    f.close()

if __name__ == '__main__':
    Sync()