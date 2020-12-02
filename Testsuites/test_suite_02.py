import sys

sys.path.append(".")
import unittest

from Testcases.test_login_01 import HerokuAppLogin1

# get all tests from Login class
login1 = unittest.TestLoader().loadTestsFromTestCase(HerokuAppLogin1)

# create a test suite
test_suite = unittest.TestSuite([login1])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)