from pytest_bdd import given, when, then, scenarios
from conftest import create_account_url
import selenium
# from selenium.webdriver.support.select.Select

scenarios('../features/hotsaucemall.feature')


@given("User on the HotSauceMall website")
def test_homepage(browser):

    browser.get(create_account_url)


@when("User will fill all the required details for account creation and click on save")
def test_user_details(browser):
    browser.find_element_by_xpath('//*[@id="js-site-wrapper"]/main/section/div/div[2]/p[2]/a').click()
    browser.find_element_by_xpath('//*[@id="l-Customer_LoginEmail"]').send_keys('xyz@gmail.com')
    browser.find_element_by_xpath('//*[@id="l-Customer_Password"]').send_keys('xyz12345')
    browser.find_element_by_xpath('//*[@id="l-Customer_VerifyPassword"]').send_keys('xyz12345')
    browser.find_element_by_xpath('//*[@id="l-Customer_ShipFirstName"]').send_keys('xyz')
    browser.find_element_by_xpath('//*[@id="l-Customer_ShipLastName"]').send_keys('abc')
    browser.find_element_by_xpath('//*[@id="l-Customer_ShipEmail"]').send_keys('xyz@gmail.com')
    browser.find_element_by_xpath('//*[@id="l-Customer_ShipPhone"]').send_keys('1234567809')
    browser.find_element_by_xpath('//*[@id="l-Customer_ShipAddress1"]').send_keys('mink')
    browser.find_element_by_xpath('//*[@id="l-Customer_ShipAddress2"]').send_keys('mink2')
    browser.find_element_by_xpath('//*[@id="l-Customer_ShipCity"]').send_keys('Perth')
    # country_field = browser.find_element_by_xpath('//*[@id="Customer_ShipCountry"]')
    # country_field.send_keys("United States")
    # sel= Select(browser.find_element_by_id("//*[@id="Customer_ShipCountry"]"))
    # sel.select_by_visible_text('United States')

    # browser.find_element_by_xpath("")
    # browser.find_element_by_xpath("")
    # browser.find_element_by_xpath("")
    browser.find_element_by_xpath('//*[@id="l-Customer_BillFirstName"]').send_keys('xyz')
    browser.find_element_by_xpath('//*[@id="l-Customer_BillLastName"]').send_keys('abc')
    browser.find_element_by_xpath('//*[@id="l-Customer_BillCompany"]').send_keys('qwerty')
    browser.find_element_by_xpath('//*[@id="l-Customer_BillEmail"]').send_keys('xyz@gmail.com')
    browser.find_element_by_xpath('//*[@id="l-Customer_BillPhone"]').send_keys('123456754')
    browser.find_element_by_xpath('//*[@id="l-Customer_BillAddress1"]').send_keys("mink1")
    browser.find_element_by_xpath('//*[@id="l-Customer_BillAddress2"]').send_keys('mink2')
    browser.find_element_by_xpath('//*[@id="l-Customer_BillCity"]').send_keys('Perth')
#     browser.find_element_by_xpath("")
#     browser.find_element_by_xpath("")
#     browser.find_element_by_xpath('//*[@id="js-site-wrapper"]/main/div[3]/section/div/div/form/div[3]/div/input').click()
#
#
# @then("User Account should be created successfully")
# def test_account_created(browser):
#     assert 'inventory' in browser.current_url
