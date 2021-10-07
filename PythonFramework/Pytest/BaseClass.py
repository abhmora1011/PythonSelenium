import inspect
import logging


class BaseClass:
    @property
    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # file_handler object

        logger.setLevel(logging.DEBUG)  # To skip the debug level message

        return logger
