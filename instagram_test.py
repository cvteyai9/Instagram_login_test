#爬取IG關鍵字
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time
import wget
import allure
import pytest
import configparser as cp

filename = './config.ini'
inifile = cp.ConfigParser()
inifile.read(filename, 'UTF-8')

@pytest.mark.login
@allure.story("登入測試")
def test_login():
    driver = openBrowser()
    login(driver)
    # time.sleep(60)
    closeBrowser(driver)

@pytest.mark.information
@allure.story("個人資訊驗證")
def test_information():
    driver = openBrowser()
    login(driver)
    profile_inf(driver)
    inf_vertify(driver)
    closeBrowser(driver)

@allure.step("開啟瀏覽器")
def openBrowser():
    driver = webdriver.Chrome('C:/Users/TracK/AppData/Local/Programs/Microsoft VS Code/bin/chromedriver.exe')
    driver.get('https://www.instagram.com/')
    return driver

@allure.step("關閉瀏覽器")
def closeBrowser(driver):
    driver.quit()

@allure.step("登入")
def login(driver):
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    username.clear()
    password.clear()
    username.send_keys(inifile["profile"]["username"])
    password.send_keys(inifile["profile"]["password"])
    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]"))
    )
    login.click()

@allure.step("開啟個人資訊頁面")
def profile_inf(driver):
    waitbutton_1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button"))
    )
    waitbutton_1.click()
    waitbutton_2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"))
    )
    waitbutton_2.click()

@allure.step("核對個人資訊")
def inf_vertify(driver):
    proimg = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div[7]/div/div/a"))
    )
    proimg.click()
    title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/h1"))
    )
    information = title.text
    assert inifile["profile"]["id"] == information