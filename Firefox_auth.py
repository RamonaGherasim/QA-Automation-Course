# Login interactiv (ca un pop up)
# Ne folosim de url si adaugam username si parola in url
# eg. https://username:parola@rest_of_the_url


from unittest import TestCase  # in acest caz clasa mosteneste direct din TestCase
from selenium import webdriver


class Firefox(TestCase):
    USERNAME = 'admin'
    PASSWORD = 'admin'

    def setUp(self) -> None:
        self.firefox = webdriver.Firefox()
        self.firefox.maximize_window()

    def tearDown(self) -> None:
        self.firefox.quit()

    def test_auth(self):
        self.firefox.get(
            "https://" + self.USERNAME + ':' + self.PASSWORD + "@the-internet.herokuapp.com/basic_auth")