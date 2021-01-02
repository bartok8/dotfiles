#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import chromedriver_binary
from rakuten_credentials import *
from u_2021_01.lsturl import *


# 指定URLの楽天くじを引く関数 [楽天パンダのルーレットバージョンのみ対応]
def openRakutenLuckyKuji(pDriver, pURL):
    try:
        pDriver.get(pURL) # 楽天くじURLを開く
        time.sleep(5)
        pDriver.find_element_by_xpath("//*[@id='entry']").click() # Startボタン
        time.sleep(20) # ルーレットくじの待ち時間
    except NoSuchElementException:
        print("At {}".format(pURL))
        print("- NoSuchElementException発生 - 次の処理へ\n")
        time.sleep(1)


def openRakutenLuckyKuji2(pDriver, pURL):
    try:
        pDriver.get(pURL) # 楽天くじURLを開く
        time.sleep(5)
        element = pDriver.find_element_by_xpath("//*[@id='entry']")
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(element, 5, 5)
        action.click()
        action.perform()
        time.sleep(20) # ルーレットくじの待ち時間
    except NoSuchElementException:
        print("At {}".format(pURL))
        print("- NoSuchElementException発生 - 次の処理へ\n")
        time.sleep(1)

        

#--
#　Chromeを開く
#webdriverpath = "/Chrome webdriverへのパス/" # Webdriver Path
options =  webdriver.ChromeOptions()
#driver = webdriver.Chrome(webdriverpath)
driver = webdriver.Chrome()
driver.set_window_size(1300,1040)

lstURLenavi = [
    "https://kuji.rakuten.co.jp/256356cd1a", # rakuten card
]

# 楽天トップページに移動
url = "https://www.rakuten.co.jp"
driver.get(url)

# 楽天ログインページに移動
url = "https://grp01.id.rakuten.co.jp/rms/nid/vc?__event=login&service_id=top"
driver.get(url)
time.sleep(5)

# 楽天にログイン
elem_search_word = driver.find_element_by_id("loginInner_u")
#elem_search_word.send_keys("bartok8@gmail.com") # USER ID
elem_search_word.send_keys(ID) # USER ID
elem_search_word = driver.find_element_by_id("loginInner_p")
#elem_search_word.send_keys("10823695") # USER PASSWORD
elem_search_word.send_keys(PASS) # USER PASSWORD
driver.find_element_by_css_selector('input[type="submit"]').click()
time.sleep(10)

# 楽天ラッキーくじのURLリストを開く
for itemURL in lstURL:
#    openRakutenLuckyKuji(driver, itemURL)
    openRakutenLuckyKuji2(driver, itemURL)


# 楽天enavi
url = "https://www.rakuten-card.co.jp/e-navi/index.xhtml"
driver.get(url)
time.sleep(5)


#user_id = "bartok8@gmail.com"
#password = "10823695"

# ログイン画面のユーザー欄にユーザIDを入力
driver.find_element_by_name('u').send_keys(ID)

# ログイン画面のパスワード欄にパスワードを入力
driver.find_element_by_name('p').send_keys(PASS)

# ログインボタンを押下する
driver.find_element_by_id('loginButton').click()

time.sleep(10)

for itemURL in lstURLenavi:
    openRakutenLuckyKuji2(driver, itemURL)



# # login to enavi
# elem_search_word = driver.find_element_by_id("u_placeholder")
# elem_search_word.send_keys("bartok8@gmail.com") # USER ID
# elem_search_word = driver.find_element_by_id("p_placeholder")
# elem_search_word.send_keys("10823695") # USER PASSWORD

# #element = driver.find_element_by_css_selector('input[type="submit"]')
# element = driver.find_element_by_id("loginButton")
# print("hoge1")
# action = webdriver.common.action_chains.ActionChains(driver)
# print("hoge2")
# action.move_to_element_with_offset(element, 5, 5)
# print("hoge3")
# action.click()
# print("hoge4")
# action.perform()
# print("hoge5")
    
# 処理終了
driver.close

print("くじ引きが終わりました！")


