# -*- coding: utf-8 -*-

import sys
import io
from configparser import ConfigParser, MissingSectionHeaderError


class BotConfig(object):
    '''Contains configuration for bot'''

    voice_dir = None

    @classmethod
    def __init__(cls, path):
        '''Initialize bot.

           @param path (string): Path to configuration file.
        '''
        config = ConfigParser()
        try:
            config.read(path)
        except MissingSectionHeaderError:
            print("Can't apply configuration. There are wrong section"
                  " definition.")
            sys.exit(-1)
        try:
            cls.db_host = config['database']['db_host']
            cls.db_user = config['database']['db_user']
            cls.db_pass = config['database']['db_pass']
            cls.token = config['bot']['token']
            cls.log_dir = config['bot']['log_dir']
            cls.voice_dir = config['bot']['voice_dir']
        except KeyError:
            print("Can't apply configuration. There are missing options.")
            sys.exit(-1)


# TODO Singleton for Logger
def getLog():
    pass


# TODO Singleton for SqlManager
def getSM():
    pass
