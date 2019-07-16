import pytest
from  login_page import LoginPage
from selenium import webdriver


@pytest.fixture(scope='module')
def driver():
	driver = webdriver.Chrome()
	driver.maximize_window()
	yield driver
	driver.close()


def test_fail_login(driver):
	LoginPage(driver).refresh()