from lib import sfAccount
from lib import sfLogin
from lib import utilities as utils


# sfAccount Functions
def createAccount(parameters):
    result = sfAccount.create(parameters)
    return result


def deleteAccount(parameters):
    result = sfAccount.delete(parameters)
    return result


def validateAccount(parameters):
    result = sfAccount.validate(parameters)
    return result


# sfLogin functions
def login():
    result = sfLogin.login()
    return result


def logout():
    result = sfLogin.logout()
    return result


# utilities functions
def init(parameters):
    result = utils.init(parameters)
    return result
