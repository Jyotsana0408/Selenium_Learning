"""
locators :
    strategies used to identify and interact with elements on a web page—like buttons, text boxes, links, and more.
    They’re the backbone of any automation script because without them, Selenium wouldn’t know where to click, type, or verify.


    Locator Type	    Description

    id	                Targets elements with a unique id attribute—fastest and most reliable
    name	            Uses the name attribute—common in form fields
    className	        Locates elements by their CSS class name
    tagName	            Finds elements by their HTML tag (e.g., input, button)
    linkText	        Targets anchor (<a>) elements by their full visible text
    partialLinkText	    Matches anchor elements using partial visible text
    cssSelector	        Uses CSS syntax—very flexible for complex DOM structures
    xpath	            Uses XML path expressions—great for dynamic or nested elements
    relative locators	Introduced in Selenium 4—locates elements based on spatial relationships


These are the standard locators used in Selenium:

    Locator Type	        Example in Python
    id	                    By.ID, "username"
    name	                By.NAME, "email"
    class_name	            By.CLASS_NAME, "btn-primary"
    tag_name	            By.TAG_NAME, "input"
    link_text	            By.LINK_TEXT, "Sign Up"
    partial_link_text	    By.PARTIAL_LINK_TEXT, "Sign"
    css_selector	        By.CSS_SELECTOR, "#login input[type='text']"
    xpath	                By.XPATH, "//input[@name='password']"


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

# Using different locators
driver.find_element(By.ID, "username")
driver.find_element(By.NAME, "email")
driver.find_element(By.CLASS_NAME, "btn-primary")
driver.find_element(By.TAG_NAME, "input")
driver.find_element(By.LINK_TEXT, "Sign Up")
driver.find_element(By.PARTIAL_LINK_TEXT, "Sign")
driver.find_element(By.CSS_SELECTOR, "#login-form input[type='text']")
driver.find_element(By.XPATH, "//input[@name='password']")

driver.find_elements() :
    used to locate multiple elements on a webpage that match a given locator strategy.
    It returns a list of WebElement objects, which you can loop through or interact with individually.


Method	            Returns	                Behavior
find_element()	    Single WebElement	    Throws exception if not found
find_elements()	    List of WebElements	    Returns empty list if none found

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()

# using id
driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# using name
driver.find_element(By.NAME, "q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# using link text
driver.find_element(By.LINK_TEXT, "Register").click()

# using partial link text
driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()


driver.quit()
