
URL = "https://www.Walmart.com/"



import time
import undetected_chromedriver as webdriver
from selenium.webdriver.chrome.service import Service
# this line helps us look for elements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service('C:\Program Files (x86)\chromedriver.exe')
global driver
driver = webdriver.Chrome(service=s, use_subprocess=True)


#pulls up walmart page
#logs into walmart account ( for use of saving cart items)
#waits for home page to load
#goes to first location
#collects prices and saves to a file
#repeat for each location.
