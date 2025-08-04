"""

A web table in Selenium
    refers to an HTML <table> element that displays data in rows and columns on a webpage.
    Selenium can be used to locate, extract, and interact with this data for testing or automation purposes.

What Is a Web Table?
    A web table is structured using:
        <table> – defines the table
        <tr> – defines a row
        <td> – defines a cell (data)
        <th> – defines a header cell

A static web table in Selenium
    refers to an HTML table whose structure—rows and columns—remains fixed during runtime.
    These tables are ideal for automation because
    their content doesn't change dynamically, making them predictable and easy to interact with.

Example of a Static Web Table -

        <table name="BookTable">
          <tr>
            <th>Book Name</th>
            <th>Author</th>
            <th>Subject</th>
            <th>Price</th>
          </tr>
          <tr>
            <td>Learn Selenium</td>
            <td>Amit</td>
            <td>Selenium</td>
            <td>300</td>
          </tr>
          <tr>
            <td>Learn Java</td>
            <td>Mukesh</td>
            <td>Java</td>
            <td>500</td>
          </tr>
        </table>

How to Handle Static Web Tables in Selenium -
    You can:
    Count rows and columns
    Read specific cell data
    Loop through all cells
    Apply conditions (e.g., filter by author)

Static vs Dynamic Web Tables in Selenium-

    Feature	                Static Web Table	                Dynamic Web Table
    Structure	            Fixed rows and columns	            Rows/columns change based on data or user actions
    Content Source	        Hardcoded in HTML	                Loaded via JavaScript, AJAX, or APIs
    Visibility	            All data is visible on page load	Data may be paginated, filtered, or hidden
    XPath Stability	        Easier to locate with fixed XPath	Requires flexible, dynamic XPath strategies
    Examples	            Product list, static reports	    Dashboards, live monitoring, search results
    Automation Complexity	Simple to automate	                Requires handling dynamic loading, waits, etc.

Example: Static Web Table
    html
    <table>
      <tr><th>Name</th><th>Age</th></tr>
      <tr><td>Alice</td><td>30</td></tr>
      <tr><td>Bob</td><td>25</td></tr>
    </table>
        Data is embedded in HTML
        No JavaScript or backend interaction

Example: Dynamic Web Table
    html
    <table id="liveData">
      <!-- Rows populated via JavaScript -->
    </table>
    <script>
      fetch('/api/users').then(data => populateTable(data));
    </script>
        Table is empty at first
        Data is fetched and rendered dynamically

How to Handle in Selenium-
    Static Table
        Use direct XPath or CSS selectors
        Loop through <tr> and <td> elements

    Dynamic Table
        Use WebDriverWait to wait for data
        Handle pagination, filters, or AJAX updates
        Use dynamic XPath with variables
"""

# 1) Count the number of rows and columns
# 2) Read specific row and column data
# 3) Read all row and column data
# 4) Read data based on condition (List books, whose author is Mukesh)

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1) Count the number of rows and columns
no_of_rows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
no_of_column = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print("Number of rows - ",no_of_rows)
print("Number of columns - ",no_of_column)

# 2) Read specific row and column data
specific_element = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]")
print("\nPrinting specific element - ",specific_element.text)

# 3) Read all row and column data
print("\nPrinting all the rows and column.........")
for r in range(2,no_of_rows+1):
    for c in range(1,no_of_column+1):
        all_element = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(all_element, end='    ')
    print()

# 4) Read data based on condition (List books, whose author is Mukesh)
for r in range(2,no_of_rows+1):
    author_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if author_name == "Mukesh":
        book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(book_name,"   ",author_name,"   ",price)

time.sleep(4)
print("Testing done!")
driver.quit()
