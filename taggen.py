#!/usr/bin/python
# -*- coding: utf8 -*-

import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Авторизация
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('tag-gen-0e74ede9572f.json', scope)
gc = gspread.authorize(credentials)

# Открываем таблицу и получаем все значения
wks = gc.open("tag-gen").sheet1
tag_list = wks.get_all_values()

# Генерируем тэги и удаляем лишние символы
k = input('Введите число: ')
tags = str(random.sample(tag_list, int(k)))
tags_res = tags.replace('\'', '').replace('[', '').replace(']', '')
print(tags_res)
