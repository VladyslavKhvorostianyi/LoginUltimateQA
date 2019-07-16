class BasePage:
	
	url = None
	locator = None
	driver = None
	
	def __init__(self, driver):
		self.driver = driver
	
	def refresh(self):
		driver.get(self.url))
		return self