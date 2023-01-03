# XPATH Selectors
# = un alt mod de a identifica elementele

# /html/body/div[2]/div/div/form/div[1]/div/input  => Full XPATH (Absolut)
# = toate elementele de la root si pana la elementul selectat

# //*[@id="username"]  => XPATH (Relativ)
# cel mai des se utilizeaza XPATH si nu Full XPATH
# // => select current node
# * => (select all) tine locul unui tag cum ar fi: input, div, form, img precedat de [@atribut="valoare"]
# @ => select the attribut with the value ... Se foloseste doar cand folosim atribut
# Xpath=//tagname[@attribute='value']

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

test = webdriver.Chrome()
test.get("https://the-internet.herokuapp.com/login")

test.find_element(By.XPATH, '//*[@id="username"]').send_keys("Hello")
time.sleep(3)
test.find_element(By.XPATH, '//input[@type="password"]').send_keys("1234")
time.sleep(3)

# XPATH cu keywordul "contains"
test.find_element(By.XPATH, "//input[contains(@name,'pass')]").send_keys("1234")
time.sleep(3)

# XPATH selector dupa text()
test.find_element(By.XPATH, "//i[text()=' Login']").click()
time.sleep(2)

# //selected_item/parent::tag => cand vrem sa navigam in sus catre parinte
# //i[text()=" Login"]/parent::button
# Navigarea din parinte inspre copil se face cu /
# Navigarea catre un urmas care nu este urmas direct se face cu //
# Navigarea in sens invers (e.g frate anterior) /preceding-sibling::tag
# Navigarea la urmatorul frate /following-sibling::tag ex: //*[@id="username"]/preceding-sibling::label

test.find_element(By.XPATH, '//i[text()=" Login"]/parent::button')
test.find_element(By.XPATH, '//form[@name="login"]/div[1]//input').send_keys("12345")
time.sleep(2)


