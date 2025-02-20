import json
import sys
import time
from datetime import datetime

global username, phone_number, email, password,initial_balance
user_file = "user_details.json"  # JSON file to store user data
def load_users():
    try:
        with open(user_file, "r") as file:
            return json.load(file) or []  # Load data, return empty list if None/invalid
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return empty list if file is missing or corrupted

def save_users(users):
    with open(user_file, "w") as file:
        json.dump(users, file, indent=4)

# Function for user registration
def user_registration():
    global username, phone_number, email, password,initial_balance
    print("Enter the following details for Registration")
    username = input("Enter the username: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    confirm_password = input("Confirm the password: ")

    if password != confirm_password:
        print("Passwords do not match! Please try again.")
        return user_registration()  # Restart registration
    try:
        initial_balance = int(input("Enter the initial balance: "))
    except ValueError:
        print("Invalid balance amount! Enter numbers only.")
        return user_registration()
    user_details = {
        "username": username,
        "phone_number": phone_number,
        "email": email,
        "password": password,
        "initial_balance": initial_balance,
        "transaction":[]
    }
    users = load_users()
    users.append(user_details)  # Append new user
    save_users(users)  # Save updated data
    print("User registration successful!")
    time.sleep(2)
    homepage()


def login():
    users = load_users()
    print("Loaded users:", users)  # Debugging step
    print("Enter the details for Login")

    entered_username = input("Enter the username: ")
    entered_password = input("Enter the password: ")

    for user in users:
        print("Checking user:", user)  # Debugging step
        if "username" not in user or "password" not in user:
            print("Error: Missing 'username' or 'password' in user data!")
            continue
        if user["username"] == entered_username and user["password"] == entered_password:
            print("***Login successful!***")
            print("**Welcome to the Dashboard!!**")
            time.sleep(2)
            dashboard(user)
            return
    print("Invalid username or password. Try again.")  # If no match is found
    homepage()

def exit_app():
    print("Exiting... Goodbye!")
    sys.exit()

def dashboard(user):
    print("\n1. Wallet Operations 2. Coupons 3. Transaction History\n4. Update Profile\n5. Logout")
    option = input("Please Select the Option: ")

    if option == "1":
        wallet_operations(user)
    elif option == "2":
        coupons(user)
    elif option == "3":
        transaction_history()
    elif option == "4":
        update_profile()
    elif option == "5":
        print("Logging out... Returning to homepage.")
        time.sleep(2)
        homepage()
    else:
        print("Invalid option! Try again.")
        dashboard(user)


def transaction_history(user):
    print("Transaction History:")
    print(f"{'Time':<20} {'Type':<10} {'Amount':<10} {'Balance':<10}")
    print("-" * 50)

    if "transactions" in user and user["transactions"]:
        for tx in user["transactions"]:
            print(f"{tx['time']:<20} {tx['type']:<10} {tx['amount']:<10} {tx['balance']:<10}")
    else:
        print("No transactions found!")

    time.sleep(3)
    dashboard(user)

def wallet_operations(user):
    users = load_users()
    print("\n1. Check Balance 2. Deposit Money\n3. Withdraw Money 4. Dashboard")
    option = input("Please select the option: ")

    if option == "1":
        time.sleep(1)
        print(f"Available balance: {user['initial_balance']} /-")
        time.sleep(3)
        wallet_operations(user)

    elif option == "2":
        time.sleep(1)
        try:
            deposit = int(input("Enter the amount to deposit: "))
            user["initial_balance"] += deposit

            # Ensure transactions list exists in user data
            if "transactions" not in user:
                user["transactions"] = []

            # Save transaction inside user data
            user["transactions"].append({
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "type": "Deposit",
                "amount": deposit,
                "balance": user["initial_balance"]
            })

            print("***Deposit Successful!***")
        except ValueError:
            print("Invalid amount! Enter numbers only.")
            time.sleep(3)
            wallet_operations(user)

    elif option == "3":
        time.sleep(1)
        try:
            withdraw = int(input("Enter the amount to withdraw: "))
            if withdraw > user["initial_balance"]:
                print("Insufficient balance!")
            else:
                user["initial_balance"] -= withdraw
                print("***Withdrawal Successful!***")

                # Ensure transactions list exists
                if "transactions" not in user:
                    user["transactions"] = []

                # Save transaction inside user data
                user["transactions"].append({
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "type": "Withdraw",
                    "amount": withdraw,
                    "balance": user["initial_balance"]
                })
        except ValueError:
            print("Invalid amount! Enter numbers only.")
            time.sleep(3)
            wallet_operations(user)

    elif option == "4":
        dashboard(user)
        return

    # Save user data to JSON file
    for i in range(len(users)):
        if users[i]["username"] == user["username"]:
            users[i] = user
            break
    save_users(users)  # Save changes
    wallet_operations(user)


def coupons(user):
    users = load_users()
    print("\nAvailable Coupons:")
    print("1. SAVE10 (10% Bonus)\n2. SALE20 (20% Bonus)\n3. NORETURN5 (5% Bonus)")
    option = input("Select a coupon to apply: ")

    if option == "1":
        discount = (10 * user["initial_balance"]) / 100
        user["initial_balance"] += discount
        print(f"Coupon applied! New balance: {user['initial_balance']} /-")
        time.sleep(3)
        dashboard(user)

    elif option == "2":
        discount = (20 * user["initial_balance"]) / 100
        user["initial_balance"] += discount
        print(f"Coupon applied! New balance: {user['initial_balance']} /-")
        time.sleep(3)
        dashboard(user)

    elif option == "3":
        discount = (5 * user["initial_balance"]) / 100
        user["initial_balance"] += discount
        print(f"Coupon applied! New balance: {user['initial_balance']} /-")
        time.sleep(3)
        dashboard(user)

    else:
        print("Invalid coupon selection!")
    trans_history.append({
        "time": datetime.now().strftime("%Y-%m-%d"),
        "type": "Discount",
        "amount": "discount",
        "balance": user["initial_balance"]
    })
    # Update user in list and save
    for i in range(len(users)):
        if users[i]["username"] == user["username"]:
            users[i] = user
            break
    save_users(users)
    dashboard(user)

def transaction_history():
    print("Transaction History")
    print(f"{'Time':<20} {'Type':<10} {'Amount':<10} {'Balance':<10}")
    print("-" * 50)
    for tx in trans_history:
        print(f"{tx['time']:<20} {tx['type']:<10} {tx['amount']:<10} {tx['balance']:<10}")


def update_profile(user):
    users = load_users()

    print("Update Your Profile:")
    new_username = input(f"New Username ({user['username']}): ").strip()
    new_phone = input(f"New Phone Number ({user['phone_number']}): ").strip()
    new_email = input(f"New Email ({user['email']}): ").strip()
    new_password = input(f"New Password (leave empty to keep current): ").strip()

    # Update only if the user provided new values
    if new_username:
        user["username"] = new_username
    if new_phone:
        user["phone_number"] = new_phone
    if new_email:
        user["email"] = new_email
    if new_password:
        user["password"] = new_password  # Consider hashing for better security

    # Save the updated user data back to the JSON file
    for i in range(len(users)):
        if users[i]["email"] == user["email"]:  # Identify user by unique email
            users[i] = user
            break

    save_users(users)
    print("Profile updated successfully!")

    time.sleep(2)
    dashboard(user)


def homepage():
    print("\n1. Registration\n2. Login\n3. Exit")
    option = input("Select the option: ")

    if option == "1":
        user_registration()
    elif option == "2":
        login()
    elif option == "3":
        exit_app()
    else:
        print("Invalid option! Please enter 1, 2, or 3.")
        homepage()

# Start the application
print("Welcome to the E-wallet Application")
time.sleep(2)
homepage()
