"""

driver.get_screenshot_as_* methods
    used to capture screenshots of the browser during automation.
    These are incredibly useful for debugging, logging test results, or visual verification.

Screenshot Methods in Selenium WebDriver

    1. driver.get_screenshot_as_file(filename)
        Saves the screenshot to a file.
        driver.get_screenshot_as_file("screenshot.png")
        Returns: True if successful, False otherwise.
        Use case: Save screenshots during test failures or checkpoints.

    2. driver.get_screenshot_as_png()
        Returns the screenshot as a PNG image in binary format.
        image_data = driver.get_screenshot_as_png()
        with open("screenshot.png", "wb") as f:
            f.write(image_data)
        Use case: Embed screenshots in reports or send via email.

    3. driver.get_screenshot_as_base64()
        Returns the screenshot as a Base64-encoded string.
        base64_image = driver.get_screenshot_as_base64()
        Use case: Embed directly into HTML reports or logs.
            Example: Capture Screenshot on Test Failure
            try:
                driver.find_element(By.ID, "nonexistent").click()
            except Exception as e:
                driver.get_screenshot_as_file("error_screenshot.png")
                print("Screenshot saved due to error:", e)
        Tip: Save with Timestamp
            import time
            filename = f"screenshot_{int(time.time())}.png"
            driver.get_screenshot_as_file(filename)
"""

import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.save_screenshot("E://Jyotsna//Selenium_Learning//Selenium_Learning//16_Capture_screenshot_of_webpage//homepage.png")
# driver.save_screenshot(os.getcwd()+"//homepage.png")
driver.get_screenshot_as_file(os.getcwd()+"//homepage.png")

# saves screenshot in binary format
# driver.get_screenshot_as_png()
# driver.get_screenshot_as_base64()

time.sleep(3)
print("Testing done!")
driver.quit()