"""
Author:董仕伟
QQ:842785707
Time:2020/4/28 16:56
Company:科信技术有限公司
"""
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://voice.baidu.com/act/newpneumonia/newpneumonia/")
driver.maximize_window()

# a1 = driver.find_element_by_xpath("//*[@id=‘main’]/div/div/div[1]/div/a")
a2 = driver.find_element_by_xpath("//a[@href ='//www.baidu.com']").click()
# a3 = driver.find_element_by_xpath("(//a[@target ='_blank'])[1]")

#  元素2 切换地区
s1 = driver.find_element_by_xpath("(//span[@data-type ='btn'])[2]").click()
print(s1)
# 元素3  现有确诊
s2 = driver.find_element_by_xpath("(//div/span[@style])[1]")

#  元素4 滚动播放按钮
s4 = driver.find_element_by_xpath("//div[@class ='VirusSummarySix_1-1-255_szVrQM']").click()

time.sleep(5)
driver.close()
driver.quit()