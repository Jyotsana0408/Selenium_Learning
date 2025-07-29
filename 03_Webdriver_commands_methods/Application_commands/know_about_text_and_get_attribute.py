"""
In Selenium, both .text and .get_attribute() are used to extract information from web elements.

.text — Grabs Visible Text

    Purpose: Gets the text that’s visible to users on the webpage.
    Works With: Elements like headings, paragraphs, buttons, etc.
    Example: If you have <h1>Welcome!</h1>, .text will return "Welcome!".
    Limitation: Doesn’t work well with input fields (like <input value="hello">) because they don’t have inner text.
        element = driver.find_element(By.ID, "welcome")
        print(element.text)  # Output: Welcome!

.get_attribute("attribute_name") — Grabs HTML Attribute Values

    Purpose: Retrieves the value of a specific attribute from an element.
    Works With: Any HTML attribute like href, value, class, placeholder, etc.
    Example: If you have <input value="hello">, .get_attribute("value") will return "hello".
    Bonus: Works even if the element is hidden!
        input_field = driver.find_element(By.ID, "email")
        print(input_field.get_attribute("value"))  # Output: hello

Comparison Table: .text vs .get_attribute()

    Feature	                    .text	                                    .get_attribute("attr")

    What it returns	            Visible text between HTML tags	            Value of a specified attribute
    Visibility requirement	    Requires element to be visible	            Works even if element is hidden
    Source of data	            Uses innerText from the DOM	                Uses attribute value from HTML (attr="value")
    Common use case	            Extracting labels, headings, button text	Getting href, value, placeholder, etc.
    Whitespace handling	        Trims leading/trailing spaces	            Returns raw attribute value
    If value not found	        Returns empty string	                    Returns None (or null in Java)
    Dynamic content	            May not reflect JS-updated values	        Can reflect updated attribute values
    Example usage	            element.text	                            element.get_attribute("href")
    Works with input fields	    No (input fields have no inner text)	    Yes (use get_attribute("value"))
    Use for debugging	        Good for checking visible content	        Good for checking element properties


"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/login")
driver.maximize_window()

# emailbox
emailbox = driver.find_element(By.XPATH,"//input[@id='Email']")
emailbox.clear()
emailbox.send_keys("abc@gmail.com")
# text
print("Result of text: ",emailbox.text) # no inner text is present for an element, hence did print nothing
# get_attribute
print("Result of get_attribute: ",emailbox.get_attribute('value')) # abc@gmail.com

# Login button
button = driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
# text
print("Result of text of Login: ",button.text) # LOG IN
# get_attribute
print("Result of get_attribute of Login: ",button.get_attribute('value')) # no value attribute is present for an element, hence did not print anything
print("Result of get_attribute of Login: ",button.get_attribute('type')) # submit

time.sleep(2)
print("Testing done!")
driver.quit()