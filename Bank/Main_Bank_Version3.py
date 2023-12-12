# Test program using accounts
# Version 2, using a list of accounts

# Bring in all the code from the Account class file
from Account import *

# Start off with an empty list of accounts
accountsDict = {}
nextAccountNumber = 0

# Create two accounts
oAccount = Account('Joe', 100, 'JoesPassword')
joesAccountNumber = nextAccountNumber
accountsDict[joesAccountNumber] = (oAccount)
print('Account name for Joe is:', joesAccountNumber)
nextAccountNumber = nextAccountNumber + 1

oAccount = Account('Mary', 12345, 'MarysPassword')
marysAccountNumber = nextAccountNumber
accountsDict[marysAccountNumber] = (oAccount)
print('Account name for Mary is:', marysAccountNumber)
nextAccountNumber = nextAccountNumber + 1

accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()
print()

# Call some methods on the different accounts
print('Calling methods of the new accounts...')
accountsDict[joesAccountNumber].deposit(50, 'JoesPassword')
accountsDict[marysAccountNumber].withdraw(345, 'MarysPassword')
accountsDict[marysAccountNumber].deposit(100, 'MarysPassword')

# Show the accounts
accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()

# Create another account with information from the user
print()
userName = input("What is the name for the new user account? ")
userBalance = input("What is the starting balance for this account? ")
userBalance = int(userBalance)
userPassword = input("What is the password you want to use for this account? ")
oAccount = Account(userName, userBalance, userPassword)
newAccountNumber = nextAccountNumber
accountsDict[newAccountNumber] = oAccount
print('Account number for new account is:', newAccountNumber)
nextAccountNumber = nextAccountNumber + 1

# Show the newly created user account
accountsDict[newAccountNumber].show()

# Let's deposit 100 into the new account
accountsDict[newAccountNumber].deposit(100, userPassword)
usersBalance = accountsDict[newAccountNumber].getBalance(userPassword)
print()
print('After depositing 100, the user balance is:', usersBalance)

# Show the new account
accountsDict[newAccountNumber].show()