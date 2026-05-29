# Market prices, expenses and profit calculation.

from models import MarketPrice, Expense
from file_handler import (load_data, save_data, MARKET_FILE, EXPENSES_FILE, CROPS_FILE, thinLine)


def add_price():
    print(f"\n{thinLine}")
    print("  ADD A MARKET PRICE")
    print(thinLine)

    print("  Category :")
    print("  [1] Crop (maize, millet...)")
    print("  [2] Input (fertiliser, pesticide...)")
    cat_choice = input("  Your choice : ")
    category   = "input" if cat_choice == "2" else "crop"

    product   = input("  Product name : ")
    current   = input("  Current price (FCFA) : ")
    last_year = input("  Price last year (FCFA) : ")
    unit      = input("  Unit [kg] : ") or "kg"

    price  = MarketPrice(product, float(current), float(last_year), unit, category)
    prices = load_data(MARKET_FILE)

    # update if the product already exists
    updated = False
    for i, p in enumerate(prices):
        if p["product_name"].lower() == product.lower():
            prices[i] = price.to_dict()
            updated   = True
            break

    if not updated:
        prices.append(price.to_dict())

    save_data(MARKET_FILE, prices)
    print(f"\n  {price.get_info()}")


def add_expense():
    print(f"\n{thinLine}")
    print("  ADD AN EXPENSE")
    print(thinLine)

    print("  Category :")
    for i, cat in enumerate(Expense.CATEGORIES, 1):
        print(f"    [{i}] {cat}")

    choice = input("  Your choice : ")
    try:
        category = Expense.CATEGORIES[int(choice) - 1]
    except (ValueError, IndexError):
        category = "other"

    amount      = input("  Amount (FCFA) : ")
    date        = input("  Date (DD/MM/YYYY) : ")
    description = input("  Description : ")

    expense  = Expense(category, float(amount), date, description)
    expenses = load_data(EXPENSES_FILE)
    expenses.append(expense.to_dict())
    save_data(EXPENSES_FILE, expenses)

    print(f"\n  Saved: {expense.get_info()}")


def calculate_profit():
    print(f"\n{thinLine}")
    print("  PROFIT CALCULATION")
    print(thinLine)

    crops    = load_data(CROPS_FILE)
    prices   = load_data(MARKET_FILE)
    expenses = load_data(EXPENSES_FILE)

    total_expenses = 0.0
    for e in expenses:
        total_expenses += e["amount"]

    print(f"  Total expenses: {total_expenses} FCFA\n")

    total_revenue = 0.0

    for c in crops:
        if c["production"] is None:
            continue

        quantity = c["production"]["quantity_produced"]

        # find the matching market price
        price_found = None
        for p in prices:
            if p["product_name"].lower() == c["name"].lower() and p["category"] == "crop":
                price_found = p
                break

        if price_found is None:
            print(f"  {c['name']} — no market price found")
            continue

        gross          = quantity * price_found["current_price"]
        total_revenue += gross

        print(f"  {c['name']}")
        print(f"    {quantity} kg x {price_found['current_price']} FCFA/{price_found['unit']}")
        print(f"    Gross revenue: {gross} FCFA")

    net_profit = total_revenue - total_expenses
    print(f"\n{thinLine}")
    print(f"  Total revenue  : {total_revenue} FCFA")
    print(f"  Total expenses : {total_expenses} FCFA")
    print(f"  NET PROFIT     : {net_profit} FCFA")
    print(f"  Season result  : {'Profitable' if net_profit >= 0 else 'Loss-making'}")


def list_prices():
    print(f"\n{thinLine}")
    print("  MARKET PRICES")
    print(thinLine)

    prices = load_data(MARKET_FILE)

    if len(prices) == 0:
        print("  No prices registered yet.")
        return

    print("  -- Crops --")
    for p in prices:
        if p.get("category", "crop") == "crop":
            price_obj = MarketPrice(
                p["product_name"], p["current_price"],
                p["last_year_price"], p["unit"],
                p.get("category", "crop")
            )
            print(f"  {price_obj.get_info()}")

    print("\n  -- Inputs --")
    for p in prices:
        if p.get("category", "crop") == "input":
            price_obj = MarketPrice(
                p["product_name"], p["current_price"],
                p["last_year_price"], p["unit"],
                p.get("category", "input")
            )
            print(f"  {price_obj.get_info()}")


def list_expenses():
    print(f"\n{thinLine}")
    print("  MY EXPENSES")
    print(thinLine)

    expenses = load_data(EXPENSES_FILE)

    if len(expenses) == 0:
        print("  No expenses yet.")
        return

    total = 0.0
    for e in expenses:
        exp_obj = Expense(e["category"], e["amount"], e["date"], e["description"])
        print(f"  {exp_obj.get_info()}")
        total += e["amount"]

    print(f"\n  TOTAL: {total} FCFA")


def market_menu():
    while True:
        print(f"\n{thinLine}")
        print("  MARKET & FINANCES")
        print(thinLine)
        print("  [1] View market prices")
        print("  [2] Add / update a price")
        print("  [3] View my expenses")
        print("  [4] Add an expense")
        print("  [5] Calculate profit")
        print("  [6] Back")

        choice = input("\n  Your choice : ")

        if choice == "1":
            list_prices()
        elif choice == "2":
            add_price()
        elif choice == "3":
            list_expenses()
        elif choice == "4":
            add_expense()
        elif choice == "5":
            calculate_profit()
        elif choice == "6":
            break
        else:
            print("  Invalid choice.")
  
