from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)
driver.get('https://alta.ge/')
input_search = driver.find_element(By.ID,'search_input')

wait = WebDriverWait(driver, 5)
search_button = wait.until(EC.presence_of_element_located((By.XPATH, '(//button[@type="submit"])[1]')))

def find_product(product_name):
    input_search.send_keys(product_name)
    time.sleep(1)
    search_button.click()

    page_quantity = 0
    try:
        wait = WebDriverWait(driver, 5)

        xpath_expression = "//*[@id='pagination_contents']/div[4]/div/div/a[last()]"

        # Wait for the element to be visible, not just present
        page_quantity_element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_expression)))

        page_quantity = page_quantity_element.text

    except TimeoutException as e:
        print(f"Timed out waiting for the page quantity element to be visible. Exception: {e}")
    page_quantity = int(page_quantity)
    names = []
    prices = []
    for i in range(page_quantity):
        name = driver.find_elements(By.XPATH,"//a[@class='product-title']")
        price = driver.find_elements(By.XPATH,"//span[@class='ty-price-num']")
        for j in range(len(name)):
            names.append(name[j].text)
            prices.append(price[j].text)

    df = pd.DataFrame()

    df['product'] = names
    df['price'] = prices

# after 10 seconds chrome will quit
time.sleep(20)

driver.quit()