from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# _______Selectors__________

BASE_URL = 'https://www.amazon.com/'
SEARCHED_TEXT = "gifts for mom"
SEARCH_FIELD = (By.ID,"twotabsearchtextbox")
SEARCH_BUTTON = (By.XPATH, "//*[@id='nav-search-submit-button']")
PRESENT_TEXT = (By.XPATH, '//*[@class = "a-color-state a-text-bold"]')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(4)


def test_find_gift():
    driver.get(BASE_URL)
    # driver.maximize_window()
    search= WebDriverWait(driver, 3).until(EC.element_to_be_clickable(SEARCH_FIELD)).send_keys("gifts for mom")
    search_button = driver.find_element(*SEARCH_BUTTON)
    search_button.click()
    sleep(4)

    actual_text = driver.find_element(*PRESENT_TEXT).text
    assert '"gifts for mom"' == actual_text

    assert "amazon" in driver.current_url

    driver.quit()
