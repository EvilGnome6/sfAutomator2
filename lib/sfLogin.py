from lib import selFunctions as sel
import environment as env
import time


def login():
    print('Logging in...')
    sel.initialize()
    sel.getUrl(env.login['url'])
    sel.sendKeysById('username', env.login['user'])
    sel.sendKeysById('password', env.login['pass'])
    sel.clickById('Login')
    for i in range(10):
        if sel.getTitle() == 'Login | Salesforce':
            result = False
            break
        elif sel.getTitle() == 'Verify Your Identity | Salesforce':
            result = False
            break
        elif sel.getTitle() == 'Home | Salesforce':
            time.sleep(1)
            result = True
        else:
            time.sleep(1)
    if result is False:
        print('Login failed\n')
        exit()
    elif result is True:
        print('Logged in\n')


def logout():
    print('Logging out...')
    sel.getUrl(env.login['url'])
    # Wait for Home page to load
    for i in range(30):
        if sel.getTitle() == 'Home | Salesforce':
            time.sleep(1)
            break
        else:
            time.sleep(1)
    # Click View profile icon
    for i in range(30):
        result = sel.clickByClassNameAndAttribute('branding-userProfile-button', 'innerText', 'View profile')
        if result is True:
            time.sleep(1)
            break
        else:
            time.sleep(1)
    # Click Log Out link
    for i in range(30):
        result = sel.clickByLinkText('Log Out')
        if result is True:
            break
        else:
            time.sleep(30)
    # Wait for Login page to load
    for i in range(30):
        if sel.getTitle() == 'Login | Salesforce':
            result = True
            break
        else:
            time.sleep(1)
    # Log result and return
    if result is True:
        print('Logged out\n')
        return True
    else:
        print('Logout failed')
        return False
