from selenium import webdriver

if __name__ == '__main__':
    url = 'http://pythonscraping.com'
    driver = webdriver.PhantomJS(executable_path='/usr/local/phantomjs/bin/phantomjs')
    driver.get(url)
    driver.implicitly_wait(1)
    print(driver.get_cookies())