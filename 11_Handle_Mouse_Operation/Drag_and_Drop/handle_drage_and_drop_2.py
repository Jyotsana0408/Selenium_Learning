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

# Locate the trash bin (drop target)
trash = driver.find_element(By.ID, "trash")

# Locate the first two images in the gallery
images = driver.find_elements(By.XPATH, "//ul[@id='gallery']/li/img")[:2]

# Perform drag and drop for each image
actions = ActionChains(driver)
for img in images:
    actions.drag_and_drop(img, trash).perform()
    time.sleep(1)  # Small delay between actions

# Wait to observe result
time.sleep(3)

# Verify if two items are in the trash
dropped_items = driver.find_elements(By.XPATH, "//div[@id='trash']/ul/li")
if len(dropped_items) == 2:
    print("Successfully dragged two images to trash!")
else:
    print(f"Expected 2 items, found {len(dropped_items)}.")

# Clean up
driver.quit()
