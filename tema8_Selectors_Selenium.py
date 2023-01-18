# Tema 8: Selectors

# ==== Imports ====
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

phptravels_page = webdriver.Chrome()
phptravels_page.get("https://phptravels.net/signup")

# By ID
# phptravels_page.find_element(By.ID, "flights-tab").click()
# phptravels_page.find_element(By.ID, "autocomplete").send_keys("London")
# phptravels_page.find_element(By.ID, "departure").clear()
#
# # By Link text
# phptravels_page.find_element(By.LINK_TEXT, "Hotels").click()
# time.sleep(2)
# phptravels_page.find_element(By.LINK_TEXT, "Offers").click()
# time.sleep(3)
# phptravels_page.find_element(By.LINK_TEXT, "Blog").click()
# phptravels_page.back()
# phptravels_page.back()
# phptravels_page.back()
# time.sleep(3)
#
# # By name
# phptravels_page.find_element(By.NAME, "checkin").click()
# time.sleep(3)
# phptravels_page.find_element(By.ID, "flights-tab").click()
# time.sleep(2)
# phptravels_page.find_element(By.NAME, "to").send_keys("Bucharest")
# time.sleep(3)
# phptravels_page.find_element(By.NAME, "trip").click()
# time.sleep(3)
#
# # By tag
# phptravels_page.find_elements(By.TAG_NAME, "button")[7].click()
# time.sleep(5)
# phptravels_page.find_elements(By.TAG_NAME, "span")[19].click()
# time.sleep(5)
# phptravels_page.find_elements(By.TAG_NAME, "i")[5].click()
# time.sleep(5)
#
#
# # By CSS ID
# phptravels_page.find_element(By.CSS_SELECTOR, "ul>li>button#hotels-tab").click()
#
# # By CSS class
# phptravels_page.find_element(By.CSS_SELECTOR, "input.checkin").click()
# time.sleep(3)
#
# # By CSS attribute = partial_value
# phptravels_page.find_element(By.CSS_SELECTOR, 'span > [id*="select2-hotels"]').click()
# time.sleep(3)
#
# # # Partial Link text
# phptravels_page.find_element(By.PARTIAL_LINK_TEXT, "Learn").click()
# time.sleep(5)

# phptravels_page.quit()



# By Partial Link text - continued
# the_internet = webdriver.Chrome()
# the_internet.get("https://the-internet.herokuapp.com/")
#
# the_internet.find_element(By.PARTIAL_LINK_TEXT, "Broken").click()
# time.sleep(2)
# the_internet.back()
# time.sleep(2)
# the_internet.find_element(By.PARTIAL_LINK_TEXT, "Challenging").click()
# time.sleep(2)
# time.sleep(2)
#
# # By class name
# the_internet.find_elements(By. CLASS_NAME, "button")[2].click()
# time.sleep(3)
# the_internet.find_elements(By. CLASS_NAME, "row")[4].click()
# time.sleep(3)
# the_internet.back()
#
#
# #  By XPATH- attribute and value
# the_internet.find_element(By.LINK_TEXT, "Forgot Password").click()
# time.sleep(2)
# the_internet.find_element(By.XPATH, "//*[@id='form_submit']").click()
# time.sleep(2)
# the_internet.back()
# time.sleep(2)
# the_internet.find_element(By.XPATH, "//input[@type='text']").send_keys("ramona@mail.com")
# time.sleep(3)
# the_internet.find_element(By.XPATH, "//button[@class='radius']").click()
# time.sleep(2)
# the_internet.back()
#
# # By XPATH - text on the element
# the_internet.find_element(By.XPATH, "//a[text()='Elemental Selenium']").click()
# time.sleep(3)
# the_internet.find_element(By.XPATH, "//i[text()='Retrieve password']").click()
# time.sleep(3)
# the_internet.back()
# the_internet.find_element(By.XPATH, "//*[text()='Forgot Password']").click()
# time.sleep(2)
# the_internet.back()
#
# # By XPATH - partial text
# the_internet.find_element(By.XPATH, "//a[contains(text(), 'WYS')]").click()
# time.sleep(2)
#
# # By XPATH - OR (| - using pipe)
# the_internet.find_element(By.XPATH, '//button[@title="Bold"] | //button[@title="Italic"]').click()
# time.sleep(2)
#
# # By XPATH[1]
# the_internet.find_element(By.XPATH, '(//button[@type="button"])[11]').click()
# time.sleep(2)
#
# # By XPATH  - parent::
# the_internet.find_element(By.XPATH, '//*[@id="mce_0_ifr"]//parent::div').click()
# time.sleep(3)
#
# # By XPATH - sibling::
# the_internet.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/div[1]/div[2]/div/div[3]/button[1]/following-sibling::button').click()
# time.sleep(3)
# the_internet.quit()


# BY XPATH - with function with param
phptravels_page = webdriver.Chrome()
phptravels_page.get("https://phptravels.net/signup")


def choose_element(label, input_value):
    input = phptravels_page.find_element(By.XPATH, f'//label[text()="{label}"]//parent::div//input')
    input.clear()
    input.send_keys(input_value)


def choose_element1(placeholder, input_value):
    input = phptravels_page.find_element(By.XPATH, f'//input[@placeholder="{placeholder}"]')
    input.clear()
    input.send_keys(input_value)


choose_element("First Name", "Ramona")
time.sleep(2)
choose_element("Last Name", "Gherasim")
time.sleep(2)
choose_element("Phone", "123")
time.sleep(2)
choose_element("Email", "ramona@yahoo.com")
time.sleep(2)

choose_element1("First Name", "Alexandra")
time.sleep(2)
choose_element1("Last Name", "Adela")
time.sleep(2)





