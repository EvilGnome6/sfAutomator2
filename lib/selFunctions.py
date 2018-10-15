from selenium import webdriver
import environment as env

def initialize():
	global driver
	driver = webdriver.Chrome()

def getUrl(url):
	driver.get(url)

def sendKeysById(keystring, elementId):
	element = driver.find_element_by_id(elementId)
	element.send_keys(keystring)

def clickById(elementId):
	element = driver.find_element_by_id(elementId)
	element.click()