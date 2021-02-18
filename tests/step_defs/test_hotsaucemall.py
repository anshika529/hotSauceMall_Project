import random
import time

from pytest_bdd import given, when, scenarios, then
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from conftest import url

scenarios('../features/hotsaucemall.feature')


@given("User on the HotSauceMall website")
def test_homepage(browser):
    browser.get(url)


@when("User clicks on any product and add it to the cart")
def test_click_and_add_product(browser):
    links = browser.find_elements_by_css_selector('a.mm-card-grid-item__text')
    l = links[random.randint(0, len(links) - 1)]
    l.click()
    browser.find_element_by_css_selector(
        'button.button.button--medium.bg--primary.color--black.font--bold.font--uppercase.h-nb').click()
    # btn = browser.find_elements_by_css_selector('button.button.button--medium.bg--primary.color--black.font--bold.font--uppercase.h-nb')
    # btn.click()
    # list = browser.find_element_by_tag_name("a")
    # l = list[random.Random(0, len(list))]
    # l.click()

    # browser.find_element_by_css_selector('a.mm-card-grid-item__text').click()
    # browser.find_element_by_xpath('//*[@id="js-purchase-product"]/div[9]/button').click()
    # Alert(browser).dismiss()
    # action = ActionChains(browser)
    # browser.find_element_by_xpath("/html/body/div[1]/main/div[4]/section/article/form/div[9]/button").click()


@when("User navigates to the Home page")
def test_navigate_to_homepage(browser):
    # browser.find_element_by_css_selector('.column whole.nav.ul li>a').click()
    browser.find_element_by_css_selector('ul.breadcrumbs.font--medium.font--uppercase li').click()

    # sys.stdout.flush()
    # sleep(180)
    # browser.find_element_by_xpath('//*[@id="js-site-wrapper"]/main/div[1]/section/nav/ul/li[1]/a')


@when("User will search for any product and add it to the cart")
def test_search_add_product(browser):
    btn = browser.find_element_by_xpath('//*[@id="js-site-wrapper"]/header/div[2]/div/div[2]/button')
    btn.click()
    # time.sleep(10)
    # input_element = browser.find_element_by_xpath('//*[@id="l-search"]')
    # input_element.clear()
    # input_element = browser.find_element_by_css_selector("input[name^='Search']")
    # input_element.clear()
    # input_element.send_keys('PERI')
    # input_element.send_keys(keys.ENTER)
    # time.sleep(30)
    browser.find_element_by_xpath('//*[@id="l-search"]').send_keys('PERI')
    # time.sleep(10)
    # ip.submit()
    browser.find_element_by_xpath('//*[@id="l-search"]').send_keys(Keys.RETURN)
    # selecting product randomly
    links = browser.find_elements_by_css_selector('a.mm-card-grid-item__text')
    l = links[random.randint(0, len(links) - 1)]
    l.click()
    # click add to cart
    browser.find_element_by_css_selector(
        'button.button.button--medium.bg--primary.color--black.font--bold.font--uppercase.h-nb').click()
    time.sleep(60)
    # time.sleep(10)


@then("User will go to the cart and proceed checkout")
def test_cart_checkout(browser):
    browser.find_element_by_xpath('//*[@id="js-PROD"]/div[2]/div/div[1]/div/button').click()
    # time.sleep(60)
    # click on cart icon
    browser.find_element_by_xpath('//*[@id="js-site-wrapper"]/header/div[2]/div/div[5]/a').click()
    # click on check out button
    browser.find_element_by_xpath('//*[@id="js-site-wrapper"]/header/div[4]/div/div/div[7]/a').click()
    # time.sleep(10)
    browser.execute_script("window.scrollBy(0, 350)")
    # secure check out button
    # time.sleep(10)
    browser.find_element_by_css_selector('.column.whole>a.button.button--block.button--large.bg--primary.color--black.font--bold.font--uppercase.h-nb').click()
    time.sleep(10)
