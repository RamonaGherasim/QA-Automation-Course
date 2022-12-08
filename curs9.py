# Curs 9
import time

from selenium import webdriver

from selenium.webdriver.common.by import By

# Locators in Selenium: ID, name, class name, tag name, partial link text, link text, CSS Selectors, xPath

# ID => se selecteaza cu #


chrome_page = webdriver.Chrome()  # .Chrome este clasa din pachetul Selenium
chrome_page.get("https://the-internet.herokuapp.com/login")  # accesarea paginii html dorite
# time.sleep(5)  # parametrul este in secunde

chrome_page.find_element(By.ID, "username").send_keys("Ramona")  # tipareste "Ramona" in field-ul "Username" din browser

chrome_page.find_element(By.ID, "password").send_keys("ramona1")
time.sleep(5)

chrome_page.find_element(By.TAG_NAME, "button").click()
time.sleep(5)

chrome_page.find_element(By.LINK_TEXT, "Elemental Selenium").click()  # link text => stringul care este intre <a>_!</a>
time.sleep(3)


chrome_page.quit()  # metoda aceasta inchide toata instanta browser-ului => de preferat
# chrome_page.close()  # metoda aceasta inchide un singur tab (cel activ din instanta de browser)
# !! Inchide instanta browser-ului atunci cand termini de testat pe pagina !!




