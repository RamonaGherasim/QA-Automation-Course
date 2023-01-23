
# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
s = Service(ChromeDriverManager().install()) #modalitate prin care noi putem sa ddescarcam driverul de browser in online
chrome = webdriver.Chrome(service=s) #modialitate prin care noi putem sa deschidem browserul. programul pe care il rulam va gasi driverul care a fost descarcat, il va folosi pt a lansa brrowseru iar serviciul de browser lansat il va salva int-o cutiuta numita Chrome.


# maximizam fereastra
chrome.maximize_window()


# navigam catre un url
chrome.get('https://the-internet.herokuapp.com/login')
sleep(3)

chrome.find_element(By.ID, "username").send_keys("tomsmith")
sleep(3)

#<input type="password" name="password" id="password">
chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
sleep(3)

#Log in button's Full XPATH: /html/body/div[2]/div/div/form/button/i
chrome.find_element(By.XPATH, "//button[@type='submit']").click()
sleep(3)

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)