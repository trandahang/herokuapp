import sys
import unittest

sys.path.append(".")

from Pages.login_page import LoginPage
from Testcases.base_test import BaseTest
from TestData.test_data import Data
from Pages.result_page import ResultPage
from Objects.account import Account

class HerokuAppLogin1(BaseTest):
    @classmethod
    def setUp(self):
        super().setUp()

    def teaDown(self):
        super().teaDown()

    def test_login_successfully(self):
        login_page = LoginPage(self.driver)
        #self.assertTrue(login_page.is_title_matches())

        account = Account(Data.USERNAME, Data.PASSWORD)

        login_page.login_object(account)

        #log_page.login(Data.USERNAME, Data.PASSWORD)
        result_page = ResultPage(self.driver)

        print(result_page.get_message())
        self.assertIn("You logged into a secure area!", result_page.get_message())



if __name__ == '__main__':
    unittest.main()
