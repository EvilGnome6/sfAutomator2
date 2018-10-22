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
            result = True
        else:
            time.sleep(1)
    if result is False:
        print('Login failed\n')
        exit()
    elif result is True:
        print('Logged in\n')
