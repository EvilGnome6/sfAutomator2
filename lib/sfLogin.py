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
			return False
		elif sel.getTitle() == 'Verify Your Identity | Salesforce':
			return False
		elif sel.getTitle() == 'Home | Salesforce':
			return True
		else: time.sleep(1)
	return False