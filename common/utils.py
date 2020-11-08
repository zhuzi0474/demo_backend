# -*- coding:utf-8 -*-


def format_args_get(args):
    format_args = dict()
    for k, v in args.items():
        format_args[k] = v[0].decode(encoding='utf-8')
    return format_args

