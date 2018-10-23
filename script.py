from lib import sfAutomator as sf

# Log in to Salesforce
sf.login()

# Create new Account
account1 = sf.createAccount()

# Validate Account
sf.validateAccount(account1)

# Delete Account
sf.deleteAccount(account1)

# Log out of Salesforce
sf.logout()

print('Script Complete')
