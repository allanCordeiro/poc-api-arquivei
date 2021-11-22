import sys
import logging
from datetime import datetime


class Logger:
    def __init__(self):
        file_timestamp = datetime.now().strftime('%Y-%m-%d')
        logging.basicConfig(filename=f'files/logs/log_{file_timestamp}.log',
                            filemode='a',
                            level=logging.INFO,
                            format='%(asctime)s ::%(levelname)s :: %(message)s',
                            force=True
                            )
        self.__logger = logging.getLogger('root')

    def log(self, msg, msg_type="error"):
        if msg_type == "error":
            self.__logger.error(msg)
        elif msg_type == "info":
            self.__logger.info(msg)
        else:
            self.__logger.info(msg)


