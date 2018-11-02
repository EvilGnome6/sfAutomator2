from lib import parameters as pars
from lib import selFunctions as sel
from lib import utilities as utils
import environment as env
import time


def create(parameters):
    utils.log('Creating Account...')
    # Open the Accounts page
    sel.getUrl(env.login['url'] + '/lightning/o/Account/home')
    # Click on the New Button
    for i in range(10):
        result = sel.clickByClassNameAndAttribute('forceActionLink', 'text', 'New')
        if result is True:
            break
        else:
            time.sleep(1)
    # Wait for the New Account form to load
    for i in range(3):
        result = sel.findElementByClassNameAndAttribute(
            'test-id__section-header-title', 'innerHTML', 'Account Information')
        if result is True:
            break
        else:
            time.sleep(1)
    # Send account parameters to form
    for field in pars.account[parameters['accountType']]:
        result = sel.fillLightningForm(field, pars.account[parameters['accountType']][field])
        if result is False:
            utils.log('Could not fill field: ' + field + ' with value: ' +
                      pars.account[parameters['accountType']][field])
    # Click Save
    result = sel.clickByClassNameAndAttribute('forceActionButton', 'innerText', 'Save')
    # Wait until the page loads, extract the account ID from the URL and return it
    for i in range(10):
        url = sel.getCurrentUrl()
        if '/view' in url:
            break
        else:
            time.sleep(1)
    accountId = url.split('/')[-2]
    utils.log('Created Account: ' + accountId + '\n')
    pars.account[parameters['accountHandle']] = accountId
    return True


def delete(parameters):
    utils.log('Deleting Account...')
    sel.getUrl(env.login['url'] + '/' + pars.account[parameters['accountHandle']])
    # Click the Show more actions icon
    for i in range(10):
        result = sel.clickByClassNameAndAttribute('slds-icon-utility-down', 'innerText', 'Show more actions')
        if result is True:
            break
        else:
            time.sleep(1)
    if result is False:
        utils.log('Could not click Show more Actions icon')
    # Click the Delete option
    for i in range(3):
        result = sel.clickByLinkText('Delete')
        if result is True:
            break
        else:
            time.sleep(1)
    if result is False:
        utils.log('Could not click Delete option')
    # Click the Delete button
    for i in range(10):
        result = sel.clickByClassNameAndAttribute('forceActionButton', 'innerText', 'Delete')
        if result is True:
            break
        else:
            time.sleep(1)
    if result is True:
        utils.log('Deleted Account: ' + pars.account[parameters['accountHandle']] + '\n')
        return True
    else:
        utils.log('Could not click Delete button')
        utils.log('Could not delete Account: ' + pars.account[parameters['accountHandle']] + '\n')
        return False


def validate(parameters):
    utils.log('Validating Account ' + pars.account[parameters['accountHandle']] + ' ...')
    # Start logging results
    utils.results('Validate Account:,' + pars.account[parameters['accountHandle']])
    utils.results('Field,Expected,Actual,Result')
    # Navigate to the Account page
    sel.getUrl(env.login['url'] + '/' + pars.account[parameters['accountHandle']])
    # Click the Details tab
    for i in range(30):
        result = sel.clickByLinkText('Details')
        if result is True:
            break
        else:
            time.sleep(1)
    # Initialize the test result, validate account parameters and log result
    pars.testResult = 'Pass'
    skipList = ['accountHandle']
    for field in parameters:
        if field not in skipList:
            result = sel.validateLightningForm(field, parameters[field])
    utils.results('Result:,' + pars.testResult + '\n')
    utils.log('    Result: ' + pars.testResult)
    utils.log('Account ' + pars.account[parameters['accountHandle']] + ' validated\n')
