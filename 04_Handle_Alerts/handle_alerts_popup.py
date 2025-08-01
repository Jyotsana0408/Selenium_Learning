"""

To handle alerts and popups in Selenium using Python, you use the switch_to.alert interface.
Here's a quick guide to the most common types and how to deal with them:

Types of Alerts in Selenium-

    Type	            Description	                                    Handling Method
    Simple Alert	    Just an OK button (e.g., “Action completed”)	alert.accept()
    Confirmation Alert	OK and Cancel buttons (e.g., “Are you sure?”)	alert.accept() or alert.dismiss()
    Prompt Alert	    Accept/Cancel + input field                 	alert.send_keys() + alert.accept()

Methods You Can Use-

    Method	            What It Does
    alert.accept()	    Clicks “OK”
    alert.dismiss()	    Clicks “Cancel”
    alert.text	        Gets the message from the alert
    alert.send_keys()	Sends input to a prompt alert

"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.maximize_window()

# opens alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(2)

alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.send_keys("welcome")
time.sleep(2)

# alert_window.accept() #close alert window by using OK button
alert_window.dismiss() #close alert window by using cancel button

time.sleep(2)
print("Testing done!")
driver.quit()