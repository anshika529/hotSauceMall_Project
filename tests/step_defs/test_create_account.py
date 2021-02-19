# import time
#
# from pytest_bdd import given, when, then, scenarios
# from conftest import create_account_url
# import selenium
#
# # from selenium.webdriver.support.select.Select
#
# scenarios('../features/hotsaucemall.feature')
#
#
# # @given("User on the HotSauceMall website")
# # def test_homepage(browser):
# #     browser.get(create_account_url)
#
#
# @when("User will fill all the required details for account creation and click on save")
# def test_user_details(browser):
#     browser.find_element_by_css_selector('a.button.bg--secondary.color--black.font--uppercase').click()
#     browser.find_element_by_css_selector('input#l-Customer_LoginEmail').send_keys('g@gmail.com')
#     browser.find_element_by_css_selector('input#l-Customer_Password').send_keys('xyz12345')
#     browser.find_element_by_css_selector('input#l-Customer_VerifyPassword').send_keys('xyz12345')
#     browser.find_element_by_css_selector('input#l-Customer_ShipFirstName').send_keys('xyz')
#     browser.find_element_by_css_selector('input#l-Customer_ShipLastName').send_keys('abc')
#     # browser.find_element_by_css_selector('input#l-Customer_ShipEmail').send_keys('a@gmail.com')
#     browser.find_element_by_css_selector('input#l-Customer_ShipPhone').send_keys('1234567809')
#     browser.find_element_by_css_selector('input#l-Customer_ShipAddress1').send_keys('mink')
#     browser.find_element_by_css_selector('input#l-Customer_ShipAddress2').send_keys('mink2')
#     browser.find_element_by_css_selector('input#l-Customer_ShipCity').send_keys('Calgary')
#     browser.find_element_by_css_selector('select#Customer_ShipCountry').send_keys("Canada")
#     browser.find_element_by_css_selector('input#l-Customer_ShipState').send_keys("Alberta")
#     browser.find_element_by_css_selector('input#l-Customer_ShipZip').send_keys('T9S')
#     # dropDownCountry.click()
#     # dropDownCountry.select_by_index(4)
#     # options = browser.find_elements_by_tag_name("option")
#     # for option in options:
#     #     option.click()
#     # country_field = browser.find_element_by_xpath('//*[@id="Customer_ShipCountry"]')
#     # country_field.send_keys("United States")
#     # sel= Select(browser.find_element_by_id("//*[@id="Customer_ShipCountry"]"))
#     # sel.select_by_visible_text('United States')
#     browser.find_element_by_css_selector('input#l-Customer_BillFirstName').send_keys('xyz')
#     browser.find_element_by_css_selector('input#l-Customer_BillLastName').send_keys('abc')
#     browser.find_element_by_css_selector('input#l-Customer_BillCompany').send_keys('qwerty')
#     browser.find_element_by_css_selector('input#l-Customer_BillEmail').send_keys('g@gmail.com')
#     browser.find_element_by_css_selector('input#l-Customer_BillPhone').send_keys('123456754')
#     browser.find_element_by_css_selector('input#l-Customer_BillAddress1').send_keys('mink1')
#     browser.find_element_by_css_selector('input#l-Customer_BillAddress2').send_keys('mink2')
#     browser.find_element_by_css_selector('input#l-Customer_BillCity').send_keys('Calgary')
#     browser.find_element_by_css_selector('select#Customer_BillCountry').send_keys('Canada')
#     browser.find_element_by_css_selector('input#l-Customer_BillState').send_keys('Alberta')
#     browser.find_element_by_css_selector('input#l-Customer_BillZip').send_keys('T9S')
#     browser.find_element_by_css_selector(
#         'input.button.button--large.bg--primary.color--black.font--uppercase.h-nb').click()
#     # time.sleep(10)
#
#
# @when("User will go to the cart and proceed check out")
# def test_cart_checkout(browser):
#     # click on continue shopping
#     browser.find_element_by_xpath('//*[@id="js-site-wrapper"]/main/div[2]/p/a').click()
#     # click on cart icon
#     time.sleep(10)
#
# # @when("User will click on continue to ship and pay")
# # def test_ship_and_pay(browser):
