import time
import requests
import urllib
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    start_time = time.time()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-images")
    chrome_options.add_argument("--diaable-javascript")
    chrome_driver = webdriver.Chrome(options=chrome_options)
    url = 'https://account.xiaomi.com/fe/service/login/password?_qrsize=180&sid=mi_eshop&qs=%253Fcallback%253Dhttp' \
          '%25253A%25252F%25252Forder.mi.com%25252Flogin%25252Fcallback%25253Ffollowup%25253Dhttps%2525253A%2525252F' \
          '%2525252Fwww.mi.com%2525252Findex.html%252526sign' \
          '%25253DMjM0MWU0NjBlOTU1YzY4NGQzOTc3MDk4N2M2MjQ5Y2ZiZTMxNTFlZQ%25252C%25252C%2526sid%253Dmi_eshop' \
          '%2526_qrsize%253D180&callback=http%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F' \
          '%252Fwww.mi.com%252Findex.html%26sign%3DMjM0MWU0NjBlOTU1YzY4NGQzOTc3MDk4N2M2MjQ5Y2ZiZTMxNTFlZQ%2C%2C&_sign' \
          '=c0455AmnySfgSTjnQ4ptPssEzGw%3D&serviceParam=%7B%22checkSafePhone%22%3Afalse%2C%22checkSafeAddress%22' \
          '%3Afalse%2C%22lsrp_score%22%3A0.0%7D&showActiveX=false&theme=&needTheme=false&bizDeviceType=&_locale=zh_CN'
    chrome_driver.get(url)

    user = '17374131136'
    password = 'zyqq1234'
    print("开始登录")

    chrome_driver.find_element(By.NAME, "account").clear()
    chrome_driver.find_element(By.NAME, "account").send_keys(user)

    chrome_driver.find_element(By.NAME, "password").clear()
    chrome_driver.find_element(By.NAME, "password").send_keys(password)

    chrome_driver.find_element(By.CLASS_NAME, "ant-checkbox-input").click()
    #
    chrome_driver.find_element(By.CLASS_NAME, "mi-button").click()
    print(time.time() - start_time)
    time.sleep(5)
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                   'Chrome/124.0.0.0 Safari/537.36',
    #     'Hots': 'movie.douban.com'
    # }
