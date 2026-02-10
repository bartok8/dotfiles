#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
#import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from rakuten_credentials import *
from u_2021_01.lsturl import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 指定URLの楽天くじを引く関数 [楽天パンダのルーレットバージョンのみ対応]
def openRakutenLuckyKuji(pDriver, pURL):
    try:
        pDriver.get(pURL) # 楽天くじURLを開く
        time.sleep(5)
        #pDriver.find_element_by_xpath("//*[@id='entry']").click() # Startボタン
        pDriver.find_element(By.XPATH, "//*[@id='entry']").click() # Startボタン
        time.sleep(20) # ルーレットくじの待ち時間
    except NoSuchElementException:
        print("At {}".format(pURL))
        print("- NoSuchElementException発生 - 次の処理へ\n")
        time.sleep(1)

def openRakutenLuckyKuji2(pDriver, pURL):
    try:
        pDriver.get(pURL) # 楽天くじURLを開く
        time.sleep(5)
        #element = pDriver.find_element_by_xpath("//*[@id='entry']")
        element = pDriver.find_element(By.XPATH, "//*[@id='entry']")
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(element, 5, 5)
        action.click()
        action.perform()
        time.sleep(20) # ルーレットくじの待ち時間
    except NoSuchElementException:
        print("At {}".format(pURL))
        print("- NoSuchElementException発生 - 次の処理へ\n")
        time.sleep(1)

def login_rakuten(driver, pURL):        
    driver.get(pURL)
    time.sleep(5)

    # 楽天にログイン
    #elem_search_word = driver.find_element_by_id("loginInner_u")
    elem_search_word = driver.find_element(By.ID, "loginInner_u")
    #elem_search_word.send_keys("bartok8@gmail.com") # USER ID
    elem_search_word.send_keys(ID) # USER ID
    #elem_search_word = driver.find_element_by_id("loginInner_p")
    elem_search_word = driver.find_element(By.ID, "loginInner_p")
    #elem_search_word.send_keys("10823695") # USER PASSWORD
    elem_search_word.send_keys(PASS) # USER PASSWORD
    #driver.find_element_by_css_selector('input[type="submit"]').click()
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()


def login_rakuten_enavi(driver, pURL):
    driver.get(pURL)
#    print(driver.page_source)

    # iframes = driver.find_elements(By.TAG_NAME, "iframe")
    # print("iframe count:", len(iframes))
    # for i, f in enumerate(iframes):
    #     print(i, f.get_attribute("id"), f.get_attribute("name"), f.get_attribute("src"))

    # # input 要素を全部列挙
    # inputs = driver.find_elements(By.TAG_NAME, "input")
    # for i, inp in enumerate(inputs):
    #     print(i, inp.get_attribute("type"), inp.get_attribute("name"), inp.get_attribute("id"), inp.get_attribute("placeholder"))

    # buttons = driver.find_elements(By.TAG_NAME, "button")
    # for b in buttons:
    #     print("text:", b.text, "id:", b.get_attribute("id"), "class:", b.get_attribute("class"))

    # links = driver.find_elements(By.TAG_NAME, "a")
    # for i, a in enumerate(links):
    #     print(i, a.text, a.get_attribute("id"), a.get_attribute("class"))
        
    # divs = driver.find_elements(By.TAG_NAME, "div")
    # for i, d in enumerate(divs):
    #     txt = d.text.strip()
    #     if txt:
    #         print(i, txt, d.get_attribute("id"), d.get_attribute("class"))

    # divs = driver.find_elements(By.TAG_NAME, "div")
    # for d in divs:
    #     txt = d.text.strip()
    #     if txt:
    #         print("text:", txt, "id:", d.get_attribute("id"), "class:", d.get_attribute("class"))

    # divs = driver.find_elements(By.TAG_NAME, "div")
    # for d in divs:
    #     onclick = d.get_attribute("onclick")
    #     role = d.get_attribute("role")
    #     if onclick or role == "button":
    #         print("CLICKABLE:", d.text, "id:", d.get_attribute("id"), "class:", d.get_attribute("class"))            

    wait = WebDriverWait(driver, 15)


    wait.until(EC.presence_of_element_located((By.ID, "user_id")))

    # ユーザーID
    user_input = driver.find_element(By.ID, "user_id")
    user_input.clear()
    user_input.send_keys(ID)

    print("hoge1")

    # ログインボタン（推定: id="loginBtn"）
    login_button = driver.find_element(By.ID, "cta001")
    login_button.click()
    
    print("hoge11")    
    
    wait.until(EC.presence_of_element_located((By.ID, "user_id")))

    print("hoge2")

    time.sleep(5)
    
    # # input 要素を全部列挙
    # inputs = driver.find_elements(By.TAG_NAME, "input")
    # for i, inp in enumerate(inputs):
    #     print(i, inp.get_attribute("type"), inp.get_attribute("name"), inp.get_attribute("id"), inp.get_attribute("placeholder"))

    print("hoge3")        

#    wait.until(EC.presence_of_element_located((By.ID, "user_id")))

    print("hoge4")            
    
    # パスワード（推定: id="password" または name="password"）
#    pw_input = driver.find_element(By.ID, "password")
    pw_input = driver.find_element(By.ID, "password_current")
#    pw_input = driver.find_element(By.ID, "username")
    print("hoge5")                
    pw_input.clear()
    pw_input.send_keys(PASS)

    time.sleep(5)    
    print("hoge6")                    

#    wait.until(EC.presence_of_element_located((By.ID, "user_id")))

    # divs = driver.find_elements(By.TAG_NAME, "div")
    # for d in divs:
    #     onclick = d.get_attribute("onclick")
    #     role = d.get_attribute("role")
    #     if onclick or role == "button":
    #         print("CLICKABLE:", d.text, "id:", d.get_attribute("id"), "class:", d.get_attribute("class"))
    
    # ログインボタン（推定: id="loginBtn"）
    login_button = driver.find_element(By.ID, "cta011")
#    login_button = driver.find_element(By.ID, "cta001")
    login_button.click()

    print("hoge7")                        

    # ログイン後のページ読み込み待ち
    # time.sleep(5)

    # return driver        

def traverse_rakuten(driver):    
    # 楽天ログインページに移動
    url = "https://grp01.id.rakuten.co.jp/rms/nid/vc?__event=login&service_id=top"
    login_rakuten(driver, url)
    time.sleep(10)        
    for itemURL in lstURL:
        print("At {} ...".format(itemURL))
        openRakutenLuckyKuji2(driver, itemURL)
    
def traverse_rakuten_enavi(driver):
    lstURLenavi = [
        "https://kuji.rakuten.co.jp/256356cd1a", # rakuten card
    ]
    # 楽天enavi
    #url = "https://www.rakuten-card.co.jp/e-navi/index.xhtml"
    url = "https://www.rakuten-card.co.jp/e-navi/auth/login.xhtml"
    login_rakuten_enavi(driver, url)
    time.sleep(10)
    for itemURL in lstURLenavi:
        print("At enavi {} ...".format(itemURL))    
        openRakutenLuckyKuji2(driver, itemURL)

#
# top level
#
if __name__ == "__main__":
    # open chrome
    options =  webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    driver.set_window_size(1300,1040)

    traverse_rakuten(driver)
    traverse_rakuten_enavi(driver)
    
    # 処理終了
    driver.close

    print("traverse end")

# ends here.
