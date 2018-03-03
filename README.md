Simple Schedule Bot for Chernihiv National Technological University.

Installation guide:
0. Clone this repo;
1. pip3 install python-telegram-bot;
2. pip3 install pymysql;
3. deploy db schema from schedulebot/schedule.sql and fill it with your data
    (temporary outdated)
4. create configuration file:
---------------------------------------------------------------------
# Information about database
[database]
db_host=
db_user=
db_pass=

[bot]
# Token for bot
token=
# Directory for logs (would be better to write full path)
log_dir=/var/log/
# Directory with base voice samples (leave empty to disable feature)
voice_dir=path/voice_samples/base/
----------------------------------------------------------------------
5. Run bot using "D:\Desktop\bot> python .\schedulebot\schedule.py -c '<config_path>'"
