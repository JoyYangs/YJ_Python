'''
selenium执行自动化的流程
1- 自动化程序调用selenium客户端库函数
2- 客户端库会发送selenium命令给浏览器的驱动程序
3- 浏览器驱动程序接收到命令后，驱动浏览器去执行命令
4- 浏览器执行命令
5- 浏览器驱动程序获取命令的执行结果，返回给自动化程序
6- 自动化程序对返回结果进行处理

'''
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# opt = webdriver.ChromeOptions() 
# print(opt)
# print(opt.__dict__)
# opt.add_argument("user-data-dir=/Applications/Google Chrome/User Data")

# wd = webdriver.Chrome('/Users/joye/Downloads/chromedriver')
# # print(wd.__dict__)

# wd.get('https://ke.qq.com')

# # id = js_keyword
# input = wd.find_element_by_id('js_keyword')
# input.send_keys('vue')
# # id = js_search
# search = wd.find_element_by_id('js_search')
# search.click()

# # class = sort-nav-order
# nav_order = wd.find_element_by_class_name('sort-nav-top')
# # nav_order 是一个 selenium.webdriver.remote.webelement.WebElement 对象
# free = wd.find_element_by_css_selector('[href="https://ke.qq.com/course/list/vue?price_min=0&price_max=0"]')
# free.click()

# # ul class = course-card-list
# course_list = wd.find_elements_by_class_name('course-card-list')
# li_lists = course_list[0].find_elements_by_tag_name('li')
# li_lists[2].click()

# wd.close()

# buy_btn = wd.find_element_by_class_name('institution-btn-txt')
# buy_btn.click()







# course_item1 = course_list.find_element_by_class_name('course-card-item--v3')
# # li > a class = item-img-link
# item_link = course_item1.find_element_by_class_name('item-img-link')
# item_link.click()

# # buy class = institution-btn-txt
# buy_btn = wd.find_element_by_class_name('institution-btn-txt')
# buy_btn.click()



import os
from selenium import webdriver

# chromedriver = "/Users/joye/Downloads/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chromedriver)
# driver.get("http://stackoverflow.com")
# # driver.quit()


driver = webdriver.Chrome(executable_path='/Users/joye/Downloads/chromedriver')
driver.get("http://stackoverflow.com")
