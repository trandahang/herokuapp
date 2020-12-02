import logging
import TestData

from Locators.login_page_locators import LoginpageLocators
from Pages.base_page import BasePage
from TestData.test_data import Data


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        self.navigate_to(Data.BASE_URL)

    def login(self, username, password):
        self.enter_text(LoginpageLocators.INPUT_USERNAME, username)
        self.enter_text(LoginpageLocators.INPUT_PASSWORD, password)
        self.click(LoginpageLocators.BUTTON_LOGIN)

    def login_object(self, account):
        self.enter_text(LoginpageLocators.INPUT_USERNAME, account.username)
        self.enter_text(LoginpageLocators.INPUT_PASSWORD, account.password)
        self.click(LoginpageLocators.BUTTON_LOGIN)

