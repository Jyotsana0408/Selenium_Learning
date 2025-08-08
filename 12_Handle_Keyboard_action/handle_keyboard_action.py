"""
Keyboard actions in Selenium :
    handled using the ActionChains class and the Keys class from selenium.webdriver.common.keys.
    These allow you to simulate key presses like typing, holding modifier keys (Shift, Ctrl), pressing Enter, Tab, etc.

Keys Class Reference:
    Key	                Description
    Keys.ENTER	        Enter key
    Keys.TAB	        Tab key
    Keys.ESCAPE	        Escape key
    Keys.BACKSPACE	    Backspace
    Keys.DELETE	        Delete key
    Keys.SHIFT	        Shift modifier
    Keys.CONTROL	    Ctrl modifier
    Keys.SPACE	        Spacebar
    Keys.ARROW_DOWN	    Down arrow
    Keys.ARROW_UP	    Up arrow

Common Keyboard Actions in Selenium:

1. Send Keys to an Input Field-

    From selenium.webdriver.common.keys import Keys
    element = driver.find_element(By.ID, "search")
    element.send_keys("Selenium WebDriver")
    element.send_keys(Keys.ENTER)

    Send_keys(): Types text into an input field.
    Keys.ENTER: Simulates pressing the Enter key.

2. Using ActionChains for Complex Key Sequences-

    From selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB).send_keys("Hello").send_keys(Keys.ENTER).perform()

    Sends a sequence of keys: Tab → Hello → Enter.
    Useful for navigating forms or triggering keyboard shortcuts.

3. Hold Modifier Keys (Shift, Ctrl, Alt)-

    actions.key_down(Keys.SHIFT).send_keys("selenium").key_up(Keys.SHIFT).perform()

    Types “SELENIUM” in uppercase by holding Shift.
    You can also use Keys.CONTROL, Keys.ALT, etc.

4. Keyboard Shortcuts (e.g., Ctrl+A, Ctrl+C)-

    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()  # Ctrl+A
    actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()  # Ctrl+C

    Simulates common shortcuts like select all and copy.

5. Clear and Re-type-

    element.clear()
    element.send_keys("New text")

    Clears existing input and types new text.
"""

import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Ctrl+A
# Ctrl+C
# tab
# Ctrl+V

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

# Navigate to the demo page
driver.get("https://text-compare.com/")
driver.maximize_window()

input_1 = driver.find_element(By.XPATH,"//*[@id='inputText1']")
input_2 = driver.find_element(By.XPATH,"//*[@id='inputText2']")

# Add some value in first input box
input_1.send_keys("welcome to selenium")

act = ActionChains(driver)

# input_1 -->Select Ctrl+A Select the text and release the keys
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# input_1--> Copy text Ctrl+C
# act.key_down(Keys.CONTROL)
# act.send_keys("c")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# press tab key to navigate to input_2 box
# act.send_keys(Keys.TAB)
# act.perform()

act.send_keys(Keys.TAB).perform()

# input_2--> Copy text Ctrl+C
# act.key_down(Keys.CONTROL)
# act.send_keys("v")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()


time.sleep(3)
print("Testing done!")
driver.quit()
