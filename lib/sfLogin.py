from lib import selFunctions as sel
import environment as env

def login():
	sel.initialize()
	sel.getUrl(env.login['url'])