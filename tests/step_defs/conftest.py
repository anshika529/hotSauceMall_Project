import pytest
from selenium import webdriver

url = 'https://www.hotsaucemall.com/hot-sauce.html'
create_account_url = 'https://www.hotsaucemall.com/checkout.html'


@pytest.fixture(scope="session")
def browser():
    br = webdriver.Chrome("/Users/anshikanegi/Downloads/chromedriver")
    br.maximize_window()
    br.implicitly_wait(10)
    yield br
    br.quit()
