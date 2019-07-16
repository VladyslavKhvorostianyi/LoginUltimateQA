from selenium import webdriver
from configuration import PATH_TO_DRIVER

class Driver:

	def __init__(self):
		self.driver = webdriver.Chrome(executable_path=PATH_TO_DRIVER)