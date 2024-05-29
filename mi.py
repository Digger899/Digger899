import time
import requests
import urllib
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re


class XiaoMi():
    def __init__(self, account: str, password: str):
        self.account = account
        self.password = password
        self.option = webdriver.ChromeOptions()
        self.option.add_argument("--disable-images")
        self.option.add_argument("--disable-javascript")
        self.option.add_argument("--disable-gpu")
        self.option.add_argument("--no-sandbox")
        self.option.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=self.option)

    def login(self):
        url = 'https://www.mi.com/index.html'
        self.driver.get(url)
        self.driver.find_element(By.CLASS_NAME, "user-name").click()
        time.sleep(3)
        # self.driver.find_element((By.NAME, 'account')).clear()
        self.driver.find_element(By.NAME, 'account').send_keys(self.account)

        # self.driver.find_element((By.NAME, 'password')).clear()
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)

        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.CSS_SELECTOR, ".ant-checkbox-input").click()

        self.driver.find_element(By.XPATH, '//*[@id="rc-tabs-0-panel-login"]/form/div[1]/button').click()
        time.sleep(3)

        print("登录成功")
        self.buy('https://www.mi.com/shop/buy/detail?product_id=19709')

    def buy(self, Product_link):
        self.driver.find_element(By.XPATH, '//*[@id="header-wrapper"]/div/nav[1]/div[2]/a').click()
        time.sleep(3)
        self.driver.find_element(By.ID, 'search').send_keys("Redmi K70 Pro")
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, "lxml")
        print(soup.find_all("a"))
        time.sleep(5)

def scripts():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-images")
    chrome_options.add_argument("--disable-javascript")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(options=chrome_options)
    url = 'https://account.xiaomi.com'
    chrome_driver.get(url)
    page_source = chrome_driver.page_source
    soup = BeautifulSoup(page_source, "lxml")
    input_coms = soup.find_all('input')
    print([ic for ic in input_coms])
    if len(input_coms) > 0:
        user = '17374131136'
        password = 'zyqq1234'
        #
        # 登录
        # chrome_driver.find_element((By.NAME, 'account')).clear()
        chrome_driver.find_element(By.NAME, 'account').send_keys(user)
        #
        # chrome_driver.find_element((By.NAME, 'password')).clear()
        chrome_driver.find_element(By.NAME, 'password').send_keys(password)

        chrome_driver.find_element(
            (By.CSS_SELECTOR, "button.mi-button.mi-button--primary.mi-button--fullwidth")).click()
        chrome_driver.find_element(
            (By.CSS_SELECTOR, "button.mi-button.mi-button--primary.mi-button--fullwidth")).click()
        print("登录成功")
    # time.sleep(10)


if __name__ == '__main__':
    XiaoMi('17374131136', 'zyqq1234').login()
