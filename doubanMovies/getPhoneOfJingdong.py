from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import time
from mySqlHelper import mySqlHelper

'''browser=webdriver.Chrome()
url='https://list.jd.com/list.html?cat=9987,653,655&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main'
browser.get(url)
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')#模拟进度条下拉，获取当前页数所有商品
#获取节点'下一页'
next_page=browser.find_element(By.CLASS_NAME, 'pn-next')#方式1
next_page=browser.find_element(By.XPATH,'//a[@class="pn-next"]') 方式2
#模拟点击
#next_page.click()'''
class jdSpder():
    def browser_open(self):
        self.browser=webdriver.Chrome()
        self.wait=WebDriverWait(self.browser,10)
        self.flag=True

    def get_data(self):
        goods=self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//li[@class="gl-item"]/div')))
        good_id=[item.get_attribute('data-sku') for item in goods]
        links=['https://item.jd.com/{id}.html'.format(id=item) for item in good_id]
        prices=self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//li[@class="gl-item"]/div/div[3]/strong[1]/i')))
        #prices = self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//div[@class="gl-i-wrap j-sku-item"]/div[3]/strong/i')))
        prices=[price.text for price in prices]
        names = self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//li[@class="gl-item"]/div/div[4]/a/em')))
        names = [name.text for name in names]
        commits = self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//li[@class="gl-item"]/div/div[5]/strong/a')))
        commits = [commit.text for commit in commits]
        shops = self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//li[@class="gl-item"]/div/div[7]/span/a')))
        shops = [shop.text for shop in shops]
        self.data=zip(links, names, prices, commits, shops)



    def save_data(self):
        self.db=mySqlHelper()
        temp = ('link', 'name', 'price', 'commits', 'shop_name')
        for item in self.data:
            self.dic=dict(zip(temp,item))
            self.db.insert(self.dic)


    def change_page(self):
        try:
            self.wait.until(ec.element_to_be_clickable((By.XPATH, '//a[@class="pn-next"]'))).click()
            time.sleep(1)
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            print("数据存储成功！")
        except NoSuchElementException:
            self.flag=False



    def run(self):
        i=1
        self.browser_open()
        self.browser.get('https://list.jd.com/list.html?cat=9987,653,655&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main')
        time.sleep(1)
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        while self.flag:
            print('正在爬取第{0}页'.format(i))
            self.get_data()
            self.save_data()
            self.change_page()
            i=i+1
        print("结束")




if __name__=='__main__':
    spider=jdSpder()
    spider.run()



















