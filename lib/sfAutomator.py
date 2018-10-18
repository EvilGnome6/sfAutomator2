from lib import selFunctions as sel
from lib import sfAccount
from lib import sfLogin

def login():
	result = sfLogin.login()
	if result == False:
		print('Login failed')
		exit()
	elif result == True:
		print('Logged in\n')

def newAccount():
	sfAccount.new()