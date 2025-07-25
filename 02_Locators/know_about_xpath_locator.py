"""
XPath :

    Powerful locator strategy used to identify elements on a web page by navigating through its HTML DOM structure.
    XPath is a way to locate elements on a web page using the structure of the page’s HTML.
    Think of the web page like a tree, and XPath is how you move through the branches to find exactly what you want.
    In Selenium, we use XPath when we want to click a button, type into a textbox,
    or check if something exists—even if it doesn't have a clear name or ID.

Two Ways to Write XPath:

    Type	                        How It Works	                                                    Example
    Absolute(full path) XPath	    Starts from the top/root of the page’s HTML and follows every step	    /html/body/div[1]/input
    Relative(partial) XPath	        Starts from anywhere—it just jumps to the part you care about	    //input[@id='username']
    - Relative XPath is better because it works even if the page layout changes.

Example of Absolute/full xpath :- /html/body/nav/div/div/div[1]/div/ul/li[2]/a
Example of Relative/partial xpath :- //*[@id="navbarSupportedContent"]/div[1]/div/ul/li[2]/a

Basic Structure of xpath :

    //tagname[@attribute='value']
        This means:
        // = “find anywhere”
        tagname = the HTML tag (like div, input, button)
        @attribute='value' = match an attribute (like id='login')

Cool XPath Tricks :

    Here’s how XPath can be extra smart:

    What It Does	                XPath	                        Why Use It
    Match part of an attribute	    contains(@class, 'btn')	        Useful for dynamic class names
    Match visible text	            text()='Login'	                For buttons or links
    Match first item	            //li[1]	                        Get the first in a list
    Match last item	                //li[last()]	                Get the last one
    Combine conditions	            @name='email' and @type='text'	For precise matches

DOM :

    It is an API interface provided by user or programming interface for web documents.
    When a web page is loaded, the browser creates a Document Object Model of the page.
    It turns your HTML into a tree-like structure made of nodes (elements, text, attributes).
    JavaScript uses the DOM to read, change, or react to parts of the page.

Absolute XPath vs Relative XPath :

    Feature	            Absolute XPath	                                Relative XPath
    Starts With	        / (single slash)	                            // (double slash)
    Path Type	        Full path from the root to the element	        Partial path from anywhere in the DOM
    Example	            /html/body/div[1]/form/input[2]	                //input[@name='email']
    Use of attribute    use only tags/nodes                             use attributes
    Flexibility	        Very rigid—breaks if page structure changes	    Flexible—works even if layout changes
    Length	            Long and hard to maintain	                    Short and easier to read
    Use Case	        Rarely used in automation	                    Preferred in Selenium scripts

Steps to Write XPath Manually :
    1) Inspect the Element Right-click the element in your browser → Inspect → View its HTML.
    2) Identify Unique Attributes Look for id, name, class, or type that uniquely identify the element.
    3) Build the XPath Use tag + attribute:
        //button[@type='submit']
    Use Functions for Flexibility :

        1) contains() → Partial match
        //input[contains(@name, 'user')]

        2) starts-with() → Match beginning
        //div[starts-with(@id, 'section')]

        3) text() → Match visible text
        //a[text()='Sign Up']

        4) Using and in XPath
            Use and when all conditions must be true:
            //input[@id='search_query_top' and @name='search_query']
            This matches an <input> element that has both id="search_query_top" and name="search_query".

        5) Using or in XPath
        Use or when any one of the conditions can be true:
        //input[@id='search_query_top' or @name='search_query']
        This matches an <input> element if it has either id="search_query_top" or name="search_query".

        Navigate Relationships (Axes) Use axes to move through the DOM:
        parent::, child::, following::, preceding::
        //label[text()='Email']/following::input[1]

contains() and starts-with() are functions used to match dynamic or partial attribute values—perfect for locating elements when IDs or class names change or aren't fully predictable.

contains() Function :
    Matches elements whose attribute contains a specific substring.
    Useful for partial matches in dynamic attributes.
    Syntax:
        //tagname[contains(@attribute, 'value')]
    Example:
        //input[contains(@name, 'user')]
        Finds any <input> element with a name that includes the word “user” (e.g., username, user_id).

starts-with() Function
    Matches elements whose attribute starts with a specific string.
    Ideal when attribute values begin with a consistent prefix.
    Syntax:
        //tagname[starts-with(@attribute, 'value')]
    Example:
        //div[starts-with(@id, 'section')]
        Finds any <div> whose id starts with “section” (e.g., section1, section-header).

Scenario	                                Use
Attribute value is partially known	        contains()
Attribute value has a predictable prefix	starts-with()
Need to match dynamic IDs or classes	    Either, depending on pattern


Built-in Browser Tools :

    Google Chrome / Edge -
        Right-click on the element you want.
        Select Inspect to open DevTools.
        In the Elements panel, right-click the highlighted HTML.
        Choose Copy → Copy XPath.
        This gives you the absolute XPath, which may be brittle if the page structure changes.

Browser Extensions :

    SelectorsHub -
        A powerful extension for Chrome and Firefox.
        Generates relative XPath, CSS selectors, and even jQuery.
        Highlights elements and validates XPath in real-time.

    ChroPath -
        Auto-generates XPath and CSS selectors.
        Offers a studio mode to record steps and generate test cases.
        Great for Selenium users.

    XPath Helper -
        Lightweight Chrome extension.
        Lets you hover and instantly see XPath.
        Ideal for quick XPath extraction.

"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("http://www.automationpractice.pl/index.php")

driver.maximize_window()

# Absolute Xpath
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/input[4]").send_keys("T-shirts")
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/button[1]").click()

# Relative Path
driver.find_element(By.XPATH, "//input[@id='search_query_top']").send_keys("T-shirts")
driver.find_element(By.XPATH, "//button[@name='submit_search']").click()

# relative xpath options
# using and operator
driver.find_element(By.XPATH, "//input[@id='search_query_top' and @name='search_query']").send_keys("T-shirts")

# using or operator
driver.find_element(By.XPATH, "//input[@id='search_query_top' or @name='search_query']").send_keys("T-shirts")

# contains() method
driver.find_element(By.XPATH, "//*[contains(@name, 'search')]")

# starts-with() method
driver.find_element(By.XPATH, "//*[starts-with(@type, 'tex')]")

# text()
driver.find_element(By.XPATH, "//a[text()='Women']")

print("Testing done!")
time.sleep(3)
driver.quit()