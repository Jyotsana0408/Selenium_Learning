"""
CSS selectors :

    one of the most powerful and flexible locator strategies in Selenium.
    They allow you to target elements based on their attributes, hierarchy, and even partial matches
    making them ideal for dynamic or complex web pages.

Common CSS Selector Patterns :

    Selector Type	    Syntax Example	            Description
    ID	                #login	                    Selects element with id="login"
    Class	            .btn-primary	            Selects element with class="btn-primary"
    Tag	                input	                    Selects all <input> elements
    Attribute	        input[name='email']	        Selects <input> with name="email"
    Tag + Class	        button.submit-btn	        Selects <button> with class submit-btn
    Tag + ID	        div#container	            Selects <div> with id="container"
    Descendant	        div p	                    Selects <p> inside <div>
    Child	            ul > li	                    Selects direct <li> children of <ul>
    Sibling (adjacent)	h1 + p	                    Selects <p> immediately after <h1>
    Substring match	    input[name*='user']	        Contains "user" in name
    Starts with	        input[id^='login']	        id starts with "login"
    Ends with	        img[src$='.jpg']	       ends with .jpg

Example in Python with Selenium :

    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()
    driver.get("https://example.com")

    # Locate elements using CSS selectors
    driver.find_element(By.CSS_SELECTOR, "#login")                     # By ID
    driver.find_element(By.CSS_SELECTOR, ".btn-primary")              # By class
    driver.find_element(By.CSS_SELECTOR, "input[name='email']")       # By attribute
    driver.find_element(By.CSS_SELECTOR, "div.container > p")         # Child selector
    driver.find_element(By.CSS_SELECTOR, "input[name*='user']")       # Partial match

Why Use CSS Selectors?
    Faster than XPath in most browsers
    More readable and concise
    Flexible for targeting dynamic elements
    Widely supported across testing frameworks

CSS Selector Syntax for Tag + Class + Attribute:
    tagname.classname[attribute="value"]

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.facebook.com/")

driver.maximize_window()

# using tag and id combination
driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")

# tag name is always optional
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")

# using tag and class combination
driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@gmail.com")

# using tag and attribute combination
driver.find_element(By.CSS_SELECTOR, "[name=email]").send_keys("abc@gmail.com")

# using tag,class and attribute combination
driver.find_element(By.CSS_SELECTOR, ".inputtext[name=pass]").send_keys("12345")

driver.quit()