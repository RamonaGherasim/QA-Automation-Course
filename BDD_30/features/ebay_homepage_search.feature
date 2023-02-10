Feature: Test the search functionality of the ebay homepage

  Background:
    Given Home page: I am on ebay homepage

  @T1 @regression @BDD
  Scenario Outline: Check that the user can make a simple search in the Ebay homepage
    When Home page: I search for "<product_name>" in "<category_name>"
    Then Home page: I have at least "<nr_of_results>" results returned

    @cell_phones
    Examples:
      | product_name | category_name             | nr_of_results |
      | iphone       | Cell Phones & Accessories | 1000          |
      | samsung      | Cell Phones & Accessories | 1000          |

    @electronics
    Examples:
      | product_name | category_name        | nr_of_results |
      | LED          | Consumer Electronics | 1000          |
      | TV           | Consumer Electronics | 1000          |

    @clothes
    Examples:
      | product_name | category_name                 | nr_of_results |
      | dress        | Clothing, Shoes & Accessories | 1000          |
      | sweater      | Clothing, Shoes & Accessories | 1000          |


  @T2 @functional @BDD
  Scenario Outline: Check that the user can make an advanced search for a product
    When Home page: When I click on the advanced link
    When Advanced search page: I type "<kwd_item>" in the keyword textbox
    When Advanced search page: I select "<kwd_option>" from keyword options
    When Advanced search page: I type "<excluded_words>" in the exclude words from your search box
    When Advanced search page: I select the "<category>" category
    When Advanced search page: I click the search button
    Then Home page: I have at least "<nr_of_results>" results returned

    Examples:
      | kwd_item     | kwd_option               | excluded_words | category        | nr_of_results |
      | pampers      | Exact words, exact order | size           | Baby            | 200           |
      | hiking boots | Exact words, any order   | kids           | Sporting Goods  | 500           |
      | K-beauty     | Any words, any order     | men            | Health & Beauty | 1000          |