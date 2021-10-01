from flask import Flask, request

from common_utils import *
from logging_utils import log_msg

MAX_RECORDS = int(get_env_var('MAX_RECORDS', '1000'))
DEFAULT_RECORDS = int(get_env_var('DEFAULT_RECORDS', '100'))

def get_args():
    return request.args.to_dict(flat=False)

def get_body():
    return request.get_json(force=True)

def get_request_field_quietly(key):
    body = get_body()
    if not key in body:
        return None
    else:
        return body[key]

def get_multivalued_request_field_as_str(key):
    args = get_request_field_quietly(key)
    if is_empty_array(args):
        return None
    s=""
    for arg in args:
        if is_not_empty(arg):
            s="{}{}".format(s, arg)
    return s
        
def get_arg(args, key):
    args = get_args()
    if is_empty_arg(args, key) or is_empty(args[key][0]):
        return_value = None
    else:
        return_value = args[key][0]
    log_msg("DEBUG", "get_arg", "Searching with arg_key = {}, arg_value = {}".format(key, return_value))
    return return_value

def get_multivalued_arg(args, key):
    args = get_args()
    if is_empty_arg(args, key): 
        return_value = None
    else:
        return_value = args[key]
    log_msg("DEBUG", "get_multivalued_arg", "Searching with arg_key = {}, arg_value = {}".format(key, return_value))
    return return_value

def get_multivalued_arg_as_str(args, key):
    args = get_multivalued_arg(args, key)
    if is_empty_array(args):
        return None
    s=""
    for arg in args:
        if is_not_empty(arg):
            s="{}&{}={}".format(s, key, arg)
    return s

def check_mandatory_param(key):
    if is_empty_array(cast_array(get_request_field_quietly(key))):
        log_msg("ERROR", "check_mandatory_param", "bad request : missing argument = {}, body = {}".format(key, request.data))
        return {
            "status": "bad_request",
            "reason": "missing {} argument".format(key)
        }
    else:
        return {
            "status": "ok"
        }

def is_not_ok(body):
    return not "status" in body or is_false(body["status"])

def get_the_right_count(count):
    if is_bad_number(count):
        return None
    else:
        if is_empty(count):
            count = DEFAULT_RECORDS
        else:
            count = cast_int(count)
            if count > MAX_RECORDS:
                count = MAX_RECORDS
        log_msg("DEBUG", "get_the_right_count", "count = {}".format(count))
        return count
