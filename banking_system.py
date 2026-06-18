# =====================   N1 BANKING SYSTEM   ==================


accounts = {}


def create_account(acc_num,name ,initial_balance= 0):
    if acc_num in accounts:
        print("Account already exists")
    else:
        accounts[acc_num] = {"name":name,"balance": initial_balance}
        print(f"account created successfully for {name} with number {acc_num}")


def deposit(acc_num,amount):
    if acc_num in accounts:
        if amount > 0:
            accounts[acc_num]['balance'] += amount
            print(f"deposit {amount}. new balance = {accounts[acc_num]['balance']}")
        else:
            print("invalid deposit amount")
    else:
        print("account not found")


def withdraw(acc_num,amount):
    if acc_num in accounts:
        if 0 < amount <= accounts[acc_num]['balance']:
            accounts[acc_num]['balance'] -= amount
            print(f"withdraw {amount}. new balance = {accounts[acc_num]['balance']}")
        else:
            print("insufficient balance !! ")
    else:
        print("account not found")

def check_balance(acc_num):
    if acc_num in accounts:
        print(f"account balance for {acc_num} is {accounts[acc_num]['balance']}")
    else:
        print("account not found")

def transfer(from_acc,to_acc,amount):
    if from_acc in accounts and to_acc in accounts:
        if 0 < amount <= accounts[from_acc]['balance']:
            accounts[to_acc]['balance'] += amount
            accounts[from_acc]['balance'] -= amount
            print(f"transferred {amount} from {from_acc} to {to_acc} to balance = {accounts[from_acc]['balance']}")
        else:
            print("transfer fail ! check your balance")
    else:
        print("one or both account not find...")


def show_all_accounts():
    if accounts:
        print("\n===== All Accounts =====")
        print(f"{'Acc Number':<15}{'Name':<20}{'Balance':<10}")
        print("-" * 45)
        for acc_num, info in accounts.items():
            print(f"{acc_num:<15}{info['name']:<20}{info['balance']:<10}")
    else:
        print("No accounts found.")


while True:
    print("\n====N1 BANKING SYSTEM====\n")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Transfer")
    print("6. Show all accounts")
    print("7. Exit")
    choice = int(input("enter your choice: "))
    if choice == 1:
        acc_num = input("Enter account number : ")
        name = input("enter account holder name : ")
        initial = float(input("enter initial deposit : "))
        create_account(acc_num,name,initial)
    elif choice == 2:
        acc_num = input("Enter account number : ")
        amount = float(input("ente amount to be deposited : "))
        deposit(acc_num,amount)
    elif choice == 3:
        acc_num = input("Enter account number : ")
        amount = float(input("Enter amount to be withdrawn : "))
        withdraw(acc_num,amount)
    elif choice == 4:
        acc_num = input("Enter account number : ")
        check_balance(acc_num)
    elif choice == 5:
        from_acc = input("Enter your account number : ")
        to_acc = input("enter recipient account number : ")
        amount = float(input("Enter amount to be transfer : "))
        transfer(from_acc,to_acc,amount)
    elif choice == 6:
        show_all_accounts()
    elif choice == 7:
        print("THANK YOU for using N1 BANKING SYSTEM ........")
        break
    else:
        print("invalid choice please try again")


