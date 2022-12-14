# Curs 10
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

test = webdriver.Chrome()
test.get("https://the-internet.herokuapp.com/login")

# TAG Selector
test.find_element(By.TAG_NAME, 'form')
time.sleep(5)

# CSS Selector
# Atunci cand inlantuim elemente deja facem CSS selection
# Putem folosi > e.g. form >div => toti copiii div directi de sub form
# form div => toti copiii div sub form
# form >div [type="text"]
test.find_element(By.CSS_SELECTOR, "form >div [type='text']").send_keys("Ramona")
time.sleep(3)


# CSS Selectors Using :nth-of-type   => al catalea element de tipul x
# form > div:nth-of-type(1)  # primul div copil direct al elem form
# form > div:nth-of-type(2)
# test.find_element(By.CSS_SELECTOR, "form > div:nth-of-type(1) input").clear()
test.find_element(By.CSS_SELECTOR, "form > div:nth-of-type(1) input").send_keys(Keys.CONTROL + 'a')  # tot face clear dar trimitand keys
test.find_element(By.CSS_SELECTOR, "form > div:nth-of-type(1) input").send_keys("Alexandra")
time.sleep(5)

# CSS Selectors using :first-of-type sau :last-of-type
# Ex: form > div :last-of-type input
test.find_element(By.CSS_SELECTOR, "form > div:last-of-type input").send_keys("Hello")
time.sleep(3)
test.find_element(By.CSS_SELECTOR, "form > div:first-of-type input").clear()
test.find_element(By.CSS_SELECTOR, "form > div:first-of-type input").send_keys("Roro")
time.sleep(3)

# XPATH Selector
test.close()
