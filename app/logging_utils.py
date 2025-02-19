import copy
import logging
import logging.config
from typing import Union

from app import logging_config

LOGGING_PATCHED_ALREADY = False


def monkey_patch_logging_format():
    """Monkey patches the logging module format error report"""

    def print_log_record_on_error(func):
        """Monkeypatch for logging.LogRecord.getMessage

        Credits: http://stackoverflow.com/questions/2477934/
        """

        def wrap(self, *args, **kwargs):
            """Generate wrapper function for logging.LogRecord.getMessage"""
            try:
                return func(self, *args, **kwargs)
            except Exception:  # pylint: disable=broad-except
                return (
                    f"Unable to create log message with"
                    f"msg={getattr(self, "msg", "?")}, args={getattr(self, "args", "?")}"
                )

        return wrap

    # Monkeypatch the logging library for improved formatting errors
    logging.LogRecord.getMessage = print_log_record_on_error(logging.LogRecord.getMessage)


def monkey_patch_logging():
    """Monkey patches the logging module"""

    global LOGGING_PATCHED_ALREADY  # pylint: disable=global-statement
    if LOGGING_PATCHED_ALREADY:
        return True
    LOGGING_PATCHED_ALREADY = True

    monkey_patch_logging_format()

    return True


FMT_LONG = "%(asctime)s %(levelname)-8s: %(message)s  # %(filename)s:%(lineno)d %(name)s"
FMT_SHORTER = "%(asctime)s %(levelname)-8s: %(message)s"


def setup_logging(level: Union[str, int] = "INFO", fmt: str = "brief"):
    """Setup logging

    :param level: the logging level
    :param fmt: the logging format
    """
    monkey_patch_logging()

    # Deepcopy settings, apply runtime logging args
    config = copy.deepcopy(logging_config.dict_config)
    config["loggers"][""]["level"] = level
    config["handlers"]["stream"]["formatter"] = fmt

    logging.config.dictConfig(config)
