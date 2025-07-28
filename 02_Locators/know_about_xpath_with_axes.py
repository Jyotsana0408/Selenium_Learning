"""
XPath provides axes :
let you navigate the DOM tree relative to a current node.
These are super handy in Selenium when you want to locate elements based on their relationships.
Here's a breakdown of some commonly used axes like self, parent, and others:

    Axis	                Description	                                                Example
    self::	                Selects the current node itself	                            //input[@id='email']/self::input
    parent::	            Selects the parent of the current node	                    //input[@id='email']/parent::*
    child::	                Selects all children of the current node	                //div[@class='form']/child::input
    ancestor::	            Selects all ancestors (parent, grandparent, etc.)	        //input[@id='email']/ancestor::form
    descendant::	        Selects all descendants (children, grandchildren, etc.)	    //form[@id='signup']/descendant::input
    following::	            Selects all nodes after the current node in the document	//input[@id='email']/following::input
    preceding::	            Selects all nodes before the current node	                //input[@id='email']/preceding::label
    following-sibling::	    Selects siblings after the current node                 	//label[@for='email']/following-sibling::input
    preceding-sibling::	    Selects siblings before the current node	                //input[@id='email']/preceding-sibling::label


Here's a breakdown of how nodes relate to each other:

    Types of Node Relationships in XPath

    Relationship	Description	                                                    Example
    Parent	        The node directly above another node	                        <div> is the parent of <span>
    Child	        A node directly below another node	                            <span> is a child of <div>
    Ancestor	    Any node above the current node (parent, grandparent, etc.)   	<body> is an ancestor of <input>
    Descendant	    Any node below the current node (child, grandchild, etc.)	    <input> is a descendant of <form>
    Sibling	        Nodes that share the same parent	                            <label> and <input> under the same <div>
    Self	        The current node itself	Useful for confirming or filtering the current node
    Following	    All nodes that appear after the current node in the document	Useful for locating elements that come later
    Preceding	    All nodes that appear before the current node	                Helps find earlier elements in the DOM

XPath Axes for Navigating Relationships

    XPath uses axes to define these relationships:

    parent:: → Selects the parent node

    child:: → Selects child nodes

    ancestor:: → Selects all ancestors

    descendant:: → Selects all descendants

    following-sibling:: → Selects siblings after the current node

    preceding-sibling:: → Selects siblings before the current node

    self:: → Selects the current node

normalize-space() function in XPath :
    whitespace-cleaning tool that’s super useful in Selenium when you're dealing with messy or inconsistent text on web pages.

What normalize-space() Does :

    Removes leading and trailing spaces
    Replaces multiple spaces between words with a single space
    Returns the cleaned-up string
    This helps when the text you're trying to match has extra spaces that could break your XPath expression.

Why It’s Useful :

    Web content often includes invisible formatting or extra spaces.
    normalize-space() ensures your XPath works reliably, even if the text isn’t perfectly formatted.
    It’s especially handy for text-based validations and dynamic content.

"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

driver.maximize_window()

# self
text_msg = driver.find_element(By.XPATH,"//a[normalize-space()='HFCL']/self::a").text
print(text_msg)

# parent
text_msg1 = driver.find_element(By.XPATH,"//a[normalize-space()='HFCL']/parent::td").text
print(text_msg1)

# children of ancestor of self element
children = driver.find_elements(By.XPATH, "//a[normalize-space()='HFCL']/ancestor::tr/child::td")
print("Number of children nodes: ",len(children))

# ancestor
ancestor_msg = driver.find_element(By.XPATH, "//a[normalize-space()='HFCL']/ancestor::tr").text
print(ancestor_msg)

# descendant
descendants = driver.find_elements(By.XPATH, "//a[normalize-space()='HFCL']/ancestor::tr/descendant::*")
print("Number of descendant nodes: ",len(descendants))

# following
following_nodes = driver.find_elements(By.XPATH, "//a[normalize-space()='HFCL']/ancestor::tr/following::*")
print("Number of following nodes: ",len(following_nodes))

# following-sibling
following_sibling_nodes = driver.find_elements(By.XPATH, "//a[normalize-space()='HFCL']/ancestor::tr/following-sibling::*")
print("Number of following-siblings nodes: ",len(following_sibling_nodes))

following_sibling_nodes1 = driver.find_elements(By.XPATH, "//a[normalize-space()='HFCL']/ancestor::tr/following-sibling::tr")
print("Number of following-siblings tr nodes: ",len(following_sibling_nodes1))

# preceding
preceding_nodes = driver.find_elements(By.XPATH, "//a[normalize-space()='HFCL']/ancestor::tr/preceding::*")
print("Number of preceding nodes: ",len(preceding_nodes))

# preceding-sibling
preceding_sibling_nodes = driver.find_elements(By.XPATH, "//a[normalize-space()='HFCL']/ancestor::tr/preceding-sibling::*")
print("Number of preceding-siblings nodes: ",len(preceding_sibling_nodes))

preceding_sibling_nodes1 = driver.find_elements(By.XPATH, "//a[normalize-space()='HFCL']/ancestor::tr/preceding-sibling::tr")
print("Number of preceding-siblings tr nodes: ",len(preceding_sibling_nodes1))


time.sleep(1)
print("Testing Done!")
driver.quit()