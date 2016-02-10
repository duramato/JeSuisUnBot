import ircbot
import os
import os.path
import time
import logging
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

# some commands can be executed only if the user's nick is found in this list
owner = list(set([
    'supergonkas',
]))

owner_email = {
    'supergonkas': 'goncalo-matos@hotmail.com',
}

# server to connect to
server = config.get('network', 'server')
# server's port
port = int(config.get('network', 'port'))

# bot's nicknames
nicks = map(lambda s: s.strip('\''), config.get('network', 'nicknames').split(','))
# bot's real name
real_name = config.get('network', 'real_name')

# channels to join on startup
channels = map(lambda s: s.strip('\''), config.get('network', 'channels').split(','))

cmds = {
    # core commands list, these commands will be run in the same thread as the bot
    # and will have acces to the socket that the bot uses
    'core': list(set([
        'quit',
        'join',
        'channels',
    ])),

    # normal commands list, the ones that are accessible to any user
    'user': list(set([
        'task',
        'wikipedia',
        'wiki',
        'answer',
        'weather',
        'uptime',
        'google',
        'tvdb',
        'uptime',
        'issues',
        'issue',
        'join',
        'quit',
        'about',
        'shows',
        'hash',
        'torrent',
        'ssl',
    ])),

    # commands list that the bot will execute even if a human didn't request an
    # action
    'auto': list(set([
    ])),
}

# smtp server for email_alert
smtp_server = 'smtp.gmail.com'
smtp_port = 25
from_email_address = 'changeme@gmail.com'
from_email_password = 'p@s$w0rd'

# users should NOT modify below!
log = os.path.join(os.getcwd(), 'logs', '')
logging_level = logging.DEBUG
start_time = time.time()
current_nick = ''
