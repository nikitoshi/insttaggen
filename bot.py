#!/usr/bin/python
# -*- coding: utf8 -*-

import telebot


from telebot import apihelper


# apihelper.proxy

bot = telebot.TeleBot('1016000111:AAE51h1hhfe8PvRNO4hxjx5EOPCCyogrPJQ')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()
