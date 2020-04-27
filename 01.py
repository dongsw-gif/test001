"""
Author:董仕伟
QQ:842785707
Time:2020/4/24 12:48
Company:科信技术有限公司
"""

import  time
from selenium import webdriver



driver = webdriver.Chrome()
driver.get("http://baidu.com")
time.sleep(10)
time.sleep(20)

driver.quit()