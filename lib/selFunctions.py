from lib import utilities as utils
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def initialize():
    global driver
    chrome_options = Options()
    chrome_options.add_argument('--disable-notifications')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    # driver.set_window_position(0, 0)
    # driver.set_window_size(965, 1055)


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


def clickElement(element):
    try:
        element.clcik()
        return True
    except Exception:
        return False


def clickById(elementId):
    try:
        element = driver.find_element_by_id(elementId)
        element.click()
    except Exception:
        return False


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


def findChildByClassName(element, className):
    try:
        child = element.find_element_by_class_name(className)
        return child
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


def findElementById(elementId):
    try:
        element = driver.find_element_by_id(elementId)
        return element
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
        # If the label has an htmlFor attribute that is the elementId for the input field
        elementId = getElementAttribute(element, 'htmlFor')
        if (elementId is not False) and (elementId is not None):
            element = findElementById(elementId)
            # Determine the type of input field this is
            inputType = element.get_attribute('type')
            # Take the appropriate action based on type
            if inputType == 'text' or \
               inputType == 'tel' or \
               inputType == 'url':
                result = sendKeysElement(element, value)
                utils.log('    ' + field + ' = ' + value)
                return True
            elif inputType == 'checkbox':
                # Determine the status of the checkbox
                checked = element.get_attribute('checked')
                # If the status doesn't match, click the checkbox
                if checked != value:
                    element.click()
                    result = sendKeysElement(element, value)
                    utils.log('    ' + field + ' = ' + value)
            else:
                utils.log('Could not identify type of input field ' + inputType)
        # If there is no htmlFor attribute, this is a select box so we need to find the child field
        else:
            parent = element.find_element_by_xpath('parent::*')
            child = parent.find_element_by_class_name('select')
            child.click()
            for i in range(3):
                result = clickByLinkText(value)
                if result is True:
                    utils.log('    ' + field + ' = ' + value)
                    break
                else:
                    time.sleep(1)
        # Return result
        if result is True:
            return True
        else:
            return False
    except Exception:
        return False


def validateLightningForm(field, expectedValue):
    # Find the field label
    for i in range(30):
        element = findElementByClassNameAndAttribute('test-id__field-label', 'innerText', field)
        if element is not False:
            break
        else:
            time.sleep(1)
    # Move up to the parent element
    parent = element.find_element_by_xpath('parent::*')
    parent = parent.find_element_by_xpath('parent::*')
    # Search for the different child types
    childTypes = ['uiOutputText', 'uiOutputCheckbox', 'test-id__field-value']
    for childType in childTypes:
        child = findChildByClassName(parent, childType)
        if child is not False:
            break
    if childType == 'uiOutputCheckbox':
        if 'alt="True"' in child.get_attribute('innerHTML'):
            actualValue = 'true'
        else:
            actualValue = 'false'
    else:
        actualValue = child.get_attribute('innerText')
    if expectedValue == actualValue:
        result = 'Pass'
    else:
        result = 'Fail'
    utils.log('    Field: ' + field + ' | Expected: ' + expectedValue +
              ' | Actual: ' + actualValue + ' | Result: ' + result)
