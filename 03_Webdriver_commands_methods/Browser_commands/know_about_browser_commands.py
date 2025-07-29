"""
driver.close():
    Closes only the current active browser window.
    If you're working with multiple tabs or windows, only the one in focus will be closed.
    The WebDriver session remains active if other windows are still open.
    syntax - driver.close()
    Use it when - You want to close a pop-up or a specific tab without ending the entire session.

driver.quit():
    Closes all browser windows opened during the session.
    Ends the WebDriver session completely, releasing system resources.
    syntax - driver.quit()
    Use it when - You're done with the test and want to clean up everything.

Detailed Comparison:

	Feature	                    driver.close()	                            driver.quit()
1	Scope	                    Current window/tab only	                    All windows/tabs opened by WebDriver
2	Session Termination	        Session remains active	                    Session is terminated
3	Resource Cleanup	        Partial (only current window)	            Full (all resources released)
4	Use Case	                Closing pop-ups or extra tabs	            Ending the test session
5	Effect on Multiple Windows	Other windows remain open	                All windows are closed
6	Driver Object	            Still usable after execution	            Becomes invalid after execution
7	Exception Handling	        May cause issues if used on last window	    Safely ends everything
8	Performance Impact	        Minimal	                                    Frees up memory and system resources
9	Common Usage	            Mid-test cleanup	                        Final cleanup in @AfterSuite or teardown
10	Error Risk	                Higher if misused with single window	    Lower, ensures graceful exit

"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()
time.sleep(1)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(3)

print("Testing done!")

# close command
# driver.close()

# quit command
driver.quit()