import logging
import functools


def _generate_log(path):
    """
    Create a logger object
    :param path: Path of the log file.
    :return: Logger object.
    """
    # Create a logger and set the level.
    logger = logging.getLogger('LogError')
    logger.setLevel(logging.ERROR)

    file_handler = logging.FileHandler(path)

    log_format = '%(levelname)s %(asctime)s %(message)s'
    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger


def log_error(path='./log.error.txt', user_msg=None):
    """에러 메세지 로깅을 위한 함수"""
    def error_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger = _generate_log(path)
                error_msg = 'Error has occurred at /' + func.__name__ + '\n'
                logger.exception("[ERROR] "+user_msg + ";" + error_msg)
                return e
        return wrapper
    return error_log
