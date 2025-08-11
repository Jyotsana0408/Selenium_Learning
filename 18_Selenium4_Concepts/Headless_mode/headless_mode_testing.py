"""

Running Selenium in headless mode means launching the browser without a visible UI
perfect for automation on servers, CI pipelines, or when you just want speed without the visual overhead.

Why Use Headless Mode?
    Faster execution
    No GUI required (ideal for servers or Docker)
    Useful for background tasks and scheduled jobs

options.add_argument("--headless")  # Enable headless mode
options.add_argument("--window-size=1920,1080")  # Optional: set viewport size

Things to Watch Out For:

    Some websites behave differently in headless mode (e.g., animations, lazy loading).
    You may need to set a viewport size (--window-size) to ensure elements are visible.
    Screenshots still work in headless mode.

Pros of Headless Mode:
    Advantage	                Description
    Faster Execution	        No rendering of UI means quicker load and interaction times.
    Resource Efficient	        Uses less CPU and memory—ideal for servers or CI environments.
    Perfect for Automation	    Great for background tasks, scheduled jobs, and continuous integration.
    Works in Containers	        Easily runs in Docker or other headless environments without GUI support.
    Screenshots Still Work	    You can still capture screenshots for debugging or reporting.

Cons of Headless Mode:
    Limitation	                Description
    Different Behavior	        Some websites detect headless browsers and may block or alter content.
    Element Visibility Issues	Elements might not be visible or interactable without proper viewport settings.
    Debugging is Harder	        No visual feedback makes it tougher to spot layout or rendering issues.
    Animations & Lazy Loading	Some dynamic content may not load properly without scrolling or waiting.
    Limited Browser Features	Certain browser extensions or features may not work in headless mode.

When to Use It:
    Automated testing in CI/CD pipelines
    Web scraping on servers
    Scheduled background tasks
    Performance-sensitive environments

When to Avoid It:
    When debugging UI issues
    When testing visual elements or animations
    When dealing with websites that block headless browsers
"""

from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless")
    ops.add_argument("--window-size=1920,1080")
    # ops.headless = True
    service_obj = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_obj,options=ops)
    return driver

driver = headless_chrome()
driver.get("https://demoqa.com")
print(driver.title)
print(driver.current_url)

driver.quit()