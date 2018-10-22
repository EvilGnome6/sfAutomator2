from lib import parameters as pars
from lib import selFunctions as sel
import environment as env
import time


def new():
    print('Creating Account...')
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
    for field in pars.account:
        result = sel.fillLightningForm(field, pars.account[field])
        if result is False:
            print('Could not fill field: ' + field + ' with value: ' + pars.account[field])
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
    print('Created Account: ' + accountId + '\n')
    return accountId


def delete(accountId):
    print('Deleting Account...')
    sel.getUrl(env.login['url'] + '/' + accountId)
    # Click the Show more actions icon
    for i in range(10):
        result = sel.clickByClassNameAndAttribute('slds-icon-utility-down', 'innerText', 'Show more actions')
        if result is True:
            break
        else:
            time.sleep(1)
    if result is False:
        print('Could not click Show more Actions icon')
    # Click the Delete option
    for i in range(3):
        result = sel.clickByLinkText('Delete')
        if result is True:
            break
        else:
            time.sleep(1)
    if result is False:
        print('Could not click Delete option')
    # Click the Delete button
    for i in range(3):
        result = sel.clickByClassNameAndAttribute('forceActionButton', 'innerText', 'Delete')
        if result is True:
            break
        else:
            time.sleep(1)
    if result is True:
        print('Deleted Account: ' + accountId + '\n')
        return True
    else:
        print('Could not click Delete button')
        print('Could not delete Account: ' + accountId + '\n')
        return False
