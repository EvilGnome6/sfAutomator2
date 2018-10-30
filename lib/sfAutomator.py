from lib import sfAccount
from lib import sfLogin
from lib import utilities as utils


# sfAccount Functions
def createAccount(accountType):
    result = sfAccount.create(accountType)
    return result


def deleteAccount(accountId):
    result = sfAccount.delete(accountId)
    return result


def validateAccount(accountId, values):
    result = sfAccount.validate(accountId, values)
    return result


# sfLogin functions
def login():
    result = sfLogin.login()
    return result


def logout():
    result = sfLogin.logout()
    return result


# utilities functions
def setupLogFile():
    result = utils.setupLogFile()
    return result
