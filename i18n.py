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


def scripts():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-images")
    chrome_options.add_argument("--disable-javascript")
    # chrome_options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(options=chrome_options)
    url = 'http://192.168.2.95:8700/#/login'
    chrome_driver.get(url)
    user = 'admin'
    password = 'xcmg@zks'

    # 登录
    chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/span[1]/input').clear()
    chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/span[1]/input').send_keys(
        user)
    #
    chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/span[2]/input').clear()
    chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/span[2]/input').send_keys(
        password)
    chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/button').click()

    print("登录成功")
    # 获取txt文件
    filepath1 = "./ch.txt"
    filepath2 = "./en.txt"
    with open(filepath1, 'r', encoding='utf-8') as file:
        # 读取文件内容
        chh = file.read()
    with open(filepath2, 'r', encoding='utf-8') as file:
        # 读取文件内容
        enn = file.read()

    # 正则表达式模式
    pattern = r'([^=\n]+)=([^=\n]+)'
    # 提取键值对
    chs = re.findall(pattern, chh)
    ens = re.findall(pattern, enn)
    chsd = {K: V for K, V in chs}
    ensd = {K: V for K, V in ens}

    # 开始循环
    print("开始循环")
    wait = WebDriverWait(chrome_driver, 10)
    n = 0
    for i in chs:
        n += 1

        if ensd.get(i[0]):
            code = i[0]
            ch = i[1]
            en = ensd.get(i[0])
            # code = n
            # ch = n
            # en = n
            # 打开左侧界面

            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/ul/li/ul/li[2]/a')))
            element.click()

            add = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/section/div/div/div/div[2]/button')))
            add.click()

            # 使用显式等待等待元素可见
            # 执行操作

            code_input = wait.until(EC.presence_of_element_located((By.ID, 'code')))
            zh_input = wait.until(EC.presence_of_element_located((By.ID, 'zh')))
            en_input = wait.until(EC.presence_of_element_located((By.ID, 'en')))

            code_input.clear()
            code_input.send_keys(code)
            zh_input.clear()
            zh_input.send_keys(ch)
            en_input.clear()
            en_input.send_keys(en)

            wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]'))).click()

            # headers = {
            #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
            #                   'Chrome/124.0.0.0 Safari/537.36',
            #     'Hots': '192.168.2.95:8700'
            # }
            # resp = requests.get("http://192.168.2.95:8700/prod-api/biz/i18nLanguage/save", headers=headers)
            # print(resp.json())

            if wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div'))):
                wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[1]'))).click()
            wait.until(EC.invisibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div')))
            print(str(n)+":complete!")
            # break
    chrome_driver.quit()


if __name__ == '__main__':
    scripts()
