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

-----------------------------------------------------------------------------------------------------------------

About wait --->

In Selenium with Python, waits are essential for handling dynamic web pages where elements may take time to load.
They help prevent errors like NoSuchElementException or ElementNotInteractableException by pausing execution until
certain conditions are met.

Types of Waits in Selenium Python :

1. Implicit Wait

    Applies globally to all elements.
    Tells WebDriver to wait a fixed time before throwing an exception.

        from selenium import webdriver

        driver = webdriver.Chrome()
        driver.implicitly_wait(10)  # Waits up to 10 seconds
        driver.get("https://example.com")
        element = driver.find_element("id", "myElement")

2. Explicit Wait

    Waits for a specific condition to be true before proceeding.
    Uses WebDriverWait and expected_conditions.

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        driver = webdriver.Chrome()
        driver.get("https://example.com")

        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "myElement")))

    Common conditions include:

    presence_of_element_located
    element_to_be_clickable
    visibility_of_element_located
    alert_is_present

3. Fluent Wait (Advanced Explicit Wait)

    Allows polling intervals and exception handling.
    More flexible for unpredictable load times.

        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(driver, 30, poll_frequency=5, ignored_exceptions=[Exception])
        element = wait.until(EC.visibility_of_element_located((By.ID, "myElement")))

Pro Tips :

    Avoid mixing implicit and explicit waits—they can cause unpredictable behavior.
    Use explicit waits for elements that load asynchronously (e.g., AJAX).
    Fluent waits are great for flaky or slow-loading elements.
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

wait.until(EC.presence_of_element_located((By.NAME, "Email"))).clear()
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