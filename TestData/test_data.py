from Utils.utils import Utility


class Data:
    BASE_URL = 'https://the-internet.herokuapp.com/login'
    USERNAME = 'tomsmith'
    FAKE_USERNAME = 'hang'
    PASSWORD = 'SuperSecretPassword!'
    FAKE_PASSWORD = 'tran'
    BROWSER = 'ff'

    ACCOUNT_CSV_FILE = './TestData/accounts.csv'
    ACCOUNT_JSON_FILE = './TestData/accounts.json' # / -> file

    def get_account_csv(self):
        utility = Utility()
        return utility.read_csv(Data.ACCOUNT_CSV_FILE)

    def get_account_json(self):
        utility = Utility()
        return utility.read_json(Data.ACCOUNT_JSON_FILE)
