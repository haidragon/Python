from selenium import webdriver

def douyu():
    #通过浏览器获取所有的xpath元素
    li_list = driver.find_elements_by_xpath('//ul[@id="live-list-contentbox"]/li')
    content_dict = {}
    #遍历所有的li标签，存放到字典中
    for i in li_list:




if __name__ == "__main__":
    driver = webdriver.Chrome
    url = "https://www.douyu.com/director/all"
    driver.get(url)
    douyu()