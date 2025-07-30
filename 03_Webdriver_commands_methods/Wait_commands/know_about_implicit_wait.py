"""

In Selenium, wait commands are

    essential for handling dynamic web content that may take time to load or become interactive.
    Without proper waits, your script might try to interact with elements before they’re ready—leading to flaky tests or errors.

    wait commands are used to pause the execution of your script until certain conditions are met
    like an element appearing or becoming clickable.
    This helps avoid errors when interacting with elements that load dynamically.

Why Use Waits?

    Web pages often load elements asynchronously (e.g., via JavaScript or AJAX).
    Waits help synchronize your script with the actual state of the page.
    They improve test reliability, reduce errors, and optimize execution time.

Types of Waits in Selenium (Python) :

    Implicit Wait -
        Applies a default wait time for all element searches.
        driver.implicitly_wait(10)
    Explicit Wait -
        Waits for a specific condition to be true before proceeding.
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(...))
    Fluent Wait	-
        Like explicit wait, but with polling intervals and exception handling.
        WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[...])

What Is Implicit Wait -
    An implicit wait tells the Selenium WebDriver to wait for a specified amount of time when trying to locate elements on the page.
    If the element is found before the time expires, the script continues immediately.
    If not, it throws a NoSuchElementException.
    It's like saying, “Hey browser, give the page a few seconds to load before you start looking for stuff.”

How It Works -
    It’s a global setting—applies to all element searches.
    Once set, it remains active for the entire WebDriver session.
    It’s useful for handling elements that may take time to appear due to AJAX or JavaScript loading.

Example in Python
    from selenium import webdriver

    # Create a WebDriver instance
    driver = webdriver.Chrome()

    # Set implicit wait time to 10 seconds
    driver.implicitly_wait(10)

    # Open a webpage
    driver.get("https://example.com")

    # Try to find an element (waits up to 10 seconds)
    element = driver.find_element("id", "myElement")

    # Interact with the element
    element.click()

Things to Keep in Mind
    Don’t mix implicit and explicit waits—they can cause unpredictable behavior.
    Implicit wait is best for simple, consistent delays.
    For more control (like waiting for visibility or clickability), use explicit or fluent waits.

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(10) #implicit wait

driver.get("https://www.bing.com/")

driver.maximize_window()

search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("Selenium")
search_box.submit()

driver.find_element(By.XPATH,"//a[text()='Selenium']").click()

print("Testing done!")
driver.quit()