from lib import sfAutomator as sf

sf.login()
account1 = sf.newAccount()
sf.deleteAccount(account1)


print('Script Complete')
