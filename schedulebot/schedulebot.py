# -*- coding: utf-8 -*-

import Logger
import traceback
import functions
import datetime
from datetime import timedelta


class ScheduleBot(object):
    ''' Class for Schedule Bot. Contains main functionality.'''

    command_list = ['start', 'help', 'today', 'tomorrow', 'current_week',
                    'next_week', 'oddity', 'rings', ]
    help_text = ("Используй:\n"
                 "/today - просмотри расписания на сегодня\n"
                 "/tomorrow - просмотр расписания на завтра\n"
                 "/current_week - расписание текущей недели\n"
                 "/next_week - расписание следующей недели\n"
                 "/oddity - проверить неделю на парность\n"
                 "/rings - узнать расписание звонков\n")

    def __init__(self, updater):
        '''Initialize bot.

           @param updater (Updater): Updater for bot.
        '''
        self.updater = updater
        self.dispatcher = self.updater.dispatcher

    def run(self):
        '''Starts listening'''
        self.updater.start_polling()
        self.updater.idle()

    def getCommandList(self):
        '''Get list of commands'''
        return self.command_list

    def getDispatcher(self):
        '''Get dispatcher'''
        return self.dispatcher

    def start(self, bot, update):
        '''Handles 'start' command'''
        try:
            update.message.reply_text('Привет, мой юный падаван! Используй \
                                       /help, что бы узнать комманды!')
        except:
            Logger.log(traceback.format_exc())

    def help(self, bot, update):
        '''Handles 'help' command. Shows help.'''
        try:
            update.message.reply_text(self.help_text)
        except:
            Logger.log(traceback.format_exc())

    def error(self, bot, update, error):
        '''Handles errors'''
        try:
            Logger.log('Update "%s" caused error "%s"'.format(update, error))
        except:
            Logger.log(traceback.format_exc())

    def today(self, bot, update):
        '''Handles 'today' command. Returns schedule for today.'''
        try:
            result_text = functions.get_schedule_by_date(datetime.datetime.now())
            update.message.reply_text(result_text)
        except:
            Logger.log(traceback.format_exc())

    def tomorrow(self, bot, update):
        '''Handles 'tomorrow' command. Returns schedule for tomorrow.'''
        try:
            result_text = functions.get_schedule_by_date(datetime.datetime.now() + timedelta(days=1))
            update.message.reply_text(result_text)
        except:
            Logger.log(traceback.format_exc())

    def current_week(self, bot, update):
        '''Handles 'current_week' command. Returns schedule for current week'''
        try:
            week_id = functions.get_week_id()
            result_list = functions.get_schedule_current_week(week_id)
            for day_text in result_list:
                bot.send_message(chat_id=update.message.chat_id, text=day_text)
        except:
            Logger.log(traceback.format_exc())

    def next_week(self, bot, update):
        '''Handles 'next_week' command. Returns schedule for next week.'''
        try:
            week_id = functions.get_next_week_id()
            result_list = functions.get_schedule_current_week(week_id)
            for day_text in result_list:
                bot.send_message(chat_id=update.message.chat_id, text=day_text)
        except:
            Logger.log(traceback.format_exc())

    def oddity(self, bot, update):
        '''Handles 'oddity' command. Returns week's oddity.'''
        try:
            week_id = functions.get_next_week_id()
            if week_id == 1:
                result_text = "Неделя непарная."
            else:
                result_text = "Неделя парная."
            update.message.reply_text(result_text)
        except:
            Logger.log(traceback.format_exc())

    def rings(self, bot, update):
        '''Handles 'rings' command. Returns rings schedule.'''
        try:
            result_text = ("1 пара, 08:00 - 09:20, перемена 20мин\n"
                           "2 пара, 09:40 - 11:00, перемена 25мин\n"
                           "3 пара, 11:25 - 12:45, перемена 25мин\n"
                           "4 пара, 13:10 - 14:30, перемена 20мин\n"
                           "5 пара, 14:50 - 16:10, перемена 15мин\n"
                           "6 пара, 16:25 - 17:45, перемена 15мин\n"
                           "7 пара, 18:00 - 19:20\n")
            update.message.reply_text(result_text)
        except:
            Logger.log(traceback.format_exc())
