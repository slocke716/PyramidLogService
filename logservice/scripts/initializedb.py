from sqlalchemy import create_engine
from logservice import models
from logservice.models.meta import Base
from sqlalchemy.orm import sessionmaker
from logservice.handlers.sqlalchemy_handler import SQLAlchemyHandler


class InitializeDb(object):
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def initialize_db(self):
        engine = create_engine(self.connection_string)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        # create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # create a Session
        dbsession = Session()

        # http://docs.python.org/howto/logging.html#configuring-logging
        import logging

        # create logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = SQLAlchemyHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        # 'application' code
        logger.debug('Initializing Logs')
