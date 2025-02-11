from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math

def is_calc(x):
    return math.log(abs(12*math.sin(int(x))), math.e)


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # wait for a certain price
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "$100"))
    browser.find_element(By.XPATH, "//button[@id='book']").click()

    # find x and calculate
    x = browser.find_element(By.XPATH, "//span[@id='input_value']").text
    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(is_calc(x))
    browser.find_element(By.XPATH, "//button[@id='solve']").click()



finally:
    time.sleep(5)
    browser.quit()
