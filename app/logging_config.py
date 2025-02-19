dict_config = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "brief": {
            "format": "%(asctime)s %(levelname)-8s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "verbose": {
            "format": "%(asctime)s %(levelname)-8s: %(message)s  # %(filename)s:%(lineno)d %(name)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "stream": {
            "level": "DEBUG",
            "formatter": "brief",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "": {
            "handlers": ["stream"],
            "level": "DEBUG",
        },
        "uvicorn.error": {
            "level": "DEBUG",
            "handlers": ["stream"],
            "propagate": False,
        },
        "uvicorn.access": {
            "level": "DEBUG",
            "handlers": ["stream"],
            "propagate": False,
        },
    },
}
