from selenium import webdriver
from os import path

class Driver:

	def __init__(self):
		self.driver = webdriver.Chrome(executable_path=path.join(path.abspath(__file__),'resources','chromedriver'))