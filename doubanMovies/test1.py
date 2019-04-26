from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.common.exceptions import NoSuchElementException,TimeoutException


browser=webdriver.Chrome()
#browser.get('http://www.taobao.com')



#获取单个节点
'''input_first=browser.find_element_by_id('q')
input_second=browser.find_element_by_name('q')
input_third=browser.find_element_by_css_selector('#q')
input_forth=browser.find_element_by_xpath('//*[@id="q"]')
print(input_first,input_second,input_third,input_forth)'''

#获取多个节点
'''
li=browser.find_elements_by_css_selector('.service li')
print(li)'''

#节点交互
'''search=browser.find_element(By.ID, 'q')
search.send_keys('iPhone')
time.sleep(1)
search.clear()
search.send_keys('iPad')
button=browser.find_element(By.CLASS_NAME, 'btn-search')
button.click()'''

#动作链
'''url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser=webdriver.Chrome()
browser.get(url)
browser.switch_to.frame('iframeResult')
source=browser.find_element(By.ID,'draggable')
target=browser.find_element(By.ID,'droppable')
actions=ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()'''

#执行JavaScript
'''browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("bottom")')'''


#获取节点信息
'''search=browser.find_element(By.ID, 'q')
s_attribute=search.get_attribute('aria-label')
print(s_attribute)'''

#获取文本值
'''btn=browser.find_element(By.CLASS_NAME,'btn-search')
print(btn.text)'''


#获取id 位置 标签名 大小
'''btn=browser.find_element(By.CLASS_NAME,'btn-search')
print(btn.id)
print(btn.location)
print(btn.tag_name)
print(btn.size)'''

#切换Frame
'''url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser=webdriver.Chrome()
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    tag=browser.find_element(By.CLASS_NAME,'logo')
except NoSuchElementException:
    print('No Logo')
browser.switch_to.parent_frame()
tag=browser.find_element(By.CLASS_NAME,'logo')
print(tag)
print(tag.text)'''

#隐式等待
'''browser.implicitly_wait(3)
browser.get("http://www.taobao.com")
search=browser.find_element(By.ID,'q')
print(search)'''

#显示等待
'''browser.get('http://www.taobao.com')
wait=WebDriverWait(browser,10)
search=wait.until(ec.presence_of_all_elements_located((By.ID,'q')))
btn=wait.until(ec.element_to_be_clickable((By.CLASS_NAME,'btn-search')))
print(search,btn)'''

#前进后退
'''browser.get('http://www.baidu.com')
browser.get('http://www.taobao.com')
browser.back()
time.sleep(1)
browser.forward()'''

#Cookie
'''browser.get('http://www.taobao.com')
print(browser.get_cookies())
browser.add_cookie({'domain': '.taobao.com', 'httpOnly': True, 'name': 'cookielkk', 'path': '/', 'secure': False, 'value': '1ccd04f4330e65303db03f2934daee89'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())'''

#选项卡管理
'''browser.get('http://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('http://www.baidu.com')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://www.cnblogs.com/cnhkzyy/p/9260373.html')'''

#异常处理
try:
    browser.get('http://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element(By.ID, 'lkk')
except NoSuchElementException:
    print('No Element')


browser.close()
