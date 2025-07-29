"""
In Selenium with Python, the back(), forward(), and refresh() methods are part of the browser navigation toolkit
they let you simulate how a user would move through their browsing history or reload a page.
Here's how they work:

driver.back():
    Purpose: Navigates to the previous page in the browser history.
    Equivalent to: Clicking the browser’s back button.
    Usage: driver.back()

driver.forward():
    Purpose: Moves forward to the next page in the browser history (after going back).
    Equivalent to: Clicking the browser’s forward button.
    Usage: driver.forward()

driver.refresh():
    Purpose: Reloads the current page.
    Equivalent to: Pressing F5 or clicking the refresh button.
    Usage: driver.refresh()

"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.com/")

driver.maximize_window()

# back method
driver.back() #Snapdeal
time.sleep(1)
# forward method
driver.forward() #Amazon
# refresh method
driver.refresh() #Amazon

print("Testing done!")
driver.quit()