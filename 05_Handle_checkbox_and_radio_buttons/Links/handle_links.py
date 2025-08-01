"""

internal, external, and broken links—especially useful if you're working on web automation, SEO, or site maintenance:

Internal Links

    Definition: Links that point to other pages within the same website.
    Example: From about.html to contact.html on example.com.
    Purpose:
        Helps users navigate your site
        Improves SEO by distributing page authority
        Aids search engines in crawling your site structure

External Links

    Definition: Links that point to pages on a different website.
    Example: A link from example.com to wikipedia.org.
    Purpose:
        Provides additional resources or references
        Builds credibility and trust
        Can be used for affiliate marketing or partnerships

Broken Links

    Definition: Links that lead to non-existent or inaccessible pages.
    Causes:
        Page deleted or moved without updating the link
        Typo in the URL
        External site is down or removed
    Impact:
        Frustrates users with 404 errors
        Hurts SEO and crawlability
        Damages site credibility

How to Fix Broken Links

    Use tools like Ahrefs Broken Link Checker or Search Engine Journal’s guide
    Apply 301 redirects for moved pages
    Regularly audit your site with crawlers like Screaming Frog or Semrush
    Remove or replace dead external links with updated sources
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

# Find number of links in web page
links = driver.find_elements(By.TAG_NAME,'a')
# links = driver.find_elements(By.XPATH,'//a')
print("total number of links are: ",len(links))

# Print all the link names
for link in links:
    print(link.text)


time.sleep(2)
print("Testing done!")
driver.quit()