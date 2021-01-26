from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome("C:/Users/Carter/Desktop/chromedriver.exe")
browser.get(link)
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
browser.find_element_by_id("book").click()
x = int(browser.find_element_by_id("input_value").text)
browser.find_element_by_id("answer").send_keys(str(math.log(math.fabs(12*math.sin(x)))))
browser.find_element_by_css_selector("button[type='submit']").click()


