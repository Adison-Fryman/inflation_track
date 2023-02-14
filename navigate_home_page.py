# this file will simply navigate back to the walmart home page
# for use when errors occur
#URL = "https://www.walmart.com/account/login"
#import time
#import undetected_chromedriver as webdriver
#from selenium.webdriver.chrome.service import Service
# this line helps us look for elements
#from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver.common.keys import keys
s = Service('C:\Program Files (x86)\chromedriver.exe')

# This line makes my browser compatible with selenium.
driver = webdriver.Chrome(service=s, use_subprocess=True)


def go_home():
    print(__name__)
    xp_homepage = "//i[contains(@class, 'ld ld-Spark')]"
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xp_homepage)))
    finally:
        element.click()


if __name__ == '__main__':

    driver.get(URL)
    URL = "https://www.walmart.com/account/login"
    time.sleep(30)
    print('hurry up')
    time.sleep(5)
    xp_homepage = "//i[contains(@class, 'ld ld-Spark')]"
    # "//a[contains(@aria-label, 'Walmart Homepage')]" wanted to use this but its not intractable
    xp_homepage_link_id = "//a[contains(@link-identifier, 'Desktop')]"
    home_button = driver.find_element(By.XPATH, xp_homepage)
    home_button.click()
    print('it worked!')
    time.sleep(4)
    print('this was run on navigate_home_page as a test')
