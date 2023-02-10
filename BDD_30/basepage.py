from browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage(Browser):
    def wait_and_click_element(self, selector):
        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located(selector))
        self.chrome.find_element(*selector).click()

    def accept_cookies(self):
        self.chrome.find_element(By.ID, '#gdpr-banner-accept').click()

