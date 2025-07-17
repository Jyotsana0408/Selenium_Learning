"""

Test Case :

    Open web Browser (Chrome/Firefox/Edge)
    Open URL https://opensource-demo.orangehrmlive.com/
    Enter username (Admin)
    Enter password (admin123)
    Click on login
    Capture title of home page(Actual title)
    Verify title of the page: "OrangeHRM" (Expected)
    Close browser

In selenium 4 :

    Service class :
        used to configure and manage the lifecycle of the browser driver executable.
        It wraps the path to the driver and handles how Selenium starts and stops the driver process.

Why It Was Introduced :

    In Selenium 3, you passed the driver path directly using executable_path.
    In Selenium 4, this was replaced with Service() to align with the W3C WebDriver standard and improve modularity.

This applies to all locator types:

        Old Method	                            New Method
        find_element_by_id("id")	            find_element(By.ID, "id")
        find_element_by_name("name")	        find_element(By.NAME, "name")
        find_element_by_xpath("xpath")	        find_element(By.XPATH, "xpath")
        find_element_by_css_selector("css")	    find_element(By.CSS_SELECTOR, "css")
        find_element_by_class_name("class")	    find_element(By.CLASS_NAME, "class")

driver.close() :

    What it does:
        Closes only the current browser tab or window that the WebDriver is controlling.
        If multiple tabs/windows are open, it closes just one.
    Use Case:
        When you're working with multiple windows or tabs and want to close just one of them.
    Caution:
        If it's the last open window, it will also terminate the session — but not cleanly.

driver.quit() :

    What it does:
        Closes all browser windows/tabs opened during the session.
        Ends the WebDriver session completely and shuts down the driver process.
    Use Case:
        At the end of your test case or script, when you're done with all browser interactions.

Best Practice:
    Always use driver.quit() at the end of your test to ensure:
    No background processes are left running
    System resources are released properly

Summary :
Method	        Closes	            Ends Session	 When to Use
driver.close()	Current tab/window	No	             When managing multiple tabs/windows
driver.quit()	All tabs/windows	Yes	             At the end of your test or script

Recommendation for Selenium 4:
Use driver.quit() at the end of your test to clean up properly.

"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


# Launch Chrome browser
"""
    ChromeDriverManager().install() 
        - automatically downloads the correct version of ChromeDriver for your installed Chrome browser.
    
    Service(...) 
        - wraps the path to the driver and manages its lifecycle.
        - This is passed to webdriver.Chrome() to launch the browser.
"""
service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

# Open a webpage
driver.get("https://opensource-demo.orangehrmlive.com/")

# Optional: Maximize window
driver.maximize_window()

wait = WebDriverWait(driver, 0.5)

username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username_field.send_keys("Admin")

password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password_field.send_keys("admin123")

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

# Validate title
wait.until(EC.title_is("OrangeHRM"))
time.sleep(2)
assert driver.title == "OrangeHRM", f"Title mismatch! Expected 'OrangeHRM', but got '{driver.title}'"

print("Login successful. Title is:", driver.title)

driver.quit()