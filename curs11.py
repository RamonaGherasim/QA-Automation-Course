# Curs 11:
# Implicit wait => e ca un wait global, si are prioritate. Se foloseste o
# singura data la inceputul programului

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test = webdriver.Chrome()
# test.implicitly_wait(5)  # Se activeaza doar atunci cand elementele pe care le
# cautam nu sunt gasite. Atunci sistemul va astepta timp de 5 secunde.

test.get("https://the-internet.herokuapp.com/login")
test.maximize_window()  # Maximizeaza fereastra

test.find_element(By.ID, "username").send_keys("tomsmith")
# time.sleep(5)

pas = WebDriverWait(test, 5).until(EC.presence_of_element_located((By.ID, "password")))
pas.send_keys("SuperSecretPassword!")

# Sau cu ajutorul lui find
# test.find_element(By.ID, "passwordas").send_keys("SuperSecretPassword!")
# time.sleep(5)

