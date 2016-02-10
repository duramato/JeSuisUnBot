import ircbot
import os
import os.path
import time
import logging
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

owner = list(set([
    'ownernick',
]))

owner_email = {
    'owner': 'owneremail',
}


server = config.get('network', 'server')

port = int(config.get('network', 'port'))

nicks = map(lambda s: s.strip('\''), config.get('network', 'nicknames').split(','))

real_name = config.get('network', 'real_name')

channels = map(lambda s: s.strip('\''), config.get('network', 'channels').split(','))

cmds = {

    'core': list(set([
        'quit',
        'join',
        'channels',
    ])),

    'user': list(set([
        'plugin1',
        'plugin2',
        'plugin3',
    ])),


    'auto': list(set([
    ])),
}

smtp_server = 'server'
smtp_port = port
from_email_address = 'adress'
from_email_password = 'pass'

log = os.path.join(os.getcwd(), 'logs', '')
logging_level = logging.DEBUG
start_time = time.time()
current_nick = ''
