from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def init_driver():
    driver = webdriver.Chrome('chromedriver')
    
    driver.wait = WebDriverWait(driver, 5)

    return driver
 
def lookup(driver):
    driver.get("http://127.0.0.1:3002/")

    try:
        home=driver.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "team")
        ))
        return[{"success":"awesome"}]
            # print link.get('href',None),link.get_text()
        
    except TimeoutException:
        print("page not loaded")
# if __name__ == "__main__":
#     driver = init_driver()
#     lookup(driver)
#     time.sleep(5)
#     driver.quit()