"""

Handling Authentication Popups in Selenium --->

    Browser authentication popups (like the ones asking for username and password before accessing a protected page)
    are not JavaScript alerts, so Selenium’s switch_to.alert() won’t work.

Solution 1: Embed Credentials in the URL:

    This is the simplest and most widely used method:
    driver.get("https://username:password@yourwebsite.com")

    Example:
    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    This bypasses the popup by sending credentials directly in the request.

Security Note:
    This method exposes credentials in plain text, so avoid using it in production scripts or public repositories.

Alternative Methods:

    If embedding credentials doesn’t work (some browsers block it), you can try:
    AutoIt (Windows only): External tool to handle OS-level popups.
    Selenium 4 + Chrome DevTools Protocol (CDP): Advanced method to inject headers or simulate authentication.

What Is Injection?

    Injection refers to inserting malicious or unexpected input into a system—often used in security testing.
    Common Types:
        SQL Injection: Manipulating database queries via input fields.
        Script Injection (XSS): Injecting JavaScript into web pages.
        Header Injection: Modifying HTTP headers to bypass authentication.
    In Selenium, you can simulate injection attacks by entering crafted strings into form fields
    and observing how the app responds.
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

driver.maximize_window()

time.sleep(2)
print("Testing done!")
driver.quit()
