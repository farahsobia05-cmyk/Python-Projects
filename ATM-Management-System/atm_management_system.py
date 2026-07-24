balance = 5000
input_value = 0
while input_value != 4:
    print("========== ATM ==========")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    input_value = int(input("Enter value of your choice"))
    if input_value == 1:
        print(f"Your current balance is {balance}") 
    elif input_value == 2:
        deposit = int(input("How much amount you want to deposit"))
        balance += deposit
        print(f"Your balance after deposit is {balance}")
    elif  input_value == 3:
        withdraw = int(input("Enter amount to withdraw"))
        if withdraw <= balance:
            balance -= withdraw
            print(f"Your balance after withdraw is = {balance} ")
        else:
            print("Insufficient balance")
    elif input_value == 4:
        break
    else:
        print("Invalid option selected")
print("Thank you for using ATM")
