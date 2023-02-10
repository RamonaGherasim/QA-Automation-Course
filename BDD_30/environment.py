from browser import Browser
from pages.ebay_homepage import HomePage
from pages.ebay_advanced_search_page import AdvancedSearch


# before_all este o metoda recunoscuta de libraria behave si care se va executa
# inainte de toate testele
def before_all(context):
    # Context este ca o cutiuta in care vom stoca toate atributele ce pot fi
    # folosite in alte fisiere

    context.browser = Browser()
    context.home_page_object = HomePage()
    context.advanced_search_page_object = AdvancedSearch()


# after_all este o metoda recunoscuta de libraria behave si care se va executa
# dupa toate testele
def after_all(context):
    context.browser.close()