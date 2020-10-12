#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import urllib.request

def Sync(homework_id):
    homework_file = urllib.request.urlopen(f'https://drive.google.com/uc?id={homework_id}&export=download').read()

    f = open('homework/homework.py', 'wb')
    f.write(homework_file)
    f.close()

if __name__ == '__main__':
    Sync()