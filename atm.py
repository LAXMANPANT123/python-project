def show_balance(balance):
    print(f"your balance is ${balance:2f}")

def deposit():
    amount = float(input("enter an amount to be deposited"))

    if amount < 0:
        print("thats not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("enter amount to be withdrawn: "))

    if amount > balance:
        print("insufficient funds")
        return 0
    elif amount < 0:
        print("amount must be greater than 0")
        return 0
    else:
        return amount
    

def main():
    balance = 0
    is_running = True

    while is_running:

        print("****************")
        print("banking program")
        print("****************")
        print("1.showbalance")
        print("****************")
        print("2.deposit")
        print("****************")
        print("3.withdraw")
        print("****************")
        print("4.exit")


        choice = input("enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance +=deposit()
        elif choice == '3':
            balance -=withdraw()
        elif choice == '4':
            is_running = False
        else:
            print("that is not valid choice")

    print("thank you have a nice day")


main()
