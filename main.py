from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initiating the  Webdriver
chrome_options = Options()
service = Service('/path/to/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get('https://practicetestautomation.com/practice-test-login')
    # Entering valid credentials
    username = driver.find_element(By.ID, 'Username')
    password = driver.find_element(By.ID, 'Password')

    username.send_keys('your_username')  #Replace with a valid username
    password.send_keys('your_password')  #Replace with a valid password
    password.send_keys(Keys.RETURN)  #Submit the login form

    # Verifying the user has logged in successfully
    wait = WebDriverWait(driver, 10)
    success = wait.until(EC.success_located((By.ID, 'welcome-message')))
    assert success.is_displayed(), "Login failed."
    print("Login test passed.")

except Exception as a:
    print(f"Login test failed: {a}")

finally:
    # Closing the browser
    driver.quit()
