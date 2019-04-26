from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import requests
import time
from mysqlHelper import mySqlHelper

class spider():

    def get_proxy(self):
        url = "http://0.0.0.0:5555/random"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("成功！")
                return response.text
            return None
        except requests.ConnectionError:
            return None

    def browser_open(self):
        proxy = self.get_proxy()
        print(proxy)
        if proxy:
            proxies = {
                'http': 'http://' + proxy,
                'https': 'https://' + proxy
            }
        self.chrome_options=webdriver.ChromeOptions()
        self.chrome_options.add_argument('--proxy-server=http://'+proxy)
        self.browser=webdriver.Chrome(options=self.chrome_options)
        self.wait=WebDriverWait(self.browser,10)
        self.flag=True

    def get_data(self):
        items=self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//div[@class="txt-box"]')))
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')


        articals=self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//ul[@class="news-list"]/li/div[@class="txt-box"]/h3/a')))
        titles=[title.text for title in articals]
        urls = [url.get_attribute('href') for url in articals]
        btn=self.wait.until(ec.presence_of_all_elements_located((By.XPATH,'//div[@class="jzgd"]')))

        txts=self.wait.until(ec.presence_of_all_elements_located((By.XPATH,'//ul[@class="news-list"]/li/div[@class="txt-box"]/p')))
        txts=[txt.text for txt in txts]
        accounts = self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//ul[@class="news-list"]/li/div[@class="txt-box"]/div/a')))
        accounts = [account.text for account in accounts]

        self.data=zip(titles, txts ,accounts, urls)




    def change_page(self):
        try:
            #self.wait.until(ec.element_to_be_clickable((By.XPATH, '//a[@class="np"]'))).click()
            time.sleep(2)

            self.wait.until(ec.element_to_be_clickable((By.XPATH, '//div[@class="jzgd"]/a'))).click()
            time.sleep(2)
            print('加载更多内容')

        except TimeoutException:
            self.flag=False
            print("无更多内容")

    def get_detail(self):
        x=''
        for i in self.urls:
            print(i)


    def save_data(self):
        self.db=mySqlHelper()
        temp=('title', 'txt_info', 'account', 'url' )
        for item in self.data:
            self.dic=dict(zip(temp,item))
            self.db.insert(self.dic)


    def run(self):
        self.browser_open()
        #self.browser.get("https://weixin.sogou.com/weixin?type=2&s_from=input&query=%E7%88%AC%E8%99%AB&ie=utf8")
        #self.browser.get('http://httpbin.org/get')
        self.browser.get("https://weixin.sogou.com/")
        time.sleep(2)

        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        #self.get_proxy()
        time.sleep(2)
        #self.change_page()
        while self.flag:
            self.change_page()
            time.sleep(2)
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            #self.get_data()
            time.sleep(2)
        print('开始爬取')
        self.get_data()
        self.save_data()
        #self.get_detail()

if __name__=='__main__':
    spiders=spider()
    spiders.run()