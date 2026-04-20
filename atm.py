# Starting money
balance = float(input("Set your balance:"))  
pin = str(input("set your 4 digit secret pin:"))  # Secret PIN
# Check the length
if len(pin) != 4:
    print("Error: PIN must be exactly 4 digits!")

# Check if it's actually numbers (and not letters like 'abcd')
elif not pin.isdigit():
    print("Error: PIN must contain only numbers!")
else:
    print("PIN successfully set!")
print("--- Welcome to Python Bank ---")

# 2. Simple Security Check
while True:
    entered_pin = str(input("Please enter your 4-digit PIN: "))
    if len(entered_pin) != 4:
        print("Error: PIN must be exactly 4 digits!")
# Check if it's actually numbers (and not letters like 'abcd')
    elif not entered_pin.isdigit():
        print("Error: PIN must contain only numbers!")
    else:
        print("Correct PIN given successfully!")
    break
if entered_pin == pin:
    # 3. The main ATM menu loop
    while True:
        print("\nMain Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")
        
        if choice == "1":
            print(f"Your current balance is: ${balance}")
            
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            balance += amount # This is the same as balance = balance + amount
            print(f"Successfully deposited ${amount}")
            
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            # Logical Check: Don't let them take money they don't have!
            if amount > balance:
                print("Insufficient funds!")
            else:
                balance -= amount
                print(f"Please take your cash: ${amount}")
                
        elif choice == "4":
            print("Thank you for using Python Bank. have a nice day!")
            break # Exit the loop and end the program
            
        else:
            print("Invalid option. Please try again.")
else:
    print("Incorrect PIN. Access Denied.")