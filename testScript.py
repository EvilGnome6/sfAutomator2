from lib import sfAutomator as sf
from lib import parameters as pars
import os

# Set up the Log File
pars.logFile = os.path.basename(__file__)
sf.setupLogFile()

# Log in to Salesforce
sf.login()

# Create new Account
account1 = sf.createAccount('Type1')

# Create new Account
account2 = sf.createAccount('Type2')

# Validate Account
values = {
    'Account Name': 'Test Account 1',
    'Annual Revenue': '$1,000,000',
    'Rating': 'Warm',
}
sf.validateAccount(account1, values)

# Validate Account
values = {
    'Account Name': 'Test Account 2',
    'Type': 'Pending',
    'Annual Revenue': '$2,000,000',
}
sf.validateAccount(account2, values)

# Delete Account
sf.deleteAccount(account1)

# Delete Account
sf.deleteAccount(account2)

# Log out of Salesforce
sf.logout()

print('Script Complete')
