import os
from classes import *

os.system('clear')
bankus.reset_transactions()

while True:                     #keeps the loop going until the user wants to exit
    os.system('clear')
    print("Bankus\n\n")
    print("1. Bank")
    print("2. Customer")
    print("3. Account")
    print("4. Save")
    print("5. Exit")
    while True:
        try:
            selection = int(input("Select action type: "))
            if selection == 1 or 2 or 3 or 4 or 5:
                break
        except ValueError:
            print("Please input a valid selection (1-5)\n")
    
    if selection == 1:                          #Bank Options
        while True:  
            os.system("clear")
            print('Bank Options\n\n')
            print('1. Add Customer')
            print('2. Check Interest')
            print('3. Check Capital')
            print('4. Bank Status')
            print('5. Back')

            while True:
                try:
                    selection = int(input("Select action type: "))
                    if selection == 1 or 2 or 3 or 4 or 5:
                        break
                except ValueError:
                    print("Please input a valid selection (1-5)\n")
            
            if selection == 1:
                UI.add_customer_menu()

            if selection == 2:                  #Bank interest
                UI.bank_interest_menu()
            
            if selection == 3:                  #Bank Capital
                UI.bank_capital_menu()
            
            if selection == 4:
                print(bankus)
                selection = input('Go Back: ')

            if selection == 5:                  #Exit Bank Settings
                os.system('clear')
                selection = 0
                break
             
    if selection == 2:                              #Customer Options
        while True:
            os.system('clear')
            print('Customer Options\n\n')
            print('1. Add Account')
            print('2. Change Customer Name')
            print('3. Change Customer Address')
            print('4. Check Customer Balance')
            print('5. Check Customer Interest')
            print('6. List Customers')
            print('7. Back')

            while True:
                try:
                    selection = int(input("Select action type: "))
                    if selection == 1 or 2 or 3 or 4 or 5 or 6 or 7:
                        break
                except ValueError:
                    print("Please input a valid selection (1-5)\n")

            if selection == 1:              #Add Account
                UI.add_account_menu()

            if selection == 2:
                UI.customer_change_name_menu()

            if selection == 3: 
                UI.customer_change_address_menu()
            
            if selection == 4:   #should probably be a part of bank
                UI.check_balance_menu()

            if selection == 5:                              #this whole block looks like an eyesore in the terminal
                UI.customer_check_interest_menu()

            if selection == 6:
                UI.list_of_customers_menu()

            if selection == 7:
                os.system('clear')
                break
        
    if selection == 3:                                          #Account options
        while True:
            os.system('clear')
            print('Account Options\n\n')
            print('1. Check Balance')
            print('2. Withdraw')
            print('3. Deposit')
            print('4. Calculate Interest')
            print('5. Back')

            while True:
                try:
                    selection = int(input("Select action type: "))
                    if selection == 1 or 2 or 3 or 4 or 5 or 6 or 7:
                        break
                except ValueError:
                    print("Please input a valid selection (1-5)\n")
            
            if selection == 1:
                UI.check_balance_menu()
                
            if selection == 2:              #This probably wont work as intended
                UI.withdraw_menu()
            
            if selection == 3:              #this will probably shit itself as well
                UI.deposit_menu()
            
            if selection == 4:                                              
                UI.account_interest_menu()
            
            if selection == 5:
                os.system('clear')
                selection = 0
                break

    if selection == 4:                          #Save bank
        bankus.save_state("Bankus.pkl")
    if selection == 5:                          #exits loop
        print('Exiting program...')
        break
print('Goodbye!')