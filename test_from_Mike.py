from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

GMAIL_LINK = (By.XPATH, "//a[@class='gb_H' and @data-pid='23']")
EXPECTED_GMAIL_URL = "https://www.google.com/gmail/about/"
ACTUAL_GMAIL_TEXT = (By.XPATH, "//span[@class='mobile-before-hero-only']")
ANOTHER_GMAIL_TEXT_LINK = (By.XPATH, "//*[contains(text(), 'use email')]")
EXPECTED_GMAIL_TEXT = "Gmail"
GOOGLE_SEARCH_FIELD = (By.NAME, 'q')
SEARCH_BUTTON = (By.XPATH, "//input[@name='btnK']")
# we are going to give url to our driver
driver.get('https://google.com')
sleep(4)
driver.find_element(*GMAIL_LINK).click()
sleep(4)
assert EXPECTED_GMAIL_URL == driver.current_url
print(driver.find_element(*ACTUAL_GMAIL_TEXT).text)
assert driver.find_element(*ACTUAL_GMAIL_TEXT).text == EXPECTED_GMAIL_TEXT
assert driver.find_element(*ANOTHER_GMAIL_TEXT_LINK).text == "Secure, smart, and easy to use email", f"EMAIL is missing"

driver.get('https://google.com')
sleep(4)
driver.find_element(*GOOGLE_SEARCH_FIELD).send_keys("Anekdot", Keys.ENTER)
#driver.find_element(*GOOGLE_SEARCH_FIELD).click()

# search in search field
# search = driver.find_element(By.NAME, 'q')
# search.clear()
# search.send_keys('Watches')

# we are waiting for 4 seconds
sleep(4)

# select the search button
#driver.find_element(By.NAME, 'btnK').click()

# let's verify our result

#assert 'Dress' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text

# close chrome
driver.quit()

#     password = driver.find_element(By.XPATH, PASS_FIELD)
#     password.send_keys(STANDARD_PASS)