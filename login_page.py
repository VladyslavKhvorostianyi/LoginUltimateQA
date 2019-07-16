from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions, wait


class LoginPage:
	
	def __init__(self, driver):
		self.driver = driver
		
	def enter_email(self, email):
		email_elem = self.driver.find_element(By.ID, 'user_email')
		email_elem.clear()
		email_elem.click()
		email_elem.send_keys(email)
		return self
			
		
	def enter_password(self, password):
		password_elem = self.driver.find_element(By.ID, 'user_password')
		password_elem.clear()
		password_elem.click()
		password_elem.send_keys(password)
		return self
		
	def click_login(self):
		login_button = self.driver.find_element(By.ID, 'btn-signin')
		login_button.click()
		return self
		
	def assert_login_fail(self):
		pass
		
	def assert_email_validation_error(self):
		pass
		
	def assert_login_success(self):
		pass
		