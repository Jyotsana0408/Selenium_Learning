import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Path to the file to be uploaded
file_to_upload = os.path.join(os.getcwd(), "test_file.txt") #before running create test_file.txt in current folder

def chrome_setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    return driver

# Launch browser
driver = chrome_setup()
driver.maximize_window()

# Navigate to upload page
driver.get("https://demoqa.com/upload-download")

# Upload the file
upload_input = driver.find_element(By.ID, "uploadFile")
upload_input.send_keys(file_to_upload)

# Wait for upload to reflect
time.sleep(2)

# Verify upload success
uploaded_text = driver.find_element(By.ID, "uploadedFilePath").text
if os.path.basename(file_to_upload) in uploaded_text:
    print("File uploaded successfully:", uploaded_text)
else:
    print("File upload failed.")

driver.quit()
