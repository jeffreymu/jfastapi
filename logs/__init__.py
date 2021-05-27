import logging
from logging import handlers

sys_log = logging.getLogger('algo_demo_app_logger')
sys_log.setLevel(level=logging.DEBUG)


def log_init():
    sys_log.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter(
        'Process ID:%(process)d - '
        'Thread ID:%(thread)d- '
        'Log Time:%(asctime)s - '
        'Path:%(pathname)s:%(lineno)d - '
        'Log level:%(levelname)s - '
        'Log message:%(message)s'
    )
    sys_log.handlers.clear()
    file_handler = handlers.TimedRotatingFileHandler('algo_demo_app_logs.log', encoding='utf-8', when='W6')
    file_handler.setLevel(level=logging.INFO)
    file_handler.setFormatter(formatter)
    sys_log.addHandler(file_handler)
