# -*- coding:utf-8 -*-

import urllib
import unittest


class EmployeeIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://18.181.168.225:8888/api/employee/healthCheck'

    def i_test_health(self):
        r = urllib.request.urlopen(self.url)
        self.assertEqual(200, r.status)


if __name__ == '__main__':
    unittest.main()
