from lib import selFunctions as sel
import environment as env
import time

def new():
	sel.getUrl(env.login['url'] + '/lightning/o/Account/home')
	for i in range(10):
		result = sel.clickByClassNameAndAttribute('slds-button', 'innerText', 'New')
		if result == True: break
		else: time.sleep(1)