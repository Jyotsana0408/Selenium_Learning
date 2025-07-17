"""

Selenium is an open-source automation tool used primarily for automating web applications.
It allows testers and developers to simulate user interactions with a browser
    — like clicking buttons, filling forms, navigating pages
    — and verify that the application behaves as expected.

What Selenium Does:
    Automates browser actions (clicks, typing, scrolling)
    Simulates real user behavior for testing
    Supports multiple browsers: Chrome, Firefox, Edge, Safari
    Works with many programming languages: Python, Java, C#, JavaScript, Ruby
    Integrates with testing frameworks like Pytest, JUnit, TestNG
    Can be used in CI/CD pipelines (e.g., GitHub Actions, Jenkins)

Key Components of Selenium:

    Component	        Description
    Selenium WebDriver	Core API that interacts with browsers
    Selenium IDE	    A browser plugin for recording and playing back tests
    Selenium Grid	    Allows parallel test execution across multiple machines and browsers
    Browser Drivers	    Bridge between Selenium and browsers (e.g., ChromeDriver, GeckoDriver)

How Selenium Works:

    You write test scripts using Selenium APIs.
    Selenium uses a browser driver to launch and control the browser.
    It sends commands like click, send_keys, get, etc.
    The browser executes those actions and returns results.
    Your script validates the outcome (e.g., page title, element presence).

Example Use Case:

    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    driver.find_element(By.ID, "login").click()
    driver.quit()

    This script:
        Opens Chrome
        Navigates to a website
        Clicks a login button
        Closes the browser

Why Selenium Is Popular :

    Cross-browser and cross-platform support
    Strong community and documentation
    Easily integrates with CI tools
    Flexible and powerful for UI testing

----------------------------------------------------------------------------------------------------------------

Selenium 4+ Key Features :

1. W3C WebDriver Standardization :

    Selenium 4 fully adopts the W3C WebDriver protocol for browser communication.
    This eliminates the older JSON Wire Protocol, reducing inconsistencies across browsers.
    Result: More stable and predictable cross-browser automation.

2. Improved Selenium Grid :

    Rebuilt architecture with support for:
        Standalone mode
        Hub & Node mode
        Fully distributed mode
    Supports Docker, Kubernetes, and cloud platforms like AWS and Azure.
    Enhanced UI for monitoring sessions and node activity2.

3. Relative Locators :

    New locators based on element position:
    above(), below(), toLeftOf(), toRightOf(), near()
    Makes test scripts more readable and resilient to layout changes.

4. Enhanced Selenium IDE :

    Revived and available for Chrome, Firefox, and Edge.
    Features:
        Improved GUI
        Export to multiple languages (Java, Python, C#, JavaScript)
        CLI runner (SIDE runner) for parallel execution.

5. Chrome DevTools Protocol (CDP) Integration :

    Native support for Chrome debugging tools:
    Network interception
    Console log capture
    Performance metrics
    Geolocation simulation
    Enables advanced browser-level testing3.

6. New Window and Tab Management :

    New API: driver.switchTo().newWindow(WindowType.TAB/WINDOW)
    Opens new tabs or windows without creating a new WebDriver instance.

7. Upgraded Actions Class :

    More intuitive methods for:
        click(WebElement)
        clickAndHold(WebElement)
        contextClick(WebElement)
        doubleClick(WebElement)
    Improves multi-element and dynamic page interactions.

8. WebElement-Level Screenshots :

    Capture screenshots of specific elements, not just the full page:

    element = driver.find_element(By.ID, "logo")
    element.screenshot("logo.png")

9. Improved Documentation & Dev Experience :

    Better organized guides and updated examples
    Clearer explanations of capabilities, locators, and debugging tools.

10. Deprecated Features :

    DesiredCapabilities replaced by browser-specific Options classes
    FindsBy interfaces removed
    FluentWait methods now use Duration instead of TimeUnit3.

--------------------------------------------------------------------------------------------------------------------

Here’s a detailed comparison of Selenium 3 vs Selenium 4,
highlighting the major differences in architecture, features, and usability:

Architecture :
    Feature	        Selenium 3	                    Selenium 4
    Protocol	    Uses JSON Wire Protocol	        Fully adopts W3C WebDriver Protocol
    Communication	Client → JSON → Browser Driver	Direct, standardized communication
    Compatibility	Browser-specific quirks	        More consistent across browsers

Driver Management :

    Feature	                Selenium 3	                        Selenium 4
    ChromeDriver Setup	    Manual download & path setup	    Selenium Manager auto-downloads correct driver
    Driver Initialization	executable_path	                    Uses Service() class with Options object

Selenium Grid :

    Feature	        Selenium 3	                Selenium 4
    Setup	        Manual Hub & Node jars	    Simplified setup with standalone mode
    Scalability	    Limited parallelism	        Native support for Docker & Kubernetes
    UI	            No dashboard	            Enhanced Grid UI for monitoring sessions

Browser Features :

    Feature	                Selenium 3	        Selenium 4
    Window/Tab Management	Manual switching	New API: driver.switch_to.new_window()
    Element Screenshots 	Full-page only	    Capture element-level screenshots
    Relative Locators	    Not available	    New locators: above(), below(), near()

DevTools Integration :

    Feature	            Selenium 3	                Selenium 4
    Chrome DevTools	    Not supported	            Native support via CDP (Chrome DevTools Protocol)
    Use Cases	        Requires external tools	    Network throttling, performance metrics, console logs

Actions API :

    Feature	                Selenium 3	    Selenium 4
    Mouse/Keyboard Actions	Basic support	Enhanced methods: click(), clickAndHold(), contextClick()

Selenium IDE :

    Feature	    Selenium 3	            Selenium 4
    IDE Tool	Basic Firefox plugin	Rebuilt IDE with export to code, control flow, and debugging3

Test Script Compatibility :

    Feature	                    Selenium 3	    Selenium 4
    Backward Compatibility	        —	        Fully compatible with Selenium 3 scripts
    Migration Effort	            —	        Minimal changes needed for upgrade

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a webpage
driver.get("https://www.google.com")
driver.quit()