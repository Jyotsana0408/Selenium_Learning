"""
What Are Frames and iFrames -

    Frame: A deprecated HTML element used to divide a browser window into multiple sections.
    iFrame (Inline Frame): An HTML element (<iframe>) that embeds another HTML document inside the current one.
                           Still widely used for ads, embedded videos, login forms, etc.

    Selenium can only interact with elements in the current context, so if an element is inside an iFrame,
     you must switch to it first.

How to Switch to a Frame in Selenium -

    There are three main ways to switch to a frame:
    1. By Index - driver.switchTo().frame(0)  # Switch to the first frame
    2. By Name or ID - driver.switchTo().frame("frameName")  # Use the name or ID attribute
    3. By WebElement
        iframe = driver.findElement(By.id("iframeID"))
        driver.switchTo().frame(iframe)
    Once inside the frame, you can interact with its elements as usual.

How to Exit a Frame -

    To return to the main document:
        driver.switchTo().defaultContent()

    To go one level up (useful for nested frames):
        driver.switchTo().parentFrame()

Best Practices
    Always identify the frame before switching. Use driver.findElements(By.tagName("iframe")) to count them.
    Use unique locators (ID, name) when possible.
    Avoid using index unless necessary—it’s fragile if the page structure changes.
    For nested frames, switch step-by-step.
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
driver.maximize_window()

# switch ith iframe locator
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))

# switch with id
driver.switch_to.frame("iframeResult")

# switch with name
driver.switch_to.frame("iframeResult")

driver.switch_to.frame(0)
driver.find_element(By.LINK_TEXT,"CSS").click()

time.sleep(3)
print("Testing done!")
driver.quit()