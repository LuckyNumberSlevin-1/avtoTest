from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


treasure = browser.find_element_by_id("treasure")
b = treasure.get_attribute("valuex")
x = b
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
input2 = browser.find_element_by_id("robotCheckbox")
input2.click()
input3 = browser.find_element_by_id("robotsRule")
input3.click()
input4 = browser.find_element_by_css_selector('[type="submit"]')
input4.click()
time.sleep(10)
browser.quit()


