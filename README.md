Simple Schedule Bot for Chernihiv National Technological University.

Installation guide:

1. Clone this repo;
2. pip3 install python-telegram-bot;
3. pip3 install pymysql;
4. deploy db schema from schedulebot/schedule.sql and fill it with your data
    (temporary outdated)
5. create configuration file:
```
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
```
6. Run bot using "D:\Desktop\bot> python .\schedulebot\schedule.py -c '<config_path>'"
