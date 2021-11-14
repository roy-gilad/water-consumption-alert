from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def aradReadYourMeter_scraping():
    user_name="nadavgil18@gmail.com"
    password="igo075UQ"
    s = Service("C:\Program Files (x86)\chromedriver.exe")

    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(10)  # seconds
    driver.get("https://cp.city-mind.com/Login.aspx")

    #insert user name and password to login
    search = driver.find_element(By.XPATH,'//*[@id="txtEmail"]').send_keys(user_name)
    search = driver.find_element(By.XPATH,'//*[@id="txtPassword"]').send_keys(password)
    driver.find_element(By.XPATH,'//*[@id="btnLogin"]').click()
    time.sleep(5)

    driver.find_element(By.XPATH,'//*[@id="tbl_meters_list"]/tbody/tr[5]/td[3]').click()
    time.sleep(5)

    driver.find_element(By.XPATH,'//*[@id="div_body_container"]/div/div[1]/div[4]/a/img').click()
    time.sleep(5)

    driver.find_element(By.XPATH,'//*[@id="btn_table"]').click()
    time.sleep(5)


    date = driver.find_element(By.XPATH,'//*[@id="div_consumption_grapth"]/table/tbody/tr[32]/td[1]')
    time.sleep(5)
    water_consum = driver.find_element(By.XPATH,'//*[@id="div_consumption_grapth"]/table/tbody/tr[32]/td[2]')
    time.sleep(5)




    print(water_consum.text)
    print(date.text)
    return [date.text,water_consum.text]


    time.sleep(10)
    driver.quit()

