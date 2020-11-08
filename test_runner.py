# -*- coding:utf-8 -*-

import unittest

discover = unittest.defaultTestLoader.discover("./unittest", pattern="test_*")
runner = unittest.TextTestRunner()
runner.run(discover)

