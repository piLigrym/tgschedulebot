# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from ScheduleBot import ScheduleBot
from BotConfig import BotConfig
import Logger
import traceback
import functions
import datetime
import sys
import getopt
from datetime import timedelta


def addHandlers(bot):
    '''Add handlers for bot's commands'''
    for command in bot.getCommandList():
        bot.getDispatcher().add_handler(CommandHandler(command,
                                                       getattr(bot, command)))
    bot.getDispatcher().add_error_handler(bot.error)


def usage():
    '''Prints bot usage'''
    print("Schedule Bot by piLigrym and Reni Min.\n\nUsage:\n"
          "python schedule.py -c '<config_path>'\n\nOptions:\n\n"
          "-h, --help\t-\thelp\n-c, --config\t-\tPath to configuration file")


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hc:", ["help", "config="])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)
    config = None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-c", "--config"):
            config = a
        else:
            assert False, "unhandled option"
    BotConfig(config)
    bot = ScheduleBot(Updater(BotConfig.token))
    addHandlers(bot)
    try:
        bot.run()
    except:
        Logger.log(traceback.format_exc())
