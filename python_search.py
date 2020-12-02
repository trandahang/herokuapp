import sys
sys.path.append(".")

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

brower = webdriver.Firefox(executable_path=r'C:\Users\USER\Desktop\herokuapp\Drivers\geckodriver.exe')
#duong dan tuyet doi
#brower = webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe') duong dan tuong doi
brower.get('http://python.org')

brower.quit()

