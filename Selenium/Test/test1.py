from selenium import webdriver
import time
'''
chromeOption = webdriver.ChromeOptions()
chromeOption.add_argument('--user-data-dir=C:/Users/xiaoming/AppData/Local/Google/Chrome/User Data')
time.sleep(2)
print("11111")
chrome = webdriver.Chrome(chrome_options=chromeOption)
'''
chrome = webdriver.Chrome()

print("="*20)
time.sleep(2)
chrome.get("http://192.168.8.161:18080/cas/login")

chrome.find_element_by_id("username").send_keys("wanghongming_dj")
chrome.find_element_by_id("password").send_keys("zhonghui")
chrome.find_element_by_id("cfets-lg-form-btn").click()
chrome.find_element_by_link_text("中汇BPM流程管理系统").click()
chrome.switch_to.window(chrome.window_handles[1])
print(chrome.title)
chrome.switch_to.frame("main_iframe")
#chrome.find_element_by_class_name("collapsable").click()
time.sleep(2)
#chrome.find_element_by_id("sidebar_s")
chrome.find_element_by_id("client")
chrome.find_element_by_link_text("原BPM系统与全流程项目管理平台访问地址变更")


time.sleep(1)
#chrome.find_element_by_link_text("hao123").click()
#time.sleep(2)
#chrome.find_element_by_link_text("凤 凰 网").click()



