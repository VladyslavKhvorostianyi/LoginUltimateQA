import pytest
from  login_page import LoginPage
from selenium import webdriver
from configuration import *

@pytest.fixture(scope='module')
def login_page():
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get(URL_PAGE_UNDER_TEST)
	login_page = LoginPage(driver)
	yield login_page
	driver.close()


def test_correct_email_and_correct_password(login_page):
	login_page\
		.enter_email(EMAIL)\
		.enter_password(PASSWORD)\
		.click_login()\
		.assert_login_success()
		

def test_empty_email_and_empty_password(login_page):
	login_page\
		.enter_email('')\
		.enter_password('')\
		.click_login()\
		.assert_login_fail()
	
def test_invalid_email_and_correct_password(login_page):
	login_page\
		.enter_email(INVALID_EMAIL)\
		.enter_password(PASSWORD)\
		.click_login()\
		.assert_email_validation_error()
	
def test_correct_email_and_not_correct_password(login_page):
	login_page\
		.enter_email(EMAIL)\
		.enter_password(NOTCORRECT_PASSWORD)\
		.click_login()\
		.assert_login_fail()
	
def test_not_correct_email_and_correct_password(login_page):
	login_page\
		.enter_email(NOTCORRECT_EMAIL)\
		.enter_password(PASSWORD)\
		.click_login()\
		.assert_login_fail()
	
