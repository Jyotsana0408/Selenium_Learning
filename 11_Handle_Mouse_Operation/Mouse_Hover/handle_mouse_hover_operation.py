"""
Mouse Hover -

Create ActionChains Object
    actions = ActionChains(driver)
    Purpose: Initializes an ActionChains object to build a sequence of low-level interactions
             like mouse movements, clicks, key presses, etc.
    Why it's needed: Selenium doesn’t have a direct hover() method—so we simulate it using move_to_element().

Summary of Key ActionChains Methods -
    Method	                Description
    move_to_element(el)	    Moves mouse to the center of the element
    click()	                Adds a click action to the chain
    pause(seconds)	        Adds a delay between actions
    perform()	            Executes all queued actions in the chain

Difference between .click() and .perform() in Selenium's ActionChains:
    .click() vs .perform() in ActionChains
        Method	    What It Does
        .click()	Adds a click action to the action chain queue. It does not execute it.
        .perform()	Executes all the actions that have been queued in the chain.
    Think of it like this:
        .click() is like writing a step in a choreography.
        .perform() is like starting the dance.
    Example:
        actions = ActionChains(driver)
        actions.move_to_element(element).click()  # Adds hover and click to the queue
        actions.perform()                         # Executes both actions
            Without .perform(), nothing actually happens on the page.

"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://demoqa.com/menu")

# Create ActionChains and WebDriverWait
actions = ActionChains(driver)
wait = WebDriverWait(driver, 10)

# Hover over "Main Item 2"
main_item = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='nav']/li[2]/a")))
actions.move_to_element(main_item).perform()

# Hover over "SUB SUB LIST »"
sub_sub_list = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='nav']/li[2]/ul/li[3]/a")))
actions.move_to_element(sub_sub_list).perform()

time.sleep(1)
# Wait for "Sub Sub Item 2" to be visible and click it
sub_sub_item = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='nav']/li[2]/ul/li[3]/ul/li[2]/a")))
actions.move_to_element(main_item).pause(0.5).move_to_element(sub_sub_list).pause(0.5).move_to_element(sub_sub_item).click().perform()

# time.sleep(1)
# actions.move_to_element(sub_sub_item).click().perform()

print("Clicked on Sub Sub Item 2")

# Close browser
driver.quit()
