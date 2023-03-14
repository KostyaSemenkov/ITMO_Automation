from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('htttps://demoqa.com/')
icon = driver.find_elements(By.CSS_SELECTOR, '#app > header > a > img')
footer = driver.find_elements(By.CSS_SELECTOR, 'span')
button = driver.find_elements(By.CSS_SELECTOR, '#app > div > div > div.home-body > div > div')
s = [icon, footer, button]
for i in range(len(s)):
    if s[i] is None:
        print('Элемент не найден')
    else:
        print('Элемент найден')