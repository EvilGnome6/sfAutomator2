from selenium import webdriver
import environment as env

def initialize():
	global driver
	driver = webdriver.Chrome()

def getUrl(url):
	driver.get(url)