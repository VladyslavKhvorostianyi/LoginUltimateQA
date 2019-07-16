from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions, wait


class LoginPage:
	
	def __init__(self, driver):
		self.driver = driver
		
	def enter_email(self, email):
		email = self.driver.find_element(By.ID, 'user_email')
		email.send_keys(email)
			
		
	def enter_password(self, password):
		password = self.driver.find_element(By.ID, 'user_password')
		password.send_keys(password)
		
	def click_login(self):
		login_button = self.driver.find_element(By.ID, 'btn-signin')
		login_button.click()
		
	def assert_login_fail(self):
		pass
		
	def assert_email_validation_error(self):
		pass
		
	def assert_login_success(self):
		pass
		
	//*[@id="user_email"]