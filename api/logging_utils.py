import sys

from datetime import datetime
from common_utils import get_env_var, is_true

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def is_error_log(log_level):
    return any(log_level.upper() == l for l in ['ERROR', 'FATAL'])

LOG_LEVEL = get_env_var('LOG_LEVEL', 'INFO').upper()

def is_log_enable(log_level):
    return LOG_LEVEL == 'DEBUG' or any(l == log_level.upper() for l in ['INFO', 'WARN', 'ERROR', 'FATAL'])

def log_msg(log_level, function_name, msg):
    log_tpl = "{} - [{}][{}] {}"
    if is_log_enable(log_level):
        msg = log_tpl.format(datetime.now().isoformat(), log_level, function_name, msg)
        if is_error_log(log_level):
            eprint(msg)
        else:
            print(msg)
