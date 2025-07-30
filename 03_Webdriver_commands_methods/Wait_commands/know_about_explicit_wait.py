"""

explicit wait -
    gives you precise control over how long your script should wait for a specific condition to be met before moving forward.
    It’s like telling Selenium: “Hold on—don’t rush until this exact thing happens.”

What Is Explicit Wait -

    It waits for a specific condition (like visibility, clickability, or presence of an element).
    Unlike implicit wait, it’s targeted—you apply it to individual elements or actions.
    It’s implemented using WebDriverWait and expected_conditions.

Syntax Example -

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    driver = webdriver.Chrome()
    driver.get("https://example.com")

    # Wait up to 10 seconds for the element to be clickable
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submitBtn"))
    )

    element.click()

Common Conditions You Can Wait For -

    Condition Type	            Method
    Element is present in DOM	presence_of_element_located()
    Element is visible	        visibility_of_element_located()
    Element is clickable	    element_to_be_clickable()
    Alert is present	        alert_is_present()
    Title contains              specific text	title_contains()
    Text appears in element	    text_to_be_present_in_element()

Why Use Explicit Wait -

    Ideal for dynamic content (AJAX, animations, delayed loads).
    Prevents flaky tests caused by elements not being ready.
    Avoids unnecessary delays—proceeds as soon as the condition is met.

    We use explicit waits because we’re waiting for a condition to be fulfilled.
    Selenium doesn’t know ahead of time when, for example, an element will appear, become visible, or be clickable.
    So we say, “Wait up to X seconds, but only if this particular condition is met.”

It’s a conditional wait, not a fixed delay

    Unlike time.sleep(10), which just blindly pauses for 10 seconds, an explicit wait is smarter:
    It checks repeatedly at short intervals (default: every 500ms).
    As soon as the condition is true—like an element becoming clickable—it moves on.
    If the condition isn’t met within the timeout period, Selenium raises an error (usually TimeoutException).

Why not skip the wait entirely?

    Because webpages aren’t always predictable. Elements may:
    Load dynamically from AJAX requests
    Be hidden initially and only become visible after a user action
    Depends on slow network responses or animations

So we wait not because we enjoy twiddling our thumbs, but because our script would break if it tried to
interact with something that isn’t ready yet.

Implicit vs Explicit Wait in Selenium :

    Feature	                    Implicit Wait	                            Explicit Wait
    Scope	                    Applies globally to all element searches	Targets specific elements with defined conditions
    How It's Set Up	            driver.implicitly_wait(time)	            Uses WebDriverWait + expected_conditions
    Polling Frequency	        Checks every 500ms until timeout	        Checks every 500ms until condition is met
    Trigger	                    Time-based	                                Condition-based
    Max Wait Duration	        Fixed timeout	                            Fixed timeout with flexible condition
    Reusability	                Set once; applies throughout	            Needs to be written each time it's used
    Intelligence	            Blind wait until element is found	        Smart wait for specific scenarios (e.g. clickable)
    Exception Raised If Fails	NoSuchElementException	                    TimeoutException
    Best For	                Simple, static pages	                    Dynamic content and interactive elements
    Mixing Both	                Can cause flaky behavior	                Recommended to avoid mixing them

What Is poll_frequency -
    It's the interval (in seconds) between checks for a condition.
    In your example, poll_frequency=2 means Selenium will try every 2 seconds to see
    if the condition (like "element is clickable") is met.

Why Use It -
    Avoids hammering the DOM constantly, which could slow things down.
    Gives elements a little breathing room
    useful if they take time to load, animate, or transition.

Default Value -
    If you don’t set poll_frequency, Selenium defaults to 0.5 seconds.

Example in Action -
    my_wait = WebDriverWait(driver, 10, poll_frequency=2)
    This will wait up to 10 seconds, checking every 2 seconds, before throwing a TimeoutException.

"""

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

my_wait = WebDriverWait(driver,10,poll_frequency=2,
                        ignored_exceptions=[NoSuchElementException,
                                            ElementNotVisibleException,
                                            ElementNotSelectableException,Exception]) #explicit wait declaration

driver.get("https://www.bing.com/")

driver.maximize_window()

search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("Selenium")
search_box.submit()

search_link = my_wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='Selenium']")))
search_link.click()

print("Testing done!")
driver.quit()