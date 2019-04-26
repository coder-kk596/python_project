from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import time
from mysqlHelper import mysqlHelper
import csv


class houseSipder():
    def browser_open(self):
        self.flag=True
        self.i=0
        self.browser=webdriver.Chrome()
        self.wait=WebDriverWait(self.browser,10)


    def get_data(self):

        '''self.houses=self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//ul[@class="list"]/li')))
        time.sleep(1)'''
        adress_all =self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//ul[@class="list"]/li/a/div[2]/h2')))
        price_all=self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//ul[@class="list"]/li/a/div[3]/span/b')))
        url_all=self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//ul[@class="list"]/li/a')))
        url_all=[url.get_attribute('href') for url in url_all]

        title = [x.text for x in adress_all]
        address=[]
        price =[x.text for x in price_all]
        url = [x for x in url_all]
        for i in title:
            a=i.split(' ')[1]
            address.append(a)
        self.data=zip(title, address, price, url)
        '''for i in self.data:
            print(i)'''



    def load_data(self):
        try:

            s=self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//div[@class="loadbtn "]')))
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')



        except TimeoutException:
            self.flag=False

    def save_data(self):
        self.db=mysqlHelper()
        temp=('title','address','price','url')
        for i in self.data:
            self.dic=dict(zip(temp,i))
            self.db.insert(self.dic)

    def find(self):
        db1=mysqlHelper()
        self.s=[]
        for i in db1.find():
            self.s.append(list(i))

    def write(self):
        with open('1.csv', 'a') as csvfile:
            temp=['id','title','address','price','url']
            writer=csv.writer(csvfile)
            writer.writerow(temp)
            writer.writerows(self.s)




    def run(self):
        self.browser_open()
        self.browser.get('https://bj.58.com/pinpaigongyu/?minprice=600_1000&area=10_30&pagetype=sub&PGTID=0d3111f6-0000-1c6a-cd38-8186a4f0c4f6&ClickID=1')
        time.sleep(1)
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

        while self.flag:
            self.load_data()
            time.sleep(3)
        else:
            print("所有房屋加载完成，开始爬取！")

        self.get_data()
        self.save_data()
        self.find()
        self.write()



if __name__=='__main__':
    spider=houseSipder()
    spider.run()
