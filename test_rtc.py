import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    # Setup Chrome driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    # Teardown
    driver.quit()

def test_google_search(driver):
    # Open Google
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, 'q')
    search_box.click()
    search_box.send_keys('renton technical college')
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the results
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3')))
    
    # Verify the first result
    first_result = driver.find_element(By.CSS_SELECTOR, 'h3')
    assert 'Renton Technical College' in first_result.text, "The first result does not contain the expected text."
