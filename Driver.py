from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from configuration import PATH_TO_DRIVER

class Driver:

	def __init__(self):
		self.driver = webdriver.Chrome(service=Service(executable_path=PATH_TO_DRIVER))