import dotenv
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

dotenv.load_dotenv()

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

driver.get('http://tcafe2a.com/')
driver.implicitly_wait(3)

driver.find_element(By.ID, 'ol_id').send_keys(os.getenv('T_CAFE_ID'))
driver.find_element(By.ID, 'ol_pw').send_keys(os.getenv('T_CAFE_PW'))

driver.find_element(By.CLASS_NAME, 'ol_wr').find_element(
    By.TAG_NAME, 'button').click()

driver.get('http://tcafe2a.com/community/attendance')

driver.execute_script('GoGoGo()')

driver.close()
driver.quit()
