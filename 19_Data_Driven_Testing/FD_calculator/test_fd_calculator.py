from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import read_test_data, write_result
import time

def test_fd_calculator(file_path):
    data = read_test_data(file_path)
    results = []

    service_obj = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://groww.in/calculators/fd-calculator")
    wait = WebDriverWait(driver, 10)

    for entry in data:
        # Clear and enter Principal
        principal_input = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='TOTAL_INVESTMENT']")))
        principal_input.clear()
        principal_input.send_keys(str(entry['Principal']))

        # Clear and enter Rate
        rate_input = driver.find_element(By.XPATH, "//*[@id='RATE_OF_INTEREST']")
        rate_input.clear()
        rate_input.send_keys(str(entry['Rate']))

        # Clear and enter Tenure
        tenure_input = driver.find_element(By.XPATH, "//*[@id='FD_TIME_IN_YEARS']")
        tenure_input.clear()
        tenure_input.send_keys(str(entry['Tenure']))

        time.sleep(2)  # Let the site update the result

        # Get calculated maturity
        maturity_element = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='root']/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/table/tr[3]/td[2]/span")
        ))
        calculated = int(maturity_element.text.replace("₹", "").replace(",", "").strip())

        # Compare with expected
        expected = int(entry['Expected'])
        result = "PASS" if abs(calculated - expected) < 1 else f"FAIL ({calculated})"
        results.append(result)

    driver.quit()
    write_result(file_path, results)

# Run the test
test_fd_calculator("fd_test_data.xlsx")
