import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

# Navigate to the demo page
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
driver.maximize_window()

# Switch to the iframe containing the drag-and-drop elements
iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
driver.switch_to.frame(iframe)

# Locate draggable items and drop target
img1_source = driver.find_element(By.XPATH, "//ul[@id='gallery']/li[1]/img")  # First image
target = driver.find_element(By.ID, "trash")  # Trash bin

# Perform drag and drop
actions = ActionChains(driver)
actions.drag_and_drop(img1_source, target).perform()

# Wait to observe result
time.sleep(3)

# Optional: Verify if the image was dropped
dropped_items = driver.find_elements(By.XPATH, "//div[@id='trash']/ul/li")
if dropped_items:
    print("Drag and drop successful!")
else:
    print("Drag and drop failed.")

# Clean up
driver.quit()
