# Folosirea librariei unittest

# Metoda de set-up => include toate preconditiile = pasi care se fac inainte de
# a executa testul in sine. Ex: instantiem un obiect, maximise si si get page

# Metoda de tear-down => toate activitatile care trebuie sa fie executate dupa
# test. Ex: inchiderea browser-ului

# Toate metodele de test trebuie sa aiba ca si prefix "test_"

# Se ruleaza testele in mod normal, din terminal sau click dreapta si run

# NOTA: libraria se instaleaza cu pip install pytest in terminal

# import unittest  # importa tot modulul. Aici clasa mosteneste din unittest.TestCase
# Sau se poate importa doar pachetul:
from unittest import TestCase  # in acest caz clasa mosteneste direct din TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class Alerts(TestCase):
    alert_button = (By.XPATH, '//*[text()="Click for JS Alert"]')
    confirm_button = (By.XPATH, '//*[text()="Click for JS Confirm"]')
    prompt_button = (By.XPATH, '//*[text()="Click for JS Prompt"]')
    alert_msg = (By.ID, "result")

    # Definirea metodei de setUp
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)

    # Definirea metodei de tearDown
    def tearDown(self) -> None:
        self.chrome.quit()

    def test_alert_accept(self):
        self.chrome.find_element(*self.alert_button).click()
        js_alert = self.chrome.switch_to.alert
        js_alert.accept()  # built-in method care accepta alerta e.g. da click pe buton
        actual_alert_msg = self.chrome.find_element(*self.alert_msg).text
        expected_alert_msg = "You successfully clicked an alert"
        assert actual_alert_msg == expected_alert_msg, f"Error: {expected_alert_msg}, actual {actual_alert_msg} "

        # self.chrome.find_element(*self.confirm_button).click()
        # self.chrome.find_element(*self.prompt_button).click()


