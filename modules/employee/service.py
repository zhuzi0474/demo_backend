# -*- coding:utf-8 -*-

import logging
from configuration.config import Config
from uuid import uuid4

database = [{"id": "1", "name": "tony_wang", "address": "china", "idNo": "888999", "age": "23", "sex": "male"},
            {"id": "2", "name": "mike", "address": "usa", "idNo": "555666", "age": "30", "sex": "female"}]


def get_employees(kwargs):
    global database
    return dict(data=database)


def add_employees(kwargs):
    global database
    kwargs["id"] = str(uuid4())
    database.append(kwargs)
    return {"result": "success"}


def update_employees(kwargs):
    global database
    for e in database:
        if e["id"] == kwargs["id"]:
            database.remove(e)
            database.append(kwargs)
    return {"result": "success"}


def delete_employees(kwargs):
    global database
    database.remove(kwargs)
    return {"result": "success"}


def add(a, b):
    c = Config.get_config()
    return a+b
