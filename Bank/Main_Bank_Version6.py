# Main program for controlling a Bank made up of Accounts

# Bring in all the code of the Bank class
from Bank import *

#
oBank = Bank('9 to 5', '131 Fear Street, Jacksonville, USA', '(650) 555-1212')

# Main code

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To get bank information, press i')
    print('To open a new account, press o')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w')
    print('To quit, press q')
    print()
    
    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()
    
    try:
        if action == 'b':
            oBank.balance()
            
        elif action == 'c':
            oBank.closeAccount()
            
        elif action == 'd':
            oBank.deposit()
            
        elif action == 'i':
            oBank.getInfo()
            
        elif action == 'o':
            oBank.openAccount()
            
        elif action == 's':
            oBank.show()
            
        elif action == 'q':
            break
        
        elif action == 'w':
            oBank.withdraw()
    except AbortTransaction as error:
        # Print out the text of the error message
        print(error)
        
print('Done')