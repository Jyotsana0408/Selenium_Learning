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

A dynamic web table in Selenium -
    refers to an HTML table whose structure—number of rows and columns
    changes based on user interaction, backend data updates, or filters.
    These tables are commonly found in dashboards, reports, and data-driven applications.

What Makes a Web Table Dynamic?
    Rows and columns vary depending on data
    Content updates via AJAX or JavaScript
    Pagination, sorting, or filtering alters the visible data
    Often populated from databases or APIs

How to Handle Dynamic Web Tables in Selenium-

    Handling dynamic tables requires flexible XPath strategies and iteration logic. Here's a basic approach:
    Step-by-Step Strategy
        1) Locate the table using a stable XPath or CSS selector.
        2) Find all rows using:
                rows = driver.find_elements(By.XPATH, "//table[@id='tableID']/tbody/tr")
        3) Loop through rows and columns dynamically:
                for r in range(1, len(rows) + 1):
                    cols = driver.find_elements(By.XPATH, f"//table[@id='tableID']/tbody/tr[{r}]/td")
                    for c in range(1, len(cols) + 1):
                        cell = driver.find_element(By.XPATH, f"//table[@id='tableID']/tbody/tr[{r}]/td[{c}]").text
                        print(cell)
        4)Use dynamic XPath with variables if needed:
                row_num = 2
                col_num = 3
                xpath = f"//table[@id='tableID']/tbody/tr[{row_num}]/td[{col_num}]"
                cell_value = driver.find_element(By.XPATH, xpath).text

driver.execute_script("window.scrollBy(0, 1000);")-

    JavaScript command executed by Selenium to scroll the browser window vertically. Let’s break it down:

    What It Does-
        driver.execute_script(...) Executes raw JavaScript inside the browser context.
        "window.scrollBy(0, 1000);" Scrolls the window by:
        0 pixels horizontally (no left/right movement)
        1000 pixels vertically downward

    Equivalent JavaScript
        In a browser console, you could run:
            window.scrollBy(0, 1000);
        This scrolls the page down by 1000 pixels from the current position.

    Why It's Useful in Selenium
        Web elements that are not in the viewport (i.e., off-screen) often can't be interacted with.
        Scrolling ensures:
            Elements become visible
            Selenium can click, read, or validate them

    Variations You Can Use
        Purpose	                    JavaScript Code
        Scroll to top	            window.scrollTo(0, 0);
        Scroll to bottom	        window.scrollTo(0, document.body.scrollHeight);
        Scroll to specific element	arguments[0].scrollIntoView(true);

    Example in Selenium:
        element = driver.find_element(By.ID, "dynamicTable")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

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

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome driver
service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

# Open the test site
driver.get("https://testautomationpractice.blogspot.com/")

# Wait briefly for page to a load
time.sleep(2)

# Locate dynamic table rows directly
rows = driver.find_elements(By.XPATH, "//div[@id='dynamicTable']/table/tbody/tr")
print(f"Total rows found: {len(rows)}\n")

# Loop through each row and extract cell data
for r_index in range(1, len(rows) + 1):
    cells = driver.find_elements(By.XPATH, f"//div[@id='dynamicTable']/table/tbody/tr[{r_index}]/td")
    row_data = [cell.text for cell in cells]
    print(f"Row {r_index}: {row_data}")

# Optional: Extract specific metrics
chrome_cpu = driver.find_element(By.XPATH, "//tr[td[text()='Chrome']]/td[2]").text
firefox_memory = driver.find_element(By.XPATH, "//tr[td[text()='Firefox']]/td[3]").text

print("\nSpecific Metrics:")
print(f"Chrome CPU: {chrome_cpu}")
print(f"Firefox Memory: {firefox_memory}")

# Close browser
time.sleep(2)
driver.quit()
