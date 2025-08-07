
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

# Navigate to the demo page
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
max_slider = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")

print("Locations of sliders before moving ...............")
print(min_slider.location) # {'x': 59, 'y': 250}
print(max_slider.location) # {'x': 613, 'y': 250}

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform() # {'x': 159, 'y': 256}
act.drag_and_drop_by_offset(max_slider,-39,0).perform() # {'x': 574, 'y': 256}
# or
# act.click_and_hold(min_slider).move_by_offset(10, 0).release().perform()
# act.click_and_hold(max_slider).move_by_offset(-10, 0).release().perform()

print("Locations of sliders before moving ...............")
print(min_slider.location)
print(max_slider.location)

print("Testing done!")
driver.quit()


