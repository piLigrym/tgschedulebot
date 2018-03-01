import db_helper
import logger
import traceback
import datetime


days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
days_ru = ["ПОНЕДЕЛЬНИК", "ВТОРНИК", "СРЕДА", "ЧЕТВЕРГ", "ПЯТНИЦА", "СУББОТА", "ВОСКРЕСЕНЬЕ"]


def get_week_id():
    week = datetime.datetime.now().isocalendar()[1]
    if week % 2 == 0:
        week_id = 1
    else:
        week_id = 2
    return week_id


def get_next_week_id():
    week = datetime.datetime.now().isocalendar()[1]
    if week % 2 == 0:
        week_id = 2
    else:
        week_id = 1
    return week_id


def get_schedule_by_date(date):
    try:
        week_day_ind = date.weekday()
        week_day = days[week_day_ind]
        week_id = get_week_id()

        result_rows = db_helper.select_by_day_week(week_id, week_day)
        result_text = ""
        for row in result_rows:
            row_text = "{} пара: {} - {}\n{}\n" \
                       "{}, {} \n" \
                       "__________________________\n" \
                .format(row['lecture_num'], str(row['lecture_begin'])[:-3], str(row['lecture_end'])[:-3],
                        row['lecture_name'], row['lecture_hall'], row['lecture_teacher'])
            result_text += row_text
        return result_text
    except:
        logger.log(traceback.format_exc())
        return None


def get_schedule_current_week(week_id):
    try:
        result_text = []
        for i in range(5):
            week_day = days[i]
            result_rows = db_helper.select_by_day_week(week_id, week_day)
            day_text = ""
            if len(result_rows) > 0:
                day_text += "{}:\n+++++++++++++++++++++++++++\n".format(days_ru[i])
            else:
                continue
            for row in result_rows:
                row_text = "{} пара: {} - {}\n{}\n" \
                           "{}, {} \n" \
                           "__________________________\n" \
                    .format(row['lecture_num'], str(row['lecture_begin'])[:-3], str(row['lecture_end'])[:-3],
                            row['lecture_name'], row['lecture_hall'], row['lecture_teacher'])
                day_text += row_text
            day_text += "+++++++++++++++++++++++++++\n"
            result_text.append(day_text)
        return result_text
    except:
        logger.log(traceback.format_exc())




