from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from basepage import BasePage


class AdvancedSearch(BasePage):
    ENTER_KEYWORDS_OR_ITEM_NUMBER = (By.ID, "_nkw")
    KEYWORD_OPTIONS = (By.XPATH, '//select[@name="_in_kw"]')
    EXCLUDE_WORDS_FROM_SEARCH = (By.ID, '_ex_kw')
    SEARCH_CATEGORIES = (By.XPATH, '//div/span/select[@name="_sacat"]')
    SEARCH_BUTTON = (By.XPATH, '//div[5]/button')

    def enter_keywords_or_item_number(self, kwd_item):
        self.chrome.find_element(*self.ENTER_KEYWORDS_OR_ITEM_NUMBER).send_keys(kwd_item)

    def select_keywords_options(self, kwd_option):
        keyword_options_dropdown = Select(
            self.chrome.find_element(*self.KEYWORD_OPTIONS))
        keyword_options_dropdown.select_by_visible_text(kwd_option)

    def exclude_words_from_search(self, excluded_words):
        self.chrome.find_element(*self.EXCLUDE_WORDS_FROM_SEARCH).send_keys(excluded_words)

    def select_search_category(self, category):
        category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORIES))
        category_dropdown.select_by_visible_text(category)

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
