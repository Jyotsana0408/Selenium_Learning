"""

Assignment Test Case :

    Open web Browser (Chrome/Firefox/Edge)
    Open URL https://admin-demo.nopcommerce.com/login
    Provide Email (admin@yourstore.com)
    Provide password (admin)
    Click on login
    Capture title of dashboard page(Actual title)
    Verify title of the page: "Dashboard / nopCommerce administration" (Expected)
    Close browser

"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome browser
service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

# Open a webpage
driver.get("https://admin-demo.nopcommerce.com/login")

# Optional: Maximize window
driver.maximize_window()

wait = WebDriverWait(driver, 2)

wait.until(EC.presence_of_element_located((By.NAME, "Email"))).send_keys("admin@yourstore.com")
wait.until(EC.presence_of_element_located((By.NAME, "Password"))).send_keys("admin")

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()
print("Actual title:", driver.title)

wait.until(EC.title_is("nopCommerce demo store. Login"))

assert driver.title == "nopCommerce demo store. Login", f"Login failed. Title was: {driver.title}"
time.sleep(2)
print("Login successful. Title is:", driver.title)
driver.quit()