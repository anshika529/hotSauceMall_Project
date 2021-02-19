import random
import time

from pytest_bdd import given, when, scenarios, then
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from conftest import url

scenarios('../features/hotsaucemall.feature')


@given("User on the HotSauceMall website")
def home_page(browser):
    browser.get(url)
    time.sleep(2)


@when("User clicks on any product")
def click_any_product(browser):
    # randomly click on any product from homepage
    links = browser.find_elements_by_css_selector('a.mm-card-grid-item__text')
    startint = 0
    endint = 11
    links[random.randint(startint,endint)].click()
    time.sleep(2)


@when("User clicks on add to cart")
def click_add_to_cart(browser):
    # Click on add to cart button
    a = browser.find_element_by_css_selector('button.button.button--medium.bg--primary.color--black.font--bold.font--uppercase.h-nb')
    a.click()
    browser.find_element_by_xpath('//*[@id="js-PROD"]/div[2]/div/div[1]/div/button').click()
    time.sleep(10)


@when("User navigates to the Home page")
def navigate_to_homepage(browser):
    # click on Home
    b = browser.find_element_by_css_selector('ul.breadcrumbs.font--medium.font--uppercase li')
    b.click()
    time.sleep(2)


@when("User will search a product and press enter")
def search_product(browser):
    # click on search icon
    btn = browser.find_element_by_xpath('//*[@id="js-site-wrapper"]/header/div[2]/div/div[2]/button')
    btn.click()
    time.sleep(2)
    # pass value in search box
    browser.find_element_by_xpath('//*[@id="l-search"]').send_keys('PERI')
    # press enter
    browser.find_element_by_xpath('//*[@id="l-search"]').send_keys(Keys.RETURN)
    time.sleep(2)


@when("User will click Randomly on one product")
def random_click_product(browser):
    # selecting product randomly
    links = browser.find_elements_by_css_selector('a.mm-card-grid-item__text')
    startint = 0
    endint = 11
    links[random.randint(startint,endint)].click()
    time.sleep(2)


@when("User will click on add to cart button")
def add_to_cart(browser):
    # click add to cart
    browser.find_element_by_css_selector(
        'button.button.button--medium.bg--primary.color--black.font--bold.font--uppercase.h-nb').click()
    time.sleep(10)


@when("User will click on cart icon")
def click_cart_icon(browser):
    # click on cart icon
    browser.find_element_by_xpath('//*[@id="js-site-wrapper"]/header/div[2]/div/div[5]/a').click()
    time.sleep(2)


# @when("Verify the no. of products in the cart")
# def verify_products_in_cart(browser):
#     elements = browser.find_elements_by_xpath('//*[@id="js-site-wrapper"]/header/div[2]/div/div[5]/a/span').text
# #     elements = elements.text
#     print(elements)
#     time.sleep(2)


@when("User will click on checkout")
def click_checkout(browser):
    # click on check out button
    browser.find_element_by_xpath('//*[@id="js-site-wrapper"]/header/div[4]/div/div/div[7]/a').click()
    time.sleep(2)


@when("User will click on secure checkout")
def click_secure_checkout(browser):
    # scroll
    browser.execute_script("window.scrollBy(0, 350)")
    # secure check out button
    browser.find_element_by_css_selector(
        '.column.whole>a.button.button--block.button--large.bg--primary.color--black.font--bold.font--uppercase.h-nb').click()
    time.sleep(2)

@when("User will click on create new account button")
def click_create_account(browser):
    browser.find_element_by_css_selector('a.button.bg--secondary.color--black.font--uppercase').click()
    time.sleep(2)


@when("User will fill all the required details for account creation")
def user_details(browser):
    #email
    browser.find_element_by_css_selector('input#l-Customer_LoginEmail').send_keys('piii@gmail.com')
    browser.find_element_by_css_selector('input#l-Customer_Password').send_keys('xyz12345')
    browser.find_element_by_css_selector('input#l-Customer_VerifyPassword').send_keys('xyz12345')
    browser.find_element_by_css_selector('input#l-Customer_ShipFirstName').send_keys('xyz')
    browser.find_element_by_css_selector('input#l-Customer_ShipLastName').send_keys('abc')
    # browser.find_element_by_css_selector('input#l-Customer_ShipEmail').send_keys('a@gmail.com')
    browser.find_element_by_css_selector('input#l-Customer_ShipPhone').send_keys('1234567809')
    browser.find_element_by_css_selector('input#l-Customer_ShipAddress1').send_keys('mink')
    browser.find_element_by_css_selector('input#l-Customer_ShipAddress2').send_keys('mink2')
    browser.find_element_by_css_selector('input#l-Customer_ShipCity').send_keys('Calgary')
    browser.find_element_by_css_selector('select#Customer_ShipCountry').send_keys("Canada")
    browser.find_element_by_css_selector('input#l-Customer_ShipState').send_keys("Alberta")
    browser.find_element_by_css_selector('input#l-Customer_ShipZip').send_keys('T9S')
    browser.find_element_by_css_selector('input#l-Customer_BillFirstName').send_keys('xyz')
    browser.find_element_by_css_selector('input#l-Customer_BillLastName').send_keys('abc')
    browser.find_element_by_css_selector('input#l-Customer_BillCompany').send_keys('qwerty')
    # email
    browser.find_element_by_css_selector('input#l-Customer_BillEmail').send_keys('piii@gmail.com')
    browser.find_element_by_css_selector('input#l-Customer_BillPhone').send_keys('123456754')
    browser.find_element_by_css_selector('input#l-Customer_BillAddress1').send_keys('mink1')
    browser.find_element_by_css_selector('input#l-Customer_BillAddress2').send_keys('mink2')
    browser.find_element_by_css_selector('input#l-Customer_BillCity').send_keys('Calgary')
    browser.find_element_by_css_selector('select#Customer_BillCountry').send_keys('Canada')
    browser.find_element_by_css_selector('input#l-Customer_BillState').send_keys('Alberta')
    browser.find_element_by_css_selector('input#l-Customer_BillZip').send_keys('T9S')
    time.sleep(2)

@when("User will click on save")
def click_save(browser):
    browser.find_element_by_css_selector(
        'input.button.button--large.bg--primary.color--black.font--uppercase.h-nb').click()
    time.sleep(2)


@when("User will click on continue to shopping")
def continue_to_Shopping(browser):
# click on continue the shopping
    browser.find_element_by_xpath('//*[@id="js-site-wrapper"]/main/div[2]/p/a').click()
    time.sleep(2)


@when('User will go to the cart')
def click_cart(browser):
    # click on cart icon
    browser.find_element_by_xpath('//*[@id="js-site-wrapper"]/header/div[2]/div/div[5]/a').click()
    time.sleep(2)


@when("User will click on checkout button")
def click_checkout(browser):
    # click on check out button
    check = browser.find_element_by_css_selector(
        '.column.whole.medium-half.medium-offset-half.large-one-third.large-offset-two-thirds.global-mini-basket-drawer__wrap>div.row.bg--white>div.column.whole>a.button.button--block.button--large.button--square.bg--primary.color--black.font--bold.font--uppercase')
    check.click()
    time.sleep(2)


@when("User will click on secure checkout button")
def click_secure_checkout(browser):
    # scroll
    browser.execute_script("window.scrollBy(0, 350)")
    # secure check out button
    browser.find_element_by_css_selector(
        '.column.whole>a.button.button--block.button--large.bg--primary.color--black.font--bold.font--uppercase.h-nb').click()
    time.sleep(2)


@when("User will click on continue to ship")
def continue_to_ship(browser):
    # continue to ship
    browser.execute_script("window.scrollBy(0, 350)")
    browser.find_element_by_xpath(
        '//*[@id="js-site-wrapper"]/main/div[3]/section[2]/div[3]/div/ul/li/div/form/div[3]/div/input').click()
    time.sleep(2)


@when("User will click on continue to pay")
def continue_to_pay(browser):
    # continue to pay
    browser.execute_script("window.scrollBy(0, 350)")
    browser.find_element_by_xpath(
        '//*[@id="js-site-wrapper"]/main/div[3]/section[2]/div[3]/div/div[3]/div/button').click()
    time.sleep(2)