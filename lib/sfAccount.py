from lib import parameters as pars
from lib import selFunctions as sel
import environment as env
import time

def new():
	print('Creating new Account...')
	#Open the Accounts page
	sel.getUrl(env.login['url'] + '/lightning/o/Account/home')
	#Click on the New Button
	for i in range(10):
		result = sel.clickByClassNameAndAttribute('forceActionLink', 'text', 'New')
		if result == True: break
		else: time.sleep(1)
	#Wait for the New Account form to load
	for i in range(10):
		result = sel.findElementByClassNameAndAttribute('test-id__section-header-title', 'innerHTML', 'Account Information') 
		if result == True: break
		else: time.sleep(1)
	#Send account parameters to form
	for field in pars.account:
		result = sel.fillLightningForm(field, pars.account[field])
		if result == False:
			print('Could not fill field: ' + field + ' with value: ' + pars.account[field])