import pickle
import time
import os
import classes

try: 
    bankus = classes.Bank.load_state("Bankus.pkl")         #loads the bankus save file
except:
    print('No bank file present')                  #If no file present, creates a new bank instance
    print('Creating empty bank.')
    time.sleep(5)
    os.system('clear')
    bankus = classes.Bank("Bankus")


i = 0                         
os.system('clear')

while True:                     #keeps the loop going until the user wants to exit
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
                os.system('clear') 
                print('Add Account Settings\n\n')
                first_name = input('First Name: ')
                surname = input('Surname: ')
                address = input('Address: ')
                fullname = first_name + surname
                customer_list.append(fullname)
                customer_list[-1] = classes.Customer(first_name, surname, address)
                bankus.add_customer(customer_list[-1])
                bankus.__repr__()
                del first_name                  #these del statements were put in here to prevent potential unintended
                del surname                     #interactions from occuring and then it taking forever to find the cause.
                del fullname

            if selection == 2:                  #Bank interest
                os.system('clear')
                print('Bankus Interest\n\n')
                bankus.interest()
                print()
                selection = input("Go Back: ")
            
            if selection == 3:                  #Bank Capital
                os.system('clear')
                print("Bankus Capital\n\n")
                print(f'Capital: ${bankus.capital()}')
                print()
                selection = input("Go Back: ")
            
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
                os.system('clear')
                print('Add Acount\n\n')
                bankus.list_customers()     #lists customers
                print()
                while True:                 #User selects customer to create account for
                    try:
                        selection = int(input("Which customer do you want to create the account for? "))
                        if selection == len(customer_list):
                            break
                    except ValueError:
                        print('Please enter a valid customer choice')
                    except IndexError:
                        print('Please enter a valid customer choice')
                        
                accounts = getattr(customer_list[selection-1], "accounts")      #gets account list owned by selected customer
                count = 0
                for account in accounts: #number of accounts in account list which is then appended to the account name so variable names aren;t the same
                    count +=1
                account_name = getattr(customer_list[selection -1], 'first_name') + getattr(customer_list[selection - 1], 'surname') + f"{count}" #sets a name for the account var
                account_list.append(account_name)   #adds it to the account list so it can be used as a variable equal to the created instance of account

                print("1. Basic Account")
                print("2. Loyalty Saver")
                print("3. Mortgage")
                account_type = int(input("Choose account type: "))
                balance = float(input('Input balance: '))
                if account_type == 1:                                           #sets the type of account        
                    account_list[count] = BasicAccount(balance)
                if account_type == 2:
                    account_list[count] = LoyaltySaverAccount(balance)
                if account_type == 3: 
                    account_list[count] = MortgageAccount(balance)
                customer_list[selection - 1].add_account(account_list[count])   #appends it to the customer's accounts
            
            if selection == 2:
                os.system("clear")
                print("Change Customer Name\n\n")
                bankus.list_customers()
                print()
                selection = int(input("Which customer would you like to change? "))
                customers = getattr(bankus, "customers")
                customers[selection - 1].change_name()

            if selection == 3: 
                os.system("clear")
                print("Change Customer Address")
                bankus.list_customers()
                print()
                selection = int(input("Which customer would you like to change? "))
                customers = getattr(bankus, "customers")
                customers[selection - 1].change_address()
            
            if selection == 4:   #should probably be a part of bank
                os.system("clear")
                print('Check Customer Balance\n\n')
                bankus.list_customers()
                print()
                selection = int(input('Select a Customer: '))
                customer = getattr(bankus, "customers")
                customer[selection - 1].list_accounts() #Fix the repr up because it hurts my eyes
                customer[selection - 1].total_balance()
                print(f"Total Balance: ${getattr(customer[selection-1], "customer_capital")}")
                selection = input("Go Back:")

            if selection == 5:                              #this whole block looks like an eyesore in the terminal
                os.system("clear")
                print("Check Customer Interest\n\n")
                bankus.list_customers()                
                print()
                selection = int(input('Select a Customer: '))
                customer = getattr(bankus, "customers")
                customer[selection - 1].total_interest() 
                account = getattr(customer[selection - 1], "accounts")
                count = 0
                for element in account:
                    print(f"{count}. {getattr(element, "account_type")}, %{getattr(element, "interest")*100}") #this 
                    element.calculate_interest()
                    count+=1
                selection = input("Go Back: ")

            if selection == 6:
                os.system('clear')
                print('List of Customers\n\n')
                bankus.list_customers()
                print()
                selection = input('Go Back: ')

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
                os.system('clear')
                print('Check Balance\n\n')
                
            if selection == 2:              #This probably wont work as intended
                os.system('clear')
                print('Withdraw\n\n')       #When there's no accounts it dies :(
                bankus.list_customers()                
                print()
                selection = int(input('Select a customer: '))
                customer = getattr(bankus, "customers")
                accounts = getattr(customer[selection - 1], "accounts")
                i = 1
                for element in accounts: 
                    print(f'{i}. {element}')
                    i += 1
                selection = int(input('Select an account: '))
                amount  = float(input("Select amount to withdraw: "))        #ValueError: could not convert string to float: 'Select ammount to withdraw:
                accounts[selection - 1].withdraw(amount)              
                selection = input("Go Back: ")
            
            if selection == 3:              #this will probably shit itself as well
                os.system('clear')
                print("Deposit")
                bankus.list_customers()                
                print()
                selection = int(input('Select a customer: '))
                customer = getattr(bankus, "customers")
                accounts = getattr(customer[selection - 1], "accounts")
                i = 0
                for element in accounts: 
                    print(f'{i}. {element}')
                    i += 1
                selection = int(input('Select an account: '))
                amount  = float(input("Select amount to deposit: "))
                accounts[selection - 1].deposit(amount)              
                selection = input("Go Back: ")
            
            if selection == 4:                                              
                os.system('clear')
                print('Interest')
                bankus.list_customers()                
                print()
                selection = int(input('Select a customer: '))
                customer = getattr(bankus, "customers")
                accounts = getattr(customer[selection - 1], "accounts")
                i = 0
                for element in accounts: 
                    print(f'{i}. {element}')
                    i += 1
                selection = int(input('Select an account: '))
                accounts[selection - 1].interest()              
                selection = input("Go Back: ")
            
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