#this file will login to the walmart account that hopfully has the shopping list saved.
# this file is currently being unused due to the high level of security for bot detection on the walmart side,
# manual manipulation to log in is required to confirm human.


URL= "https://www.walmart.com/account/login"



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


#from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#PATH = "C:\Program Files (x86)\chromedriver.exe"

#global driver
#driver = webdriver.Chrome(PATH)

driver.get(URL)
time.sleep(3)

#xp_sign_in = "//input[@id='ld_ui_textfield_66388']"

#this xpath changed 1/12/2023
#this xpath id #has changed again, tring new approach.

#xp_sign_in ="//input[contains(@id, 'textfield')]"
#signed_in = driver.find_element(By.XPATH, xp_sign_in)

signed_in = driver.find_element(By.NAME, "Email Address")
time.sleep(2)
signed_in.send_keys('%%%%%@gmail.com')

time.sleep(3)
#xp_continue_button=
#continue_button=driver.find_element(By.XPATH, xp_continue_button)
#continue_button.click()

#pw = "###code!"
#xp_pw= ''' '''
#pw_input =driver.find_element(By.XPATH, xp_pw)
#pw_input.send_keys(pw)

#time.sleep(1)



time.sleep(180)
