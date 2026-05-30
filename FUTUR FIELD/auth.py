# auth.py
# Login and accounts creation.
# Accounts are saved in data/users.json.

from models import Farmer
from file_handler import load_data, save_data, USERS_FILE, boldLine, thinLine


def register():
    print(f"\n{thinLine}")
    print("  CREATE AN ACCOUNT")
    print(thinLine)

    users = load_data(USERS_FILE)

    name      = input("  Full name    : ")
    phone     = input("  Phone        : ")
    region    = input("  Region       : ")
    farm_name = input("  Farm name    : ")
    password  = input("  Password     : ")

    # Verification of the name disponibility
    for user in users:
        if user["name"].lower() == name.lower():
            print("  This name is already registered.")
            return

    new_farmer = Farmer(name, phone, farm_name, region, password)
    users.append(new_farmer.to_dict())
    save_data(USERS_FILE, users)

    print(f"\n  Account created! Welcome, {name}.")


def login():
    print(f"\n{thinLine}")
    print("  LOGIN")
    print(thinLine)

    users = load_data(USERS_FILE)

    if len(users) == 0:
        print("  No accounts found. Please register first.")
        return None

    name     = input("  Name     : ")
    password = input("  Password : ")

    # Verification of account informations
    for user in users:
        if user["name"].lower() == name.lower() and user["password"] == password:
            print(f"\n  Welcome back, {user['name']} — {user['farm_name']}!")
            return user

    print("  Wrong name or password.")
    return None


def auth_menu():
    while True:
        print(f"\n{boldLine}")
        print("   FUTURE FIELD — Agricultural Management")
        print(boldLine)
        print("  [1] Login")
        print("  [2] Create an account")
        print("  [3] Quit")
        print(f"\n{thinLine}")
        print("  DEMO ACCOUNT  ->  name: Demo Farmer  |  password: demo123")
        print(thinLine)

        choice = input("\n  Your choice : ")
        
        #redirection
        if choice == "1":
            user = login()
            if user is not None:
                return user

        elif choice == "2":
            register()

        elif choice == "3":
            return None

        else:
            print("  Invalid choice. Please enter 1, 2 or 3.")
