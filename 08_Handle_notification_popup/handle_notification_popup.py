import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Create ChromeOptions object to customize browser behavior
ops = webdriver.ChromeOptions()

# Disable browser notification pop-ups (e.g., "Allow notifications?")
ops.add_argument("--disable-notifications")

# Set up ChromeDriver using WebDriver Manager (auto-downloads driver)
service_obj = Service(ChromeDriverManager().install())

# Launch Chrome browser with the specified options
driver = webdriver.Chrome(service=service_obj, options=ops)

# Open the target website (this site may request location access)
driver.get("https://whatmylocation.com/")
driver.maximize_window()

# Wait for 2 seconds to observe the page behavior
time.sleep(2)

# Print confirmation message
print("Testing done!")

# Close the browser and end the session
driver.quit()
