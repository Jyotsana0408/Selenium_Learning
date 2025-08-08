import time
import os
import glob
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set your download location
location = r"E:\Jyotsna\Selenium_Learning\Selenium_Learning\13_Handle_Download_files"

def chrome_setup():
    prefs = {
        "download.default_directory": location,
        "plugins.always_open_pdf_externally": True,  # Force download instead of preview
    }
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    return driver

# Launch browser
driver = chrome_setup()
driver.maximize_window()

# Navigate directly to the PDF file
pdf_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
driver.get(pdf_url)

# Wait for download to complete
time.sleep(5)

# Check if PDF was downloaded
pdf_files = glob.glob(os.path.join(location, "*.pdf"))
if pdf_files:
    print("PDF downloaded successfully:", pdf_files[0])
else:
    print("PDF not found in download folder.")

# Close browser
driver.quit()
