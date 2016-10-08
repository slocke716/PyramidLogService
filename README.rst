README
======

This package is meant to be used to setup logging to the database from a pyramid application.
To include in a pyramid application you need to alter the development.ini/production.ini files.

EXAMPLE INI FILE
================

[loggers]
keys = root, myapp

[handlers]
keys = console, sqlalchemy

[formatters]
keys = generic

[logger_root]
level = INFO
handlers = console

[logger_myapp]
level = DEBUG
handlers = sqlalchemy
qualname = myapp

[handler_sqlalchemy]
class = logservice.handlers.sqlalchemy_handler.SQLAlchemyHandler
args = ()
level = NOTSET
formatter = generic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(asctime)s %(levelname)-5.5s [%(name)s][%(threadName)s] %(message)s


You will also want to create an initialize_log_db.py file in your scripts folder

EXAMPLE initialize_log_db.py
============================

import os
import sys
from logservice.scripts import initializedb

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    log = initializedb.InitializeDb(settings['sqlalchemy.url'])
    log.initialize_db()


EXAMPLE setup.py change
=======================

entry_points = """\
      [paste.app_factory]
      main=myapp:main
      [console_scripts]
      initialize_log_db = myapp.scripts.initialize_log_db:main
      """,
