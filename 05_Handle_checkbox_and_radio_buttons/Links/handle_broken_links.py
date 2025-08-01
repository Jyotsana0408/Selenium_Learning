"""

What This Script Does:
    It opens a local HTML file in Chrome using Selenium, grabs all hyperlinks (<a> tags),
    and checks each link using an HTTP HEAD request to identify whether it’s valid or broken.

Section-by-Section Explanation:

    Imports and Setup:

        import time
        import requests
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        from webdriver_manager.chrome import ChromeDriverManager

            Imports necessary modules:
            requests handles the HTTP calls.
            selenium is for browser automation.
            webdriver_manager automatically sets up the right Chrome driver.

    Initialize WebDriver:

        service_obj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service_obj)

            Automatically installs the correct version of ChromeDriver and launches Chrome.

    Load Local HTML Page:

        driver.get("E:/Jyotsna/.../broken_link.html")
        driver.maximize_window()

            Opens your test HTML page containing the links.
            Maximizes the browser window for better visibility (optional but helpful during manual debugging).

    Find All Links:

        all_links = driver.find_elements(By.TAG_NAME, 'a')

            Finds all anchor (<a>) tags in the webpage.

    Loop Through Each Link:

        for link in all_links:
            url = link.get_attribute('href')

            Extracts the href attribute (the actual URL) from each link.

    Skip Invalid URLs:

        if not url or not url.startswith(('http://', 'https://')):
            print(f"{url} ➤ Skipped (invalid or unsupported format)")
            continue

        Ignores empty or improperly formatted URLs (like htp://... or local file:// links).

    Check Link Status:

        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            status = response.status_code

        Sends a HEAD request (only fetches headers, not full content—making it faster).
        allow_redirects=True: follows redirects if the site responds with one.
        timeout=5: prevents the request from hanging too long.

    Broken vs. Valid Logic:

        if status >= 400:
            print(f"{url} Broken link → Status {status}")
            broken_count += 1
        else:
            print(f"{url} Valid link → Status {status}")

        Any link with status code 400 or higher is considered broken.
        Others are treated as valid.

    Handle Exceptions Gracefully:

        except requests.exceptions.RequestException as e:
            print(f"{url} Error checking → {e}")
            broken_count += 1

        Catches any request errors (like DNS issues, timeouts, SSL errors).
        Treats them as broken links too.

    Final Summary

        print(f"\nTotal number of broken links: {broken_count}")
        time.sleep(2)
        print("Testing complete!")
        driver.quit()

        Prints out how many broken links were found.
        Adds a short pause before closing the browser.
        Gracefully shuts down the WebDriver.
"""

import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("E:/Jyotsna/Selenium_Learning/Selenium_Learning/05_Handle_checkbox_and_radio_buttons/Links/broken_link.html")
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME, 'a')
broken_count = 0

for link in all_links:
    url = link.get_attribute('href')

    if not url or not url.startswith(('http://', 'https://')):
        print(f"{url} Skipped (invalid or unsupported format)")
        continue

    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        status = response.status_code

        if status >= 400:
            print(f"{url} Broken link → Status {status}")
            broken_count += 1
        else:
            print(f"{url} Valid link → Status {status}")
    except requests.exceptions.RequestException as e:
        print(f"{url} Error checking → {e}")
        broken_count += 1

print(f"\nTotal number of broken links: {broken_count}")

time.sleep(2)
print("Testing complete!")
driver.quit()
