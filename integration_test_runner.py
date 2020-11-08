# -*- coding:utf-8 -*-

import unittest

discover = unittest.defaultTestLoader.discover("./integrationtest", pattern="i_test_*")
runner = unittest.TextTestRunner()
runner.run(discover)

