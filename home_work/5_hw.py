def test_page(a, b, c):
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    user_name = driver.find_elements(By.CSS_SELECTOR, a)
    pass_word = driver.find_elements(By.CSS_SELECTOR, b)
    sub_mit = driver.find_elements(By.CSS_SELECTOR, c)
    s = [a, b, c]
    count = 0
    for i in range(len(s)):
        if s[i] is None:
            continue
        else:
            count += 1
    if count == 3:
        return 'Элементы найдены'
    else:
        return 'Элементы не найдены'


print(test_page('user-name', 'password', 'login-button'))
