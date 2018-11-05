from lib import sfAutomator as sf

# Initialize the Test
sf.init({
    'testName': 'demoScript',
})

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
