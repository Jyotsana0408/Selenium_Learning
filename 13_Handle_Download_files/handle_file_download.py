import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Get the current working directory to save downloaded files
location = os.getcwd()  # Example: E:\Jyotsna\Selenium_Learning\Selenium_Learning\13_Handle_Download_files

def chrome_setup():
    # Set Chrome preferences to download files automatically to the specified folder
    preferences = {
        "download.default_directory": location,  # Set download path
    }

    # Configure Chrome options with preferences
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option("prefs", preferences)

    # Initialize Chrome WebDriver with options
    from selenium.webdriver.chrome.service import Service
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    driver.implicitly_wait(10)  # Implicit wait for element loading
    return driver


# Launch browser with custom download settings
driver = chrome_setup()
driver.maximize_window()

# Navigate to the demo download page
driver.get("https://demoqa.com/upload-download")

# Click the download button to trigger file download
driver.find_element(By.ID, "downloadButton").click()

# Wait for download to complete
time.sleep(3)

print("Testing done! File should be downloaded to:", location)

# Close the browser
driver.quit()
