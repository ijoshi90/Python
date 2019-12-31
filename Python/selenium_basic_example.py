"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 31-12-2019 at 14:53
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.google.co.in")
assert "Google" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("iJoshi90 LinkedIn")
time.sleep(2)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
#driver.close()