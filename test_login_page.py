import pytest
import login_page
import driver


def test_try():
	login_page.LoginPage(driver.Driver()).refresh()