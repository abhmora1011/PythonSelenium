import logging


def test_loggingDemo():

    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler) # filehandler object

    logger.setLevel(logging.DEBUG)   # To skip the debug level message

    logger.debug("A debug statement is executed")

    logger.info("Information statement is executed")

    logger.warning("Something is in warning mode")

    logger.error("A major error has been occurred")

    logger.critical("Critical issue found!")

