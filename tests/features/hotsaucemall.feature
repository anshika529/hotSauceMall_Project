#Feature: HotSauceMall web browsing
#  Scenario: Selecting product and adding to the cart
#    Given User on the HotSauceMall website
#    When User clicks on any product and add it to the cart
#    When User navigates to the Home page
#    When User will search for any product and add it to the cart
#    Then User will go to the cart and proceed checkout
#    Then User account will be created

  Scenario: Create new user Account
    Given User on the HotSauceMall website
    When User will fill all the required details for account creation and click on save
#    Then User Account should be created successfully