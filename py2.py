"""
Author:董仕伟
QQ:842785707
Time:2020/4/28 12:50
Company:科信技术有限公司
"""

print("**************************作业一**************************")
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://hao.360.com/")
driver.maximize_window()

# 通过 name 定位元素
find_name = driver.find_element_by_name("q")
inputa_data = find_name.send_keys("腾讯课堂")

# 通过 id 定位元素
find_id = driver.find_element_by_id("search-btn").click()

# 通过 tag_name 标签定位， 返回第一个元素
find_tag = driver.find_element_by_tag_name("input")

# 通过 tag_name 标签定位， 返回所有元素
find_tags = driver.find_elements_by_tag_name("input")
print(find_tags)

# 通过 class_name 标签定位， 返回所有元素
find_class = driver.find_element_by_class_name("standard")
print(find_class)

# 通过 link_text 部分文本匹配
link_text = driver.find_element_by_link_text("综艺").click()

# 通过 xpath 定位元素
ss = driver.find_element_by_xpath("//input[@type='text']").send_keys("hellow")

# 通过 css 定位元素
sa = driver.find_element_by_css_selector("#search-btn").click()

time.sleep(5)
driver.close()
driver.quit()

print("**************************作业二**************************")
driver = webdriver.Chrome()
driver.get("https://voice.baidu.com/act/newpneumonia/newpneumonia/")
driver.maximize_window()

# 元素1 百度首页
"""
a1 相对路径定位 a标签
a2 相对路径href元素 定位 a标签 
a3 相对路径 + 下标定位 a标签  
"""
# a1 = driver.find_element_by_xpath("//*[@id=‘main’]/div/div/div[1]/div/a")
a2 = driver.find_element_by_xpath("//a[@href ='//www.baidu.com']")
# a3 = driver.find_element_by_xpath("(//a[@target ='_blank'])[1]")

#  元素2 切换地区
s1 = driver.find_element_by_xpath("(//span[@data-type ='btn'])[2]")
# 元素3  现有确诊
s2 = driver.find_element_by_xpath("(//span[@style='position: relative;'])[1]")
s21 = driver.find_element_by_xpath("(//div/span[@style])[1]")


#  元素4 滚动播放按钮
s3 = driver.find_element_by_xpath("//div[@class ='VirusSummarySix_1-1-255_szVrQM']")

# 元素5 累计确认
# 定位不出来了， label 标签下 元素

time.sleep(5)
driver.close()
driver.quit()