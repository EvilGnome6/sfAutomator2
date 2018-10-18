from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import environment as env

def initialize():
	global driver
	chrome_options = Options()
	chrome_options.add_argument('--disable-notifications')
	driver = webdriver.Chrome(chrome_options=chrome_options)
	driver.maximize_window()

def getUrl(url):
	driver.get(url)

def getTitle():
	return driver.title

def sendKeysById(keystring, elementId):
	element = driver.find_element_by_id(elementId)
	element.send_keys(keystring)

def clickById(elementId):
	element = driver.find_element_by_id(elementId)
	element.click()

def clickByClassNameAndAttribute(className, attribute, value):
	try:
		elements = driver.find_elements_by_class_name(className)
		for element in elements:
			if element.get_attribute(attribute) == value:
				element.click()
				return True
		return False
	except:
		return False