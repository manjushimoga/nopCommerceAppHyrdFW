import logging
import inspect


class LogGen:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename="D:\\PythonWS\\HybridFW\\Logs\\automation.log",
                            format='%(asctime)s:  %(levelname)s:  %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        logger.setLevel(logging.INFO)
        return logger
