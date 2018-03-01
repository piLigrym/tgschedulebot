import pymysql
import logger


HOST = ''
USER = ''
PASSWORD = ''
DATABASE = 'db_schedule'
CHARSET = 'utf8'


def init():
    return pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        db=DATABASE,
        charset=CHARSET,
        cursorclass=pymysql.cursors.DictCursor)


def insert(sql):
    try:
        connection = init()
        with connection.cursor() as cursor:
            cursor.execute(sql)
        connection.commit()
        connection.close()
        return True
    except pymysql.Error as e:
        logger.log(e)
        return False


def select_by_day_week(week_id, week_day):
    try:
        connection = init()
        cursor = connection.cursor()
        sql = """SELECT * FROM db_schedule.schedules WHERE week_id = {} AND week_day = '{}';"""\
            .format(week_id, week_day)
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    except pymysql.Error as e:
        logger.log(e)
        return None


