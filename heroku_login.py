import sys

sys.path.append('.')
from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'Drivers\geckodriver.exe')

browser.get('https://the-internet.herokuapp.com/login')

txt_username = browser.find_element_by_id('username')
txt_username.send_keys('tomsmith')

txt_password = browser.find_element_by_id('password')
txt_password.send_keys('SuperSecretPassword!')

btn_login = browser.find_element_by_xpath('//button[contains(text(), Login)]')
btn_login.click()

lbl_message = browser.find_element_by_id('flash') #id= flash
msg = lbl_message.text #gan cho 1 bien

print(msg)

assert 'You logged into a secure area!' in msg #so sanh

browser.quit()

