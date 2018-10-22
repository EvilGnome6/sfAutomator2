from lib import sfAccount
from lib import sfLogin


# Login functions
def login():
    result = sfLogin.login()
    return result


# Account Functions
def newAccount():
    result = sfAccount.new()
    return result


def deleteAccount(accountId):
    result = sfAccount.delete(accountId)
    return result
