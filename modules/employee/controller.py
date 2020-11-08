# -*- coding:utf-8 -*-
import modules.employee.service as employee_service
import common.utils
import logging


@common.utils.tracer
def get_employees(**kwargs):
    logging.info(kwargs)
    return employee_service.get_employees(kwargs)


@common.utils.tracer
def add_employees(**kwargs):
    return employee_service.add_employees(kwargs)


@common.utils.tracer
def update_employees(**kwargs):
    return employee_service.update_employees(kwargs)


@common.utils.tracer
def delete_employees(**kwargs):
    return employee_service.delete_employees(kwargs)


def dispatcher(self, action, **kwargs):
    if action == "list":
        return get_employees(**kwargs)
    if action == "add":
        return add_employees(**kwargs)
    if action == "update":
        return update_employees(**kwargs)
    if action == "delete":
        return delete_employees(**kwargs)
    if action == "healthCheck":
        return {"health": "OK"}
