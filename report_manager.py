# Season reports, year-over-year comparison, best crop.

from models import Production, MarketPrice
from file_handler import (load_data, CROPS_FILE,
                           MARKET_FILE, EXPENSES_FILE, boldLine, thinLine)


def season_report():
    # A mini report of your production to keep the farm evolution in track
    print(f"\n{boldLine}")
    print("  SEASON REPORT")
    print(boldLine)

    crops    = load_data(CROPS_FILE)
    prices   = load_data(MARKET_FILE)
    expenses = load_data(EXPENSES_FILE)

    if len(crops) == 0:
        print("  No data available.")
        return

    total_expenses = 0.0
    for e in expenses:
        total_expenses += e["amount"]

    total_produced = 0.0
    total_revenue  = 0.0

    print(f"\n  Number of crops: {len(crops)}\n")
    print(thinLine)

    for c in crops:
        print(f"  Crop: {c['name']} ({c['area_hectares']} ha)")

        if c["production"] is not None:
            p    = c["production"]
            prod = Production(
                p["crop_name"], p["year"],
                p["quantity_produced"], p["expected_quantity"],
                p["area_hectares"]
            )
            print(f"    Produced : {p['quantity_produced']} kg")
            print(f"    Yield    : {prod.get_yield()} kg/ha")
            print(f"    Target   : {prod.get_achievement_rate()}%")
            total_produced += p["quantity_produced"]

            for pr in prices:
                if pr["product_name"].lower() == c["name"].lower():
                    revenue = p["quantity_produced"] * pr["current_price"]
                    total_revenue += revenue
                    print(f"    Revenue  : {revenue} FCFA")
                    break
        else:
            print("    No production recorded.")
        print()

    net_profit = total_revenue - total_expenses
    print(thinLine)
    print(f"  Total produced  : {total_produced} kg")
    print(f"  Total revenue   : {total_revenue} FCFA")
    print(f"  Total expenses  : {total_expenses} FCFA")
    print(f"  NET PROFIT      : {net_profit} FCFA")
    print(f"  Season result   : {'Profitable' if net_profit >= 0 else 'Loss-making'}")


def compare_years():
    # Indicator according to the precedent year
    print(f"\n{boldLine}")
    print("  YEAR-OVER-YEAR COMPARISON")
    print(boldLine)

    prices = load_data(MARKET_FILE)

    if len(prices) == 0:
        print("  No market prices registered.")
        return

    print("  Price changes vs last year:\n")

    for p in prices:
        price_obj = MarketPrice(
            p["product_name"], p["current_price"],
            p["last_year_price"], p["unit"]
        )
        rate  = price_obj.get_increase_rate()
        arrow = "UP" if rate >= 0 else "DOWN"
        print(f"  {p['product_name']} : {arrow} {abs(rate)}%")
        print(f"    {p['last_year_price']} -> {p['current_price']} FCFA/{p['unit']}")


def best_product():
    # Top crop and it's revenue
    print(f"\n{boldLine}")
    print("  BEST PERFORMING CROP")
    print(boldLine)

    crops  = load_data(CROPS_FILE)
    prices = load_data(MARKET_FILE)

    best_name    = None
    best_revenue = 0.0

    for c in crops:
        if c["production"] is None:
            continue

        quantity = c["production"]["quantity_produced"]

        for p in prices:
            if p["product_name"].lower() == c["name"].lower():
                revenue = quantity * p["current_price"]
                if revenue > best_revenue:
                    best_revenue = revenue
                    best_name    = c["name"]
                break

    if best_name is None:
        print("  Not enough data to find the best crop.")
    else:
        print(f"  Best crop : {best_name}")
        print(f"  Revenue   : {best_revenue} FCFA")


def reports_menu():
    while True:
        print(f"\n{thinLine}")
        print("  REPORTS & STATISTICS")
        print(thinLine)
        print("  [1] Full season report")
        print("  [2] Year-over-year comparison")
        print("  [3] Best performing crop")
        print("  [4] Back")

        choice = input("\n  Your choice : ")

        if choice == "1":
            season_report()
        elif choice == "2":
            compare_years()
        elif choice == "3":
            best_product()
        elif choice == "4":
            break
        else:
            print("  Invalid choice.")
