from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# Option 1: Using WebDriver Manager to automatically download and manage the ChromeDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Option 2: Specify the path to ChromeDriver manually
# service = ChromeService(executable_path='C:/Users/WCram/Downloads/chromedriver-win64/chromedriver.exe')
# driver = webdriver.Chrome(service=service)

# Open the URL
driver.get("https://www.google.com")
time.sleep(1)

search_box = driver.find_element(By.NAME, 'q')
search_box.click()
time.sleep(1)

search_box.send_keys('renton technical college')
time.sleep(1)

search_box.send_keys(Keys.RETURN)
time.sleep(1)

# Wait for the search results to be present
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3')))

# Find the first search result title
first_result = driver.find_element(By.CSS_SELECTOR, 'h3')
first_result.click()
time.sleep(5)
print("First search result title:", first_result.text)
# Wait for the search box to be present (example code commented out)
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, '61c55f94-94b4-851d-4409-7065c25f16a2')))

# Close the driver
driver.quit()
