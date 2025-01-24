balance = 0

is_running = True
def show_balance():
    global balance
    print(f"YOUR BALANCE IS: ${balance:.2f}")

def deposit():
    amount = float(input("Enter amount to deposit: "))
    global balance 
    balance += amount
    print(f"Ok, ${amount:.2f} was added to your balance")
    return balance
def withdraw():
    amount = float(input("Enter amount to withdraw: "))
    global balance
    if amount > balance:
        print("Insufficient funds")
    else:
        balance -= amount
    return balance

def quit_program():
    global is_running
    print("Thank you for banking with us!")
    is_running = False
    

def main():
    global is_running
    print("This is the bank program, Welcome!")
    print("What would you like to do?")
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    while is_running:
        
        try:
            choice = (int(input("Choose an option: ")))
        except ValueError:            
            exit("Invalid Input")
                    
        if choice == 1:
            show_balance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            quit_program()
        else:
            print("Invalid choice")


main()