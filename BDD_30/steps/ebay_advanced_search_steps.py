from behave import *


@when('Advanced search page: I type "{kwd_item}" in the keyword textbox')
def step_impl(context, kwd_item):
    context.advanced_search_page_object.enter_keywords_or_item_number(kwd_item)


@when('Advanced search page: I select "{kwd_option}" from keyword options')
def step_impl(context, kwd_option):
    context.advanced_search_page_object.select_keywords_options(kwd_option)


@when('Advanced search page: I type "{excluded_words}" in the exclude words '
      'from your search box')
def step_impl(context, excluded_words):
    context.advanced_search_page_object.exclude_words_from_search(excluded_words)


@when('Advanced search page: I select the "{category}" category')
def step_impl(context, category):
    context.advanced_search_page_object.select_search_category(category)


@when('Advanced search page: I click the search button')
def step_impl(context):
    context.advanced_search_page_object.click_search_button()
