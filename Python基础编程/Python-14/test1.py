# coding = utf-8
from selenium import webdriver
browser = webdriver.Firefox()
    #(executable_path=r'D:\Program Files\Python\Python36\Tools\Selenium\geckodriver.exe')

browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
str = browser.find_element_by_id("su").get_attribute("value")

print(str)
#browser.quit()