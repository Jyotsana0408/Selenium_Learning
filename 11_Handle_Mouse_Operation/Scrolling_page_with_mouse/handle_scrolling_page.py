"""

JavaScript commands used in Selenium script for scrolling.
    These are executed via:
    driver.execute_script("...JavaScript code...")

JavaScript Commands Explained-

window.scrollBy(x, y):
    window.scrollBy(0, 3000)
    Purpose: Scrolls the window by a specified number of pixels.
    x: Horizontal scroll (0 means no horizontal movement)
    y: Vertical scroll (positive = down, negative = up)
    Use case: Scrolls down the page by 3000 pixels from the current position.

window.pageYOffset:
    return window.pageYOffset
    Purpose: Returns the number of pixels the document has been scrolled vertically from the top.
    Use case: Used to verify how far the page has been scrolled.

arguments[0].scrollIntoView():
    arguments[0].scrollIntoView()
    Purpose: Scrolls the page until the specified element is visible in the viewport.
    arguments[0]: Refers to the element passed from Selenium.
    Use case: Scrolls to the image of the Indian flag.

document.body.scrollHeight:
    window.scrollBy(0, document.body.scrollHeight)
    Purpose: Scrolls to the bottom of the page.
    document.body.scrollHeight: Returns the total height of the page content.
    Use case: Scrolls down by the full height of the page.

Scroll Up to Top:
    window.scrollBy(0, -document.body.scrollHeight)
    Purpose: Scrolls back up to the top of the page.
    Negative value: Moves the scroll position upward.
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

# Navigate to the demo page
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# 1) Scroll down page by pixel
driver.execute_script("window,scrollBy(0,3000)") # javascript inbuilt function
no_of_pixels_moved = driver.execute_script("return window.pageYOffset;")
time.sleep(2)
print(no_of_pixels_moved)

# 2) Scroll down page till an element is visible
flag = driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();",flag) # javascript inbuilt function
no_of_pixels_moved = driver.execute_script("return window.pageYOffset;")
time.sleep(4)
print(no_of_pixels_moved)

# 3) Scroll down page till the end
driver.execute_script("window,scrollBy(0,document.body.scrollHeight)") # javascript inbuilt function
no_of_pixels_moved = driver.execute_script("return window.pageYOffset;")
# time.sleep(4)
print(no_of_pixels_moved)

# 4) Scroll up to starting position
driver.execute_script("window,scrollBy(0,-document.body.scrollHeight)") # javascript inbuilt function
no_of_pixels_moved = driver.execute_script("return window.pageYOffset;")
time.sleep(4)
print(no_of_pixels_moved)



print("Testing done!")
driver.quit()