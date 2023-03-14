from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
user_name = driver.find_elements(By.CSS_SELECTOR, 'user-name')
pass_word = driver.find_elements(By.CSS_SELECTOR, 'password')
sub_mit = driver.find_elements(By.CSS_SELECTOR, 'login-button')
s = [user_name, pass_word, sub_mit]
for i in range(len(s)):
    if s[i] is None:
        print('Элемент не найден')
    else:
        print('Элемент найден')