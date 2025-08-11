"""
Selenium provides several cookie management methods that allow you to interact with browser cookies during automation.
Here's a comprehensive guide to the available cookie methods in Selenium WebDriver (Python):

Cookie Methods in Selenium:

    Method	                    Description
    get_cookies()	            Returns a list of all cookies visible to the current page.
    get_cookie(name)	        Returns a dictionary with details of the cookie with the specified name.
    add_cookie(cookie_dict)	    Adds a cookie to the current session. The cookie must be a dictionary with at least name and value.
    delete_cookie(name)	        Deletes the cookie with the specified name.
    delete_all_cookies()	    Deletes all cookies from the browser for the current domain.

Notes & Tips:

    - You can only add cookies after navigating to a domain (driver.get(url)).
    - Cookies are domain-specific—you can't add or access cookies for other domains.
    - Some cookies (like HttpOnly or Secure) may not be accessible via JavaScript or Selenium.
    - Adding cookies with expiry, path, or domain can be done like this:
            driver.add_cookie({
                "name": "my_cookie",
                "value": "123456",
                "path": "/",
                "domain": "demo.nopcommerce.com",
                "expiry": int(time.time()) + 3600  # 1 hour from now
            })

"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")

# Capture cookies from browser
cookies = driver.get_cookies()
print(len(cookies))

# Print details of all cookies created by browser
for cookie in cookies:
    # print(cookie)
    print(cookie.get('name'), ":", cookie.get('value'))

# Add new cookie to browser
driver.add_cookie({"name":"my_cookie", "value":"123456"})
cookies = driver.get_cookies()
print(len(cookies))

# Delete a specific cookie from browser
driver.delete_cookie("my_cookie")
cookies = driver.get_cookies()
print(len(cookies))

# Delete all the cookies
"""
    delete_all_cookies() does work, but the site may immediately recreate one or more cookies due to:
    -Page reloads
    -Background AJAX calls
    -Embedded scripts
"""
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))

time.sleep(3)
print("Testing done!")
driver.quit()