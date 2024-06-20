import pickle
import time
import os

class Bank:
    def __init__(self,name):
        self.name = name
        self.customers = []         #list of customers allows the bank to "own" customers and 
        self.bank_capital = 1000000
    
    def add_customer(self, customer):
        self.customers.append(customer)     #Appends customers to the list of customers "owned" by the bank
    
    def interest(self):                     #I MESSED THIS UP IMMA HAVE TO FULLY REDO
        new_capital = 0
        for customer in self.customers:     #iterates through the customer's accounts
            customer_accounts = getattr(customer, "accounts")
            for account in customer_accounts:               #calculates interest for each account of each customer
                interest = getattr(account, "interest")
                balance = getattr(account, "balance")
                new_capital += (balance*(1+interest/12)**12)
        print(f'Original capital: ${self.capital()}')           #prints the capital of the bank
        print(f'Capital next annum: ${new_capital}')            #capital post interest in 12 months
        print(f'Interest accrewed: ${new_capital - self.capital()}')            #amount of interest over the next 12 months

    def __repr__(self):
        return f'Bank(name={self.name}, customers={self.customers})'

    def capital(self):                                              #returns the bank's capital
        return self.bank_capital   
        
    def list_customers(self):                                       #iterates through the customer list and prints their first
        i = 0                                                       #and surname along with its place in the list
        for customer in self.customers:
            print(f"{i+1}. {getattr(customer, "first_name")} {getattr(customer,"surname")}")
            i += 1
    
    def save_state(self, filename):                                 #Saves the program state in a .pkl file
       with open(filename, 'wb') as file:
          pickle.dump(self, file)
    
    @staticmethod
    def load_state(filename):                                        #loads the program state from the .pkl 
       with open(filename, 'rb') as file:
           return pickle.load(file)
    

class BasicAccount:                                #The base Account class that methods are inherited from
    def __init__(self, balance):
        self.interest = 0.02
        self.balance = balance
        self.max_transactions = 2
        self.can_withdraw = True
        self.account_type = 'Basic'
    
    def error_messages(self):
        if self.max_transactions <= 0:                                          #error messages concerning account transactions
            print("Sorry! You've reached the action limit on this account.")
            print("Please restart the session to reset this limit")
        if self.can_withdraw == False:
            print("Sorry! You cannot withdraw from this account")
        if self.balance <= 0:
            print(f"Your balance is {self.balance}")
            print('balance is in the negative')
            print('')
        if bankus.bank_capital < -1000000:
            print("Bank Capital cannot be below -$1,000,000")
            print("Please withdraw from an account to increase the bank capital")

    def withdraw(self, amount):                                                #Withdraw from account
        if self.can_withdraw == True and self.max_transactions > 0:
            self.balance = self.balance - amount
            self.max_transactions -= 1
            print(f'You have withdrawn ${amount}')
            print(f"Your new balance is ${self.balance}")
            bankus.bank_capital += amount
        else:
            self.error_messages()
    
    def deposit(self, amount):                                  #deposit money into the account
        if self.max_transactions > 0 and bankus.bank_capital > -1000000:
            self.balance += amount                              
            self.max_transactions -= 1
            print(f"Your new balance is ${self.balance}")
            bankus.bank_capital -= amount
        else:
            self.error_messages()
    
    def calculate_interest(self):                                   #Calculates interest for this account over the past 
        interest = self.balance*(1 + self.interest / 12)**12        #Interest formula
        print(f'Balance after interest this annum: ${interest}') 
        print(f'Interest accrewed: ${interest - self.balance}')
        return interest
    
    def Balance(self):                  #Returns Balance
        return self.balance()

    def __repr__(self):
        return f'Account(account_type={self.account_type}, balance={self.balance}), interest={self.interest}, max_transactions={self.max_transactions}, can_withdraw={self.can_withdraw}' #returns transactions left instead of max transactions
    

class MortgageAccount(BasicAccount):        #Mortgage Bank Account
    def __init__(self, balance):
        self.account_type = 'Mortgage'
        #self.mortgage = mortgage
        self.interest = 0.045
        self.balance = balance
        self.can_withdraw = False
        self.max_transactions = "unlimited"

class LoyaltySaverAccount(BasicAccount):       #Loyalty Saver
    def __init__(self, balance):
        self.account_type = 'LoyaltySaver'
        self.interest = 0.03
        self.balance = balance
        self.max_transactions = 5
        self.can_withdraw = True
    
class Customer:
    def __init__(self, first_name, surname, address):
        self.first_name = first_name
        self.compound_interest = 0
        self.surname = surname
        self.address = address
        self.accounts = []                                  #Array that allows customers to "own" accounts
        self.customer_capital = 0 

    def __repr__(self):
        return f'Customer(first_name={self.first_name}, surname={self.surname}, address={self.address}, accounts={self.accounts})'

    def add_account(self, account):                         #Appends account to accounts list
        self.accounts.append(account)
    
    def change_name(self):
        new_first_name = input('Input new first name: ')                        #new first name and last name to be updated
        new_surname = input('Input new surname: ')
        print(f"Name has been changed from {self.first_name} {self.surname}")      #print original name
        print(f"Name has been changed to {new_first_name} {new_surname}")          #print new name
        self.first_name = new_first_name                                           #update first name
        self.surname = new_surname                                                 #update last name
    
    def change_address(self):
        address = input("Input new address: ")                                     #new address
        print(f'Address has been changed from {self.address}')                     #print old address      
        print(f"Address has been changed to {address}")                            #print new address
        self.address = address                                                     #update address
    
    def total_balance(self):
        self.customer_capital = 0
        for account in self.accounts:                                             #iterates through a customers accounts
            self.customer_capital += getattr(account, "balance")                  #adds the account balance to the customers total balance
        return self.customer_capital
    
    def total_interest(self):
        for account in self.accounts:                                             #Iterates through accounts
            self.compound_interest += account.calculate_interest()                #Calculates the interest for each account and adds it to customer's total interest
        print(self.compound_interest)
    
    def list_accounts(self):
        i = 0
        for account in self.accounts:              #iterates through accounts list and prints
            print(f"{i+1}. {account}")
            i += 1

try: 
    bankus = Bank.load_state("Bankus.pkl")         #loads the bankus save file
except:
    print('No bank file present')                  #If no file present, creates a new bank instance
    print('Creating empty bank.')
    time.sleep(5)
    os.system('clear')
    bankus = Bank("Bankus")

customer_list = []               #array that allows customers to be dynamically created before appending to the bank class
account_list = []                #array that allows customers to be dynamically created before appending to the customer class
i = 0                            #this prolly does nothing
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
                customer_list[-1] = Customer(first_name, surname, address)
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