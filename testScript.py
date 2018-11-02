from lib import sfAutomator as sf
# from lib import parameters as pars
# import os

# Set up the Log File
sf.init({
    'testName': 'testScript',
})
# pars.logFile = os.path.basename(__file__)
# sf.setupLogFile()

# Log in to Salesforce
sf.login()

# Create new Account
sf.createAccount({
    'accountType': 'Type1',
    'accountHandle': 'Account1',
})

# Validate Account
sf.validateAccount({
    'accountHandle': 'Account1',
    'Annual Revenue': '$1,000,000',
    'Rating': 'Warm',
})

# Delete Account
sf.deleteAccount({
    'accountHandle': 'Account1',
})

# Log out of Salesforce
sf.logout()

print('Script Complete')
