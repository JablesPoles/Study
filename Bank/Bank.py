# Bank that manages a dictionary of Account objects

from Account import *

class Bank():
    
    def __init__(self, hours, adress, phone):
        self.accountsDict = {}
        self.nextAccountNumber = 0
        self.hours = hours
        self.adress = adress
        self.phone = phone
        
    def askForValidAccountNumber(self):
        accountNumber = input('What is your account number? ')
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AbortTransaction('The account number must be an integer')
        if accountNumber not in self.accountsDict:
            raise AbortTransaction('There is no account ' + str(accountNumber))
        return accountNumber
    
    def getUsersAccount(self):
        accountNumber = self.askForValidAccountNumber()
        oAccount = self.accountsDict[accountNumber]
        self.askForValidPassword(oAccount)
        return oAccount
        
    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber
    
    def openAccount(self):
        print('*** Open Account ***')
        userName = input('What is the name for the new user account? ')
        userStartingAmount = input('What is the starting balance for this account?')
        userStartingAmount = int(userStartingAmount)
        userPassword = input("What is the password you want to use for this account? ")
        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print("Your new account number is:", userAccountNumber)
        print()
        
    def closeAccount(self):
        print('*** Close Account ***')
        userAccountNumber = input('What is your account number? ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('What is your password? ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)
        if theBalance is not None:
            print('You had', theBalance, 'in your account, which is being returned to you.')
            # Remove user's account from the dictionary of accounts
            del self.accountsDict[userAccountNumber]
            print('Your account is now closed.')
            
            
    def deposit(self):
        print('*** Deposit ***')
        oAccount = self.getUsersAccount()
        depositAmount = input('Please enter the amount to deposit: ')
        theBalance = oAccount.deposit(depositAmount)
        print('Deposited:', depositAmount)
        print('Your new balance is:', theBalance)
        
    def withdraw(self):
        print('*** Withdraw ***')
        oAccount = self.getUsersAccount()
        userAmount = input('Please enter the amount to withdraw: ')
        theBalance = oAccount.withdraw(userAmount)
        print('Withdrew:', userAmount)
        print('Your new balance is:', theBalance)
        
    def getInfo(self):
        print('Hours:', self.hours)
        print('Address:', self.adress)
        print('Phone:', self.phone)
        print('We currently have', len(self.accountsDict), 'account(s) open.')
        
        
    # Special method for Bank administrator only        
    def show(self):
        print('*** Show ***')
        print('(This would typically requiere an admin password)')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('     Account number:', userAccountNumber)
            oAccount.show()
            print()
            
    
