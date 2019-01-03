from selenium import webdriver
import time

firefox=webdriver.Firefox()
print("="*20)
time.sleep(2)
firefox.get("http://192.168.8.161:18080/cas/login")

firefox.find_element_by_id("username").send_keys("wanghongming_dj")
firefox.find_element_by_id("password").send_keys("zhonghui")
firefox.find_element_by_id("cfets-lg-form-btn").click()
firefox.find_element_by_link_text("中汇BPM流程管理系统").click()

time.sleep(3)
print(firefox.window_handles)
print(firefox.title)
#切换到新标签页
firefox.switch_to.window(firefox.window_handles[1])
print(firefox.title)
#切换到新的frame
time.sleep(1)
firefox.switch_to.frame("main_iframe")
#firefox.find_element_by_class_name("collapsable").click()
time.sleep(3)
#firefox.find_element_by_id("sidebar_s")
#print(firefox.find_elements_by_css_selector(".accordionHeader"))
#print(firefox.find_elements_by_class_name("accordionHeader"))
#点击“人事管理”
time.sleep(2)
firefox.find_elements_by_class_name("accordionHeader")[1].click()
#点击“加班申请（外包人员）”
time.sleep(2)
#print(firefox.find_elements_by_tag_name("a")[12].text)
firefox.find_elements_by_tag_name("a")[12].click()

#firefox.switch_to.frame("frame1")
#firefox.switch_to.frame(firefox.find_element_by_xpath(r"//iframe[contains(@src,'/obpm/portal/dynaform/view/displayViewWithPermission.action?_viewid=11e6-1657-f09a04c7-963a-79dceb6e1640&clearTemp=true&application=11e3-8326-7018dbe4-904e-5fe0bcdb8a06&_resourceid=11e6-27e1-afeae3de-8449-bb416a4b5f1b')]"))
firefox.switch_to.frame(firefox.find_element_by_xpath('//iframe[@src="/obpm/portal/dynaform/view/displayViewWithPermission.action?_viewid=11e6-1657-f09a04c7-963a-79dceb6e1640&clearTemp=true&application=11e3-8326-7018dbe4-904e-5fe0bcdb8a06&_resourceid=11e6-27e1-afeae3de-8449-bb416a4b5f1b"]'))

print(firefox.find_elements_by_css_selector(".close"))

list1 = firefox.find_elements_by_tag_name("a")
print("s1")
for i in list1:
    print("start")
    print(i.text)
print("end")
