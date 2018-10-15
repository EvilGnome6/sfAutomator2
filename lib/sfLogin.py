from lib import selFunctions as sel
import environment as env

def login():
	sel.initialize()
	sel.getUrl(env.login['url'])
	sel.sendKeysById(env.login['user'], 'username')
	sel.sendKeysById(env.login['pass'], 'password')
	sel.clickById('Login')