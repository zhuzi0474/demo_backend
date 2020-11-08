# -*- coding:utf-8 -*-

import unittest
import modules.employee.service as employee_service


class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.url = 1

    def test_add_employee(self):
        mockemployee = {"id": "99", "name": "mike1", "address": "usa1", "idNo": "5556661", "age": "30", "sex": "female"}
        employee_service.add_employees(mockemployee)
        ret = employee_service.get_employees(None)
        self.assertEqual(len(ret), 1)


if __name__ == '__main__':
    unittest.main()
