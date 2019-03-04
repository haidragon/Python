from selenium import webdriver
import time
from selenium.webdriver import ActionChains

def login(firefox):
    print("=" * 20)
    time.sleep(2)
    firefox.get("https://192.168.92.191/owa")
    time.sleep(2)
    firefox.find_element_by_id("username").send_keys("test02")
    firefox.find_element_by_id("password").send_keys("Pass@123")
    firefox.find_element_by_xpath('//td/input[@name="login"]').click()
    time.sleep(10)

def move(firefox):
    mail_list = firefox.find_elements_by_xpath('//div[@id="divSubject"]')
    print(len(mail_list))
    for i in range(1000):
        try:
            firefox.find_element_by_xpath('//div[@id="divToolbarButtonmove"]/a[@id="move"]').click()
            report_button = firefox.find_element_by_xpath('//body/div/div/span[@id="spnT"]')
            if report_button.is_displayed():
                report_button.click()
        except Exception as e:
            print(e.args)

def main():
    # 设置浏览器配置文件
    profile_director = r'C:\Users\xiaoming\AppData\Roaming\Mozilla\Firefox\Profiles\31hxaedj.default'
    profile = webdriver.FirefoxProfile(profile_director)
    # 创建浏览器
    firefox = webdriver.Firefox()
    login(firefox)
    move(firefox)


if __name__ == "__main__":
    main()



