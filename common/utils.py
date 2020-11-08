# -*- coding:utf-8 -*-

import datetime


def format_args_get(args):
    format_args = dict()
    for k, v in args.items():
        format_args[k] = v[0].decode(encoding='utf-8')
    return format_args


def tracer(func):
    def wrapper(**kwargs):
        start_time = datetime.datetime.now()
        res = func(**kwargs)
        end_time = datetime.datetime.now()
        print((end_time - start_time).seconds)
        return res
    return wrapper
