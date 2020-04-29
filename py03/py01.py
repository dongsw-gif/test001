"""
Author:董仕伟
QQ:842785707
Time:2020/4/30 0:12
Company:科信技术有限公司
"""

import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://mail.qq.com/")
# 切换到 iframe 中；可通过 iframe_name, id, 节点三种方式切换到iframe 中；
driver.switch_to.frame('login_frame')
# 设置隐式 等待时间
driver.implicitly_wait(30)
driver.find_element_by_xpath("//a[text()='帐号密码登录']").click()
driver.find_element_by_xpath("//input[@id='u']").send_keys("842785707@qq.com")
driver.find_element_by_xpath("//input[@type='password']").send_keys("dsw123456@")
driver.find_element_by_xpath("//input[@value='登 录']").click()

driver.sleep(10)
driver.close()
driver.quit()
