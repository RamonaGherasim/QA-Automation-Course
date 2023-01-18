# Tema 9: Verificatori
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):
    form_auth = (By.LINK_TEXT, "Form Authentication")
    h2_element = (By.XPATH, '//h2')
    h4_element = (By.XPATH, '//h4')
    login_button = (By.XPATH, '//button[@type="submit"]')
    error = (By.ID, "flash")
    username_field = (By.ID, "username")
    pass_field = (By.ID, 'password')
    logout_button = (By.CSS_SELECTOR, "#content > div > a")
    error_close = (By.CLASS_NAME, "close")

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.get("https://the-internet.herokuapp.com/")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_1(self):
        self.chrome.find_element(*self.form_auth).click()
        time.sleep(3)
        current_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/login"
        assert current_url == expected_url, f"Error! Current url:{current_url}, expected url: {expected_url}"

    def test_2(self):
        current_title = self.chrome.title
        expected_title = "The Internet"
        assert current_title == expected_title, f"Error! Current title:{current_title}, expected title: {expected_title}"

    def test_3(self):
        self.chrome.get("https://the-internet.herokuapp.com/login")
        elem = self.chrome.find_element(*self.h2_element)
        current_elem_text = elem.text
        expected_elem_text = "Login Page"
        assert current_elem_text == expected_elem_text, f"Error! Current element text:{current_elem_text}, expected element text: {expected_elem_text}"

    def test_4(self):
        self.chrome.get("https://the-internet.herokuapp.com/login")
        actual_display = self.chrome.find_element(*self.login_button).is_displayed()
        assert actual_display, f"Error: login button is not displayed!"

    def test_5(self):
        self.chrome.get("https://the-internet.herokuapp.com/login")
        href_attr = self.chrome.find_element(By.LINK_TEXT, "Elemental Selenium").get_attribute("href")
        expected_href_attr = "http://elementalselenium.com/"
        assert href_attr == expected_href_attr, f"Error! Current href value:{href_attr}, expected href value: {expected_href_attr}"

    def test_6(self):
        self.chrome.get("https://the-internet.herokuapp.com/login")
        self.chrome.find_element(*self.login_button).click()
        er = WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located(self.error))
        error_display = er.is_displayed()
        assert error_display, f"Error: No Error message displayed!"

    def test_7(self):
        self.chrome.get("https://the-internet.herokuapp.com/login")
        self.chrome.find_element(*self.username_field).send_keys("Ramona")
        self.chrome.find_element(*self.pass_field).send_keys("12345")
        self.chrome.find_element(*self.login_button).click()
        er = WebDriverWait(self.chrome, 5).until(
            EC.presence_of_element_located(self.error))
        actual_error = er.text
        expected_error = "Your username is invalid!"
        self.assertTrue(expected_error in actual_error), f"Error: actual message {actual_error}, expected message {expected_error}"

    def test_8(self):
        self.chrome.get("https://the-internet.herokuapp.com/login")
        self.chrome.find_element(*self.login_button).click()
        er = WebDriverWait(self.chrome, 5).until(
            EC.presence_of_element_located(self.error_close))
        er.click()
        error_display = self.chrome.find_element(*self.error).is_displayed()
        time.sleep(2)
        assert error_display, "Error is still displayed!"

    def test_9(self):
        self.chrome.get("https://the-internet.herokuapp.com/login")
        labels = self.chrome.find_elements(By.TAG_NAME, "label")
        expected_text = ['Username', 'Password']
        actual_text = []
        for label in labels:
            actual_text.append(label.text)
        assert actual_text == expected_text, f"Error, actual labels: {actual_text}, expected labels: {expected_text} (have to be in this order)"

    def test_10(self):
        self.chrome.get("https://the-internet.herokuapp.com/login")
        self.chrome.find_element(*self.username_field).send_keys("tomsmith")
        self.chrome.find_element(*self.pass_field).send_keys("SuperSecretPassword!")
        self.chrome.find_element(*self.login_button).click()
        new_url = self.chrome.current_url
        assert new_url.__contains__("/secure"), f"New url does not contain the word '/secure'"
        msg = WebDriverWait(self.chrome, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "success")))
        assert msg.is_displayed(), "Success message not displayed!"
        assert msg.text.__contains__('secure area!'), "Success message does not contain 'secure area'"

    def test_11(self):
        self.chrome.get("https://the-internet.herokuapp.com/login")
        self.chrome.find_element(*self.username_field).send_keys("tomsmith")
        self.chrome.find_element(*self.pass_field).send_keys(
            "SuperSecretPassword!")
        self.chrome.find_element(*self.login_button).click()
        logout = WebDriverWait(self.chrome, 5).until(
            EC.presence_of_element_located(self.logout_button))
        logout.click()
        actual_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/login"
        assert actual_url == expected_url, f"Error: actual url {actual_url}, expected url {expected_url}"

    def test_12(self):
        self.chrome.get("https://the-internet.herokuapp.com/login")
        h4_text = self.chrome.find_element(*self.h4_element).text
        pass_text_list = h4_text.split()
        for word in pass_text_list:
            self.chrome.find_element(*self.username_field).send_keys(
                "tomsmith")
            self.chrome.find_element(*self.pass_field).send_keys(word)
            self.chrome.find_element(*self.login_button).click()
            if self.chrome.current_url.__contains__("/secure"):
                print(f"The secret password is {word}")
                break
            else:
                print("I cannot find the password")