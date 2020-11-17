#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import chromedriver_binary
from rakuten_credentials import *

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

# 楽天くじ URLリスト [楽天パンダのルーレットバージョン]
lstURL = [
    "https://kuji.rakuten.co.jp/1243541a35", # travel
    "https://kuji.rakuten.co.jp/66435bd268", # takara kuji
    "https://kuji.rakuten.co.jp/6e7329f994", # syouken
    "https://kuji.rakuten.co.jp/35b1b242c7", # blog
    "https://kuji.rakuten.co.jp/5c5ccb5",    # blog2
    "https://kuji.rakuten.co.jp/6ab2af6810", # infoseek sp
    "https://kuji.rakuten.co.jp/2a836b2e57", # gurunavi
    "https://kuji.rakuten.co.jp/14d330d3e0", # hoken no sougou madoguchi
    "https://kuji.rakuten.co.jp/79021454e7", # recipi
    "https://kuji.rakuten.co.jp/4351057845/?scid=wi_grp_gmx_too_rjl", # web search
    "https://kuji.rakuten.co.jp/9d91da42ab?scid=su_53", # infoseek poinavi
    "https://kuji.rakuten.co.jp/147369f4d8?scid=su_10831", # beauty
    "https://kuji.rakuten.co.jp/69334ccff1", # syaken
    "https://kuji.rakuten.co.jp/d9135bc12d", # toto
    "https://kuji.rakuten.co.jp/643377c7a5?scid=su_8289", # deliverly
    "https://kuji.rakuten.co.jp/bec377e2d5", # deliverly?
    "https://kuji.rakuten.co.jp/9ea32a8dfa", # calendar
    #"https://kuji.rakuten.co.jp/1b628755e1", # edy
    "https://kuji.rakuten.co.jp/7393386d27", # pay
    "https://kuji.rakuten.co.jp/18584163d?scid=wi_grp_gmx_fds_kuji", # fudousan
    "https://kuji.rakuten.co.jp/46211bf9dd", # tv
    "https://kuji.rakuten.co.jp/42136c5d7d", # books
    #"https://www.infoseek.co.jp/Luckylot", # infoseek
    "https://kuji.rakuten.co.jp/6432148795", # recipi sp

    # additional...
    "https://point.rakuten.co.jp/doc/lottery/lucky/", #pointclub appli lucky kuji
    "https://kuji.rakuten.co.jp/c2d372fbbe", # smaho sakana
    "https://kuji.rakuten.co.jp/490372ef94", # smaho sakana
    "https://kuji.rakuten.co.jp/68b371ed7d", # koko hore
    "https://kuji.rakuten.co.jp/b9436b1ddd", # gurunavi sp
    "https://kuji.rakuten.co.jp/2a836b2e57", # gurunavi sp
    "https://kuji.rakuten.co.jp/ffa36a07d3", # beauty
    "https://kuji.rakuten.co.jp/34d356d5d5", # reward
    "https://kuji.rakuten.co.jp/a24364f880", # point club
    "https://kuji.rakuten.co.jp/6233615e79", # omikuji miko
    "https://kuji.rakuten.co.jp/4ad36145c2", # lucky kuji
    "https://kuji.rakuten.co.jp/69334ccff1", # syaken
    "https://kuji.rakuten.co.jp/1473379bb1", # point club
    "https://kuji.rakuten.co.jp/bb63377557", # energy
    "https://kuji.rakuten.co.jp/eff3376c7a", # energy
    "https://kuji.rakuten.co.jp/7a1321943c", # lucky kuji
    "https://kuji.rakuten.co.jp/a29321bc36", # lucky kuji
    "https://kuji.rakuten.co.jp/ad1321af05", # lucky kuji
    "https://kuji.rakuten.co.jp/34e2cb79fa", # calendar
    "https://kuji.rakuten.co.jp/b312abddc5", # 
    "https://kuji.rakuten.co.jp/8212abcffe", # syousya gentei
    "https://kuji.rakuten.co.jp/4592a41e4c", # smaho lucky
    "https://kuji.rakuten.co.jp/d141c5441b", # books
    "https://kuji.rakuten.co.jp/ffc1c52299", # books

    "https://kuji.rakuten.co.jp/b3c3746f95", # 2020/11/4 marathon   
    
#    "https://kuji.rakuten.co.jp/ad********", # Rakuten ラッキーくじ
#    "https://kuji.rakuten.co.jp/ff********", # 楽天ブックスくじ
#    "https://kuji.rakuten.co.jp/46********", # Rakuten TVくじ
#    ....
#     ※【楽天】ラッキーくじ一覧ページからURLを確認して、ここに記述します
#    ....
]

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


