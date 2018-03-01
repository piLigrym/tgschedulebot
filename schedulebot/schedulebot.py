from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logger
import traceback
import functions
import datetime
from datetime import timedelta

help_text = "Используй:\n/today - просмтри расписания на сегодня\n/tomorrow - просмотор расписания на завтра\n" \
            "/current - расписание текущей недели\n/next - раписание следующей недели\n" \
            "/oddity - проверить неделю на парность\n/calls - узнать расписание звонков\n"


def start(bot, update):
    try:
        update.message.reply_text('Привет, мой юный падаван! Используй /help, что бы узнать комманды!')
    except:
        logger.log(traceback.format_exc())


def help(bot, update):
    try:
        update.message.reply_text(help_text)
    except:
        logger.log(traceback.format_exc())


def error(bot, update, error):
    try:
        logger.log('Update "%s" caused error "%s"'.format(update, error))
    except:
        logger.log(traceback.format_exc())


def today(bot, update):
    try:
        result_text = functions.get_schedule_by_date(datetime.datetime.now())
        update.message.reply_text(result_text)
    except:
        logger.log(traceback.format_exc())


def tomorrow(bot, update):
    try:
        result_text = functions.get_schedule_by_date(datetime.datetime.now() + timedelta(days=1))
        update.message.reply_text(result_text)
    except:
        logger.log(traceback.format_exc())


def current_week(bot, update):
    try:
        week_id = functions.get_week_id()
        result_list = functions.get_schedule_current_week(week_id)
        for day_text in result_list:
            bot.send_message(chat_id=update.message.chat_id, text=day_text)
    except:
        logger.log(traceback.format_exc())


def next_week(bot, update):
    try:
        week_id = functions.get_next_week_id()
        result_list = functions.get_schedule_current_week(week_id)
        for day_text in result_list:
            bot.send_message(chat_id=update.message.chat_id, text=day_text)
    except:
        logger.log(traceback.format_exc())


def oddity(bot, update):
    try:
        week_id = functions.get_next_week_id()
        if week_id == 1:
            result_text = "Неделя непарная."
        else:
            result_text = "Неделя парная."
        update.message.reply_text(result_text)
    except:
        logger.log(traceback.format_exc())


def calls(bot, update):
    try:
        result_text = "1 пара, 08:00 - 09:20, перемена 20мин\n" \
                      "2 пара, 09:40 - 11:00, перемена 25мин\n" \
                      "3 пара, 11:25 - 12:45, перемена 25мин\n" \
                      "4 пара, 13:10 - 14:30, перемена 20мин\n" \
                      "5 пара, 14:50 - 16:10, перемена 15мин\n" \
                      "6 пара, 16:25 - 17:45, перемена 15мин\n" \
                      "7 пара, 18:00 - 19:20\n"
        update.message.reply_text(result_text)
    except:
        logger.log(traceback.format_exc())


def main():
    try:
        updater = Updater("TOKEN")

        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("today", today))
        dp.add_handler(CommandHandler("tomorrow", tomorrow))
        dp.add_handler(CommandHandler("current", current_week))
        dp.add_handler(CommandHandler("next", next_week))
        dp.add_handler(CommandHandler("oddity", oddity))
        dp.add_handler(CommandHandler("calls", calls))

        dp.add_error_handler(error)
        updater.start_polling()
        updater.idle()
    except:
        logger.log(traceback.format_exc())


if __name__ == '__main__':
    main()