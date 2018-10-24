from lib import sfAutomator as sf
from lib import parameters as pars
import os

# Set up the Log File
pars.logFile = os.path.basename(__file__)
sf.setupLogFile()

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
