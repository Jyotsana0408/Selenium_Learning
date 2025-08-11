import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

countries_list = driver.find_elements(By.XPATH,"//*[@id='select2-billing_country-results']/li")

print(len(countries_list))

for country in countries_list:
    if country.text == "Maldives":
        country.click()
        break

time.sleep(3)
print("Testing done!")
driver.quit()