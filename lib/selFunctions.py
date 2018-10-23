from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def initialize():
    global driver
    chrome_options = Options()
    chrome_options.add_argument('--disable-notifications')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver.maximize_window()
    driver.set_window_position(0, 0)
    driver.set_window_size(965, 1055)


def getCurrentUrl():
    return driver.current_url


def getUrl(url):
    driver.get(url)


def getTitle():
    return driver.title


def sendKeysById(elementId, keystring):
    try:
        element = driver.find_element_by_id(elementId)
        element.send_keys(keystring)
        return True
    except Exception:
        return False


def sendKeysElement(element, keystring):
    try:
        element.send_keys(keystring)
        return True
    except Exception:
        return False


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
    except Exception:
        return False


def clickByLinkText(linkText):
    try:
        element = driver.find_element_by_link_text(linkText)
        element.click()
        return True
    except Exception:
        return False


def findElementByClassNameAndAttribute(className, attribute, value):
    try:
        elements = driver.find_elements_by_class_name(className)
        for element in elements:
            if element.get_attribute(attribute) == value:
                return element
        return False
    except Exception:
        return False


def getElementAttribute(element, attribute):
    try:
        value = element.get_attribute(attribute)
        return value
    except Exception:
        return False


def fillLightningForm(field, value):
    try:
        # Find the label for the field
        elements = driver.find_elements_by_class_name('label')
        for element in elements:
            if element.get_attribute('innerText') == field or \
               element.get_attribute('innerText') == (field + '*') or \
               element.get_attribute('innerText') == (field + '\n*'):
                    break
        # If the label has an htmlFor attribute
        # that is the elementId for the input field
        elementId = getElementAttribute(element, 'htmlFor')
        if (elementId is not False) and (elementId is not None):
            result = sendKeysById(elementId, value)
            print('    ' + field + ' = ' + value)
            return True
        # If not, this is a select box so we need to find the child field
        else:
            parent = element.find_element_by_xpath('parent::*')
            child = parent.find_element_by_class_name('select')
            child.click()
            for i in range(3):
                result = clickByLinkText(value)
                if result is True:
                    print('    ' + field + ' = ' + value)
                    break
                else:
                    time.sleep(1)

        if result is True:
            return True
        else:
            return False
    except Exception:
        return False
