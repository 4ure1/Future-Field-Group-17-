# Everything related to crops and harvests.

from models import Crop, Production
from file_handler import load_data, save_data, CROPS_FILE, MARKET_FILE, EXPENSES_FILE, thinLine


def get_market_price(crop_name):
    # finding of crop price in the database
    prices = load_data(MARKET_FILE)
    for p in prices:
        if p["product_name"].lower() == crop_name.lower():
            return p["current_price"]
    return None


def get_total_expenses():
    # Calculation of user total expenses
    expenses = load_data(EXPENSES_FILE)
    total = 0.0
    for e in expenses:
        total += e["amount"]
    return total


def add_crop():
    #add new crop
    print(f"\n{thinLine}")
    print("  ADD A NEW CROP")
    print(thinLine)

    name = input("  Crop name (e.g. Maize) : ")

    print("  Crop type :")
    for i, t in enumerate(Crop.TYPES, 1):
        print(f"    [{i}] {t}")

    choice = input("  Your choice : ")
    try:
        crop_type = Crop.TYPES[int(choice) - 1]
    except (ValueError, IndexError):
        crop_type = "other"

    area         = input("  Area (hectares) : ")
    plant_date   = input("  Planting date (DD/MM/YYYY) : ")
    harvest_date = input("  Expected harvest date (DD/MM/YYYY) : ")

    new_crop = Crop(name, crop_type, float(area), plant_date, harvest_date)

    crops = load_data(CROPS_FILE)
    crops.append(new_crop.to_dict())
    save_data(CROPS_FILE, crops)

    print(f"\n  '{name}' added successfully.")


def add_production():
    # Harvest record
    print(f"\n{thinLine}")
    print("  RECORD A HARVEST")
    print(thinLine)

    crops = load_data(CROPS_FILE)

    if len(crops) == 0:
        print("  No crops yet.")
        return

    print("  Pick a crop :")
    for i, c in enumerate(crops, 1):
        print(f"  [{i}] {c['name']} ({c['area_hectares']} ha)")

    choice = input("  Your choice : ")
    try:
        selected = crops[int(choice) - 1]
    except (ValueError, IndexError):
        print("  Invalid choice.")
        return

    year     = input("  Year (e.g. 2026) : ")
    quantity = input("  Quantity produced (kg) : ")
    expected = input("  Target quantity (kg) : ")

    prod = Production(
        selected["name"], year,
        float(quantity), float(expected),
        selected["area_hectares"]
    )

    # attach the production to the right crop
    for c in crops:
        if c["name"] == selected["name"]:
            c["production"] = prod.to_dict()
            break

    save_data(CROPS_FILE, crops)
    print(f"\n  {prod.get_info()}")

    # show estimated profit if we have a market price
    price = get_market_price(selected["name"])
    if price is not None:
        total_expenses = get_total_expenses()
        estimated = prod.get_estimated_profit(price, total_expenses)
        gross     = prod.quantity_produced * price
        print(f"\n  --- ESTIMATED PROFIT ---")
        print(f"  Market price    : {price} FCFA/kg")
        print(f"  Gross revenue   : {gross} FCFA")
        print(f"  Total expenses  : {total_expenses} FCFA")
        print(f"  Estimated profit: {estimated} FCFA")
        print(f"  Result          : {'Profitable' if estimated >= 0 else 'Loss'}")
    else:
        print("  (No market price found — add one in Market to see profit estimate)")


def list_crops():
    # Listing of all the crops if there are some
    print(f"\n{thinLine}")
    print("  MY CROPS")
    print(thinLine)

    crops = load_data(CROPS_FILE)

    if len(crops) == 0:
        print("  No crops yet.")
        return

    for c in crops:
        crop_obj = Crop(
            c["name"], c["crop_type"],
            c["area_hectares"], c["plant_date"], c["harvest_date"]
        )
        print(f"  {crop_obj.get_info()}")

        if c["production"] is not None:
            p        = c["production"]
            prod_obj = Production(
                p["crop_name"], p["year"],
                p["quantity_produced"], p["expected_quantity"],
                p["area_hectares"]
            )
            print(f"    -> {prod_obj.get_info()}")

            price = get_market_price(c["name"])
            if price is not None:
                expenses  = get_total_expenses()
                estimated = prod_obj.get_estimated_profit(price, expenses)
                print(f"    -> Estimated profit: {estimated} FCFA")


def check_alerts():
    # Checking if you are in profit or loss
    print(f"\n{thinLine}")
    print("  PRODUCTION ALERTS")
    print(thinLine)

    crops  = load_data(CROPS_FILE)
    alerts = []

    for c in crops:
        if c["production"] is not None:
            p        = c["production"]
            prod_obj = Production(
                p["crop_name"], p["year"],
                p["quantity_produced"], p["expected_quantity"],
                p["area_hectares"]
            )
            rate = prod_obj.get_achievement_rate()

            if rate < 70:
                alerts.append(f"  WARNING : {c['name']} — only {rate}% of target reached!")
            elif rate < 100:
                alerts.append(f"  NOTICE  : {c['name']} — {rate}% of target reached.")

    if len(alerts) == 0:
        print("  No alerts. EverythinLineg looks fine.")
    else:
        for alert in alerts:
            print(alert)


def crops_menu():
    while True:
        print(f"\n{thinLine}")
        print("  CROP MANAGEMENT")
        print(thinLine)
        print("  [1] Add a crop")
        print("  [2] Record a harvest")
        print("  [3] View all crops")
        print("  [4] Production alerts")
        print("  [5] Back")

        choice = input("\n  Your choice : ")

        if choice == "1":
            add_crop()
        elif choice == "2":
            add_production()
        elif choice == "3":
            list_crops()
        elif choice == "4":
            check_alerts()
        elif choice == "5":
            break
        else:
            print("  Invalid choice.")



    


    
