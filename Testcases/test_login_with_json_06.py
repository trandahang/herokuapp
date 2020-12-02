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

    def test_login(self):
        data = Data()
        accounts = data.get_account_json()

        for acc in accounts:
            username = acc['username']
            password = acc['password']
            message = acc['message']
            account = Account(username, password)

            login_page = LoginPage(self.driver)
            login_page.login_object(account)
            result_page = ResultPage(self.driver)
            self.assertIn(message, result_page.get_message())

if __name__ == '__main__':
    unittest.main()
