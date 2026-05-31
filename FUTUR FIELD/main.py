# Entry point of the FUTURE FIELD app.

import sys

from auth import auth_menu
from crop_manager import crops_menu
from market_manager import market_menu
from instrument_manager import instruments_menu
from report_manager import reports_menu
from demo_data import run_demo
from file_handler import init_files, boldLine, thinLine


def farm_menu(user):
    # Main menu
    while True:
        print(f"\n{boldLine}")
        print(f"  FUTURE FIELD — {user['farm_name']}")
        print(f"  Farmer: {user['name']} | Region: {user['region']}")
        print(boldLine)
        print("  [1] My Crops")
        print("  [2] Market & Finances")
        print("  [3] Automatic Instruments")
        print("  [4] Reports")
        print("  [5] Log out") 

        choice = input("\n  Your choice : ")

        # Redirection to the different files
        if choice == "1":
            crops_menu()
        elif choice == "2":
            market_menu()
        elif choice == "3":
            instruments_menu()
        elif choice == "4":
            reports_menu()
        elif choice == "5":
            print(f"\n  Goodbye, {user['name']}!")
            break
        else:
            print("  Invalid choice.")


def main():
    init_files()
    run_demo()

    while True:
        user = auth_menu()

        if user is None:
            print("\n  Goodbye!\n")
            sys.exit()

        farm_menu(user)


if __name__ == "__main__":
    main()

