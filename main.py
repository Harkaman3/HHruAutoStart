from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import pickle
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome('chromedriver.exe')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://spb.hh.ru/account/login?backurl=%2F&hhtmFrom=main')
sleep(5)
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
sleep(3)
driver.refresh()
sleep(10)
driver.get('https://spb.hh.ru/applicant/resumes?hhtmFrom=resume_list&hhtmFromLabel=header')
sleep(2)
while True:

    try: 
        elem = driver.find_element(By.XPATH,'//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div[1]/div[3]/div[2]/div/div[6]/div/div/div/div[1]/span/button')
        elem.click()
    except NoSuchElementException:
        sleep(3600)
        driver.refresh()
        pass
    