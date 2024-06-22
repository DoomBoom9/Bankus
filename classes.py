import pickle
import os

class Bank:
    def __init__(self,name):
        self.name = name
        self.customers = []         #list of customers allows the bank to "own" customers and 
        self.bank_capital = 1000000
    
    def add_customer(self, first_name, surname, address):
        fullname = first_name + surname
        self.customers.append(fullname)
        self.customers[-1] = Customer(first_name, surname, address)
        self.__repr__()  #Appends customers to the list of customers "owned" by the bank
    
    def interest(self):                     #I MESSED THIS UP IMMA HAVE TO FULLY REDO
        new_capital = 0
        for customer in self.customers:     #iterates through the customer's accounts
            for account in customer.accounts:               #calculates interest for each account of each customer
                new_capital += (account.balance*(1+account.interest/12)**12)
        new_capital += self.bank_capital
        print(f'Original capital: ${self.capital()}')           #prints the capital of the bank
        print(f'Capital next annum: ${new_capital}')            #capital post interest in 12 months
        print(f'Interest accrewed: ${self.capital() - new_capital}')            #amount of interest over the next 12 months

    def __repr__(self):
        return f'Bank(name={self.name}, customers={self.customers})'

    def capital(self):                                             #returns the bank's capital
        if __name__ == "__main__":
            return bankus.bank_capital
        print(f'Capital: ${bankus.bank_capital}') 
        
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
        if __name__ != "__main__":
            if self.max_transactions <= 0:                                         
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
            bankus.bank_capital += amount
            if __name__ != "__main__":
                print(f'You have withdrawn ${amount}')
                print(f"Your new balance is ${self.balance}")
        else:
            self.error_messages()
    
    def deposit(self, amount):                                  #deposit money into the account
        if self.max_transactions > 0 and bankus.bank_capital > -1000000:
            self.balance += amount
            if self.account_type == "Basic" or "LoyaltySaver":
                self.max_transactions -= 1
            bankus.bank_capital -= amount
            if __name__ != "__main__":
                print(f"Your new balance is ${self.balance}")
        else:
            self.error_messages()
    
    def Interest(self):                                   #Calculates interest for this account over the past 
        interest = self.balance*(1 + self.interest / 12)**12        #Interest formula
        print(f'Balance after interest this annum: ${interest}') 
        print(f'Interest accrewed: ${interest - self.balance}')
        
    
    def Balance(self):                  #Returns Balance
       print(f'${self.balance}')

    def __repr__(self):
        return f'Account(account_type={self.account_type}, balance={self.balance}), interest={self.interest}, max_transactions={self.max_transactions}, can_withdraw={self.can_withdraw}' #returns transactions left instead of max transactions
    
class MortgageAccount(BasicAccount):        #Mortgage Bank Account
    def __init__(self, balance):
        self.account_type = 'Mortgage'
        self.interest = 0.045
        self.balance = balance
        self.can_withdraw = False
        self.max_transactions = 1

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

    def add_account(self, account_type, balance):  #Appends account to accounts list
        count = 0
        accounts = self.accounts
        for account in self.accounts:
            count += 1
        account_placeholder = self.first_name + self.surname
        accounts.append(account_placeholder)
        if account_type == 1:                                           #sets the type of account        
            accounts[count] = BasicAccount(balance)
        if account_type == 2:
            accounts[count] = LoyaltySaverAccount(balance)
        if account_type == 3: 
            accounts[count] = MortgageAccount(balance)
        
    def change_name(self, new_first_name, new_surname):
        if __name__ != "__main__":
            print(f"Name has been changed from {self.first_name} {self.surname}")      #print original name
            print(f"Name has been changed to {new_first_name} {new_surname}")          #print new name
        self.first_name = new_first_name                                           #update first name
        self.surname = new_surname                                                 #update last name
    
    def change_address(self, new_address): #new address
        if __name__ != "__main__":
            print(f'Address has been changed from {self.address}')                     #print old address      
            print(f"Address has been changed to {new_address}")                            #print new address
        self.address = new_address                                                     #update address
    
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

class UI:
    def add_customer_menu():
        os.system('clear') 
        print('Add Account Settings\n\n')
        first_name = input('First Name: ')
        surname = input('Surname: ')
        address = input('Address: ')
        bankus.add_customer(first_name, surname, address)
        del first_name                  #these del statements were put in here to prevent potential unintended
        del surname                     #interactions from occuring and then it taking forever to find the cause.

    def bank_interest_menu():
        os.system('clear')
        print('Bankus Interest\n\n')
        bankus.interest()
        print()
        selection = input("Go Back: ")

    def bank_capital_menu():
        os.system('clear')
        print("Bankus Capital\n\n")
        print(f'Capital: ${bankus.capital()}\n')
        selection = input("Go Back: ")

    def add_account_menu():
        os.system('clear')
        print('Add Acount\n\n')
        bankus.list_customers()     #lists customers
        print()
        while True:                 #User selects customer to create account for
            try:
                selection = int(input("Which customer do you want to create the account for? "))
                if selection == len(bankus.customer_list):
                    break
            except ValueError:
                print('Please enter a valid customer choice')
            except IndexError:
                print('Please enter a valid customer choice')
        print("1. Basic Account")
        print("2. Loyalty Saver")
        print("3. Mortgage")
        account_type = int(input("Choose account type: "))
        balance = float(input('Input balance: '))
        bankus.customers[selection - 1].add_account(account_type, balance)
    
    def customer_change_name_menu():
        os.system("clear")
        print("Change Customer Name\n\n")
        bankus.list_customers()
        print()
        selection = int(input("Which customer would you like to change? "))
        new_first_name = input("Input new first name: ")
        new_surname = input("Input new surname: ")
        bankus.customers[selection - 1].change_name(new_first_name, new_surname)

    def customer_change_address_menu():
        os.system("clear")
        print("Change Customer Address")
        bankus.list_customers()
        print()
        selection = int(input("Which customer would you like to change? "))
        new_address = input("Input new address: ")
        bankus.customers[selection - 1].change_address(new_address)
    
    def customer_check_interest_menu():
        os.system("clear")
        print("Check Customer Interest\n\n")
        bankus.list_customers()                
        print()
        selection = int(input('Select a Customer: '))
        bankus.customers[selection - 1].total_interest()
        selection = input("Go Back: ")
    
    def list_of_customers_menu():
        os.system('clear')
        print('List of Customers\n\n')
        bankus.list_customers()
        print()
        selection = input('Go Back: ')
    
    def check_balance_menu():
        pass
    
    def withdraw_menu():
        os.system('clear')
        print('Withdraw\n\n')       #When there's no accounts it dies :(
        bankus.list_customers()                
        print()
        selection = int(input('Select a customer: '))
        i = 1
        customer = bankus.customers[selection-1]
        for account in customer.accounts:
            print(f'{i}. {account}')
            i += 1
        selection = int(input('Select an account: '))
        amount = float(input("Select amount to withdraw: "))
        customer.accounts[selection - 1].withdraw(amount)
        selection = input("Go Back: ")

    def deposit_menu():
        os.system('clear')
        print("Deposit")
        bankus.list_customers()                
        print()
        selection = int(input('Select a customer: '))
        customer = bankus.customers[selection - 1]
        i = 0
        for account in customer.accounts:
            print(f'{i}. {account}')
            i += 1
        selection = int(input('Select an account: '))
        amount  = float(input("Select amount to deposit: "))
        customer.accounts[selection - 1].deposit(amount)
        selection = input("Go Back: ")

    def account_interest_menu():
        os.systen('clear')
        print('Interest')
        bankus.list_customers()
        print()
        selection = int(input('Select a customer: '))
        customer = bankus.customers[selection - 1]
        i = 0
        for account in customer.accounts:
            print(f'{i}. {account}')
            i += 1
        selection = int(input('Select an account: '))  
        customer.accounts[selection - 1].interest()
        selection = input("Go Back: ")
        




                
        



    

class TestProgram:
    def test_add_customer():
        bankus.add_customer("John", "Doe", "123 High Street")
        bankus.customers[-1]
        try:
            assert bankus.customers[-1].first_name == "John", "first name: Test Failed"
        except AssertionError:
            print("First Name: Test Failed")
        try:
            assert bankus.customers[-1].surname == "Doe", "surname: Test Failed"
        except AssertionError:
            print("Surname: Test Failed")
        try:
            assert bankus.customers[-1].address == "123 High Street"
        except AssertionError:
            print("Address: Test Failed")
        del bankus.customers[-1]
  
    def test_bank_interest():
        bankus.bank_capital = 1000000
        try:
            assert bankus.interest() == 1000000
        except AssertionError:
            print("Bank Interest Failed")
        bankus.bank_capital = 0
        try:
            assert bankus.interest() == 0
        except AssertionError:
            print("Bank Interest Failed")
        
        bankus.bank_capital = 1000000
        bankus.add_customer("Big", "Dog", "BARK BARK WOOF WOOF")
        bankus.customers[-1].add_account(1, 1000)
        try:
            assert bankus.interest() == 9999050             #Fails bc withdrawal is messed up.
        except AssertionError:
            print("Bank interest: Test Failed")

    
    def test_bank_capital():
        try:
            assert bankus.capital() == bankus.bank_capital 
        except AssertionError:
            print("Bank Capital: Test Failed")

    def test_list_customers():
        pass

    def test_save_state():
        pass

    def test_load_state():
        pass

    def test_add_account():
        bankus.add_customer("Jane", "Doe", "123 High Street")
        customers = bankus.customers
        customers[-1].add_account(1, 3000)
        account = getattr(customers[-1], "accounts")
        try: 
            assert account[-1].account_type == "Basic"
        except AssertionError:
            print("Account Type: Test Failed")
        try:
            assert account[-1].balance == 3000
        except AssertionError:
            print("Balance: Test Failed")
        del bankus.customers[-1]
        

    def test_change_name(firstName, last_name):
        bankus.add_customer(firstName, last_name, "123 High Street")
        bankus.customers[-1].change_name("Humpty", "Dumpty")
        try:
            assert bankus.customers[-1].first_name == "Humpty"
        except AssertionError:
            print('First Name Change: Test Failed')
        try: 
            assert bankus.customers[-1].surname == "Dumpty"
        except AssertionError:
            print('Surname Change: Test Failed')
        del bankus.customers[-1]

    def test_change_address(address2):
        bankus.add_customer("John", "Doe", "123 High Street")
        bankus.customers[-1].change_address(address2)
        try: 
            assert bankus.customers[-1].address == address2
        except AssertionError:
            print('Change Address: Test Failed')
        del bankus.customers[-1]

    def test_total_interest():
        pass

    def test_withdraw():
        bankus.add_customer("Brooklyn", "Smith", "5 Dalby Street")
        bankus.customers[-1].add_account(1, 1000)
        bankus.customers[-1].accounts[-1].withdraw(100)
        try:
            assert bankus.customers[-1].accounts[-1].balance == 900
        except AssertionError:
            print('Basic Withdraw: Test Failed')
        bankus.customers[-1].add_account(2, 1000)
        bankus.customers[-1].accounts[-1].withdraw(100)
        try:
            assert bankus.customers[-1].accounts[-1].balance == 900
        except AssertionError:
            print('LoyaltySaver withdraw: Test Failed')
        bankus.customers[-1].add_account(3, 1000)
        bankus.customers[-1].accounts[-1].withdraw(100)
        try: 
            assert bankus.customers[-1].accounts[-1].balance == 1000
        except AssertionError:
            ('Mortgage withdraw: Test Failed')
        del bankus.customers[-1].accounts
        del bankus.customers[-1]

    def test_deposit():
        bankus.add_customer("Paul", "Dempsey", "")
        bankus.customers[-1].add_account(1, 1000)
        bankus.customers[-1].accounts[-1].deposit(100)
        try:
            assert bankus.customers[-1].accounts[-1].balance == 1100
        except AssertionError:
            print('Basic deposit: Test Failed')
        bankus.customers[-1].add_account(2, 1000)
        bankus.customers[-1].accounts[-1].deposit(100)
        try:
            assert bankus.customers[-1].accounts[-1].balance == 1100
        except AssertionError:
            print('LoyaltySaver deposit: Test Failed')
        bankus.customers[-1].add_account(3, 1000)
        bankus.customers[-1].accounts[-1].deposit(100)
        try:
            assert bankus.customers[-1].accounts[-1].balance == 1100
        except AssertionError:
            print('LoyaltySaver deposit: Test Failed')

    def test_balance():
        pass
        
if __name__ == "__main__":
    bankus = Bank('bankus')
    bankus.save_state("foo.pkl")
    TestProgram.test_add_customer()
    TestProgram.test_bank_interest()
    TestProgram.test_bank_capital()
    TestProgram.test_list_customers()
    TestProgram.test_save_state()
    TestProgram.test_load_state()
    TestProgram.test_add_account() #fix the problem of bankus' balance not going doen
    print(bankus.bank_capital)

    TestProgram.test_change_name("Marty", "Patricks")
    TestProgram.test_change_name(1, 2)
    TestProgram.test_change_name(1.0, 73.1)

    TestProgram.test_change_address("123 Geraldine Crescent")
    TestProgram.test_withdraw()
    print(bankus.bank_capital)   #reset bankus' balance
    TestProgram.test_deposit()
    print(bankus.bank_capital)   #reset bankus' balance
    TestProgram.test_balance()
