# operations
def login(account:int, password:str)->bool:
    pass

def register(username:str,email:str,password:str,deposite_ambunt:int):
    pass

def get_balance(account:int)->int:
    pass

def withdraw(account:int, withdraw_amount:int)->str:
    pass

def deposite(account:int, deposite_amount:int)->str:
    pass

def transfer(from_account:int, to_account:int, transfer_amount):
    pass

def ministatement(account:int)->list[dict]:
    pass

def logout():
    pass


# main
if __name__ == "__main__":
    print("Welcome to the small scale bank")
    print("Select your operation \n 1.Register \n 2.Login")
    choice = int(input("Enter your opeartion number: "))
    if choice == 1:
        username = input("Enter username: ")
        email = input("Enter E-mail id: ")
        initial_deposite = int(input("Enter your initial deposite amount: "))
        password = input("Enter password: ")

        # call register function

    elif choice == 2:
        account_no = int(input("Enter your account number: "))
        password = input("Enter your password: ")
        # call login function

        # if login -True
            #show the operation list
        # else
            #print("Invalid credentials")