# Tema 10: Verificari Extra

import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TheInternetFirefox(TestCase):
    SLIDER_PAGE = (By.LINK_TEXT, "Horizontal Slider")
    SLIDER = (By.XPATH, '//input[@type="range"]')
    SLIDER_VALUE = (By.ID, "range")
    FOOTER_LINK = (By.LINK_TEXT, "Elemental Selenium")

    def setUp(self) -> None:
        self.page = webdriver.Firefox()
        self.page.get("https://the-internet.herokuapp.com/")
        self.page.maximize_window()
        self.page.implicitly_wait(5)

    def tearDown(self) -> None:
        self.page.quit()

    def test_go_to_slider_page(self):
        self.page.find_element(*self.SLIDER_PAGE).click()
        expected_url = "https://the-internet.herokuapp.com/horizontal_slider"
        actual_url = self.page.current_url
        assert actual_url == expected_url, f"Error: actual ural: {actual_url}," \
                                           f"expected url: {expected_url}"

    def test_slider_display(self):
        self.page.find_element(*self.SLIDER_PAGE).click()
        is_displayed = self.page.find_element(*self.SLIDER).is_displayed()
        assert is_displayed, "Error, slider is not displayed!"

    def test_move_slider(self):
        self.page.find_element(*self.SLIDER_PAGE).click()
        elem = self.page.find_element(*self.SLIDER)
        elem.send_keys(Keys.ARROW_RIGHT)
        expected_value = "0.5"
        actual_value = self.page.find_element(*self.SLIDER_VALUE).text
        assert actual_value == expected_value, f"Error: actual value: {actual_value}, " \
                                               f"expected value: {expected_value}"

    def test_footer_link(self):
        self.page.find_element(*self.SLIDER_PAGE).click()
        link = self.page.find_element(*self.FOOTER_LINK)
        expected_href = "http://elementalselenium.com/"
        actual_href = link.get_attribute("href")
        assert actual_href == expected_href, f"Error: actual ural: {actual_href}," \
                                           f"expected url: {expected_href}"

    def test_footer_link_opens_in_new_tab(self):
        self.page.find_element(*self.SLIDER_PAGE).click()
        link = self.page.find_element(*self.FOOTER_LINK)
        link.click()
        # If the current URL is the same, it means the link has opened in a
        # different tab
        expected_url = "https://the-internet.herokuapp.com/horizontal_slider"
        actual_url = self.page.current_url
        assert actual_url == expected_url, f"Error: actual ural: {actual_url}," \
                                           f"expected url: {expected_url}"

        # OR it could be done by using the target attribute
        # expected_value = "_blank"
        # actual_value = link.get_attribute("target")
        # assert actual_value == expected_value, f"Error: actual value: {actual_value}," \
        #                                        f"expected value: {expected_value}"



