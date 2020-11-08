# -*- coding:utf-8 -*-

import importlib


class Config:
    config = None

    @staticmethod
    def get_config():
        return Config.config

    @staticmethod
    def set_config_env(env):
        Config.config = importlib.import_module("configuration.config_%s" % env)

