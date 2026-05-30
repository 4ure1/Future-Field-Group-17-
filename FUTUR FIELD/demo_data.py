# Creation of a demo account to try our program

from models import Farmer, Crop, Production, MarketPrice, Expense, IrrigationSystem, LightSystem
from file_handler import (load_data, save_data, USERS_FILE, CROPS_FILE, MARKET_FILE, INSTRUMENTS_FILE, EXPENSES_FILE)


def is_already_seeded():
    # check if the demo account already exists
    users = load_data(USERS_FILE)
    for u in users:
        if u["name"] == "Demo Farmer":
            return True
    return False


def demo_users():
    users = load_data(USERS_FILE)

    demo = Farmer(
        name      = "Demo Farmer",
        phone     = "00000000",
        farm_name = "Green Valley Farm",
        region    = "Centre (Ouagadougou)",
        password  = "demo123"
    )
    users.append(demo.to_dict())
    save_data(USERS_FILE, users)


def demo_market():
    # real Burkina Faso markets prices 2025-2026
    prices = []

    crop_prices = [
        ("Maize",        150, 125, "kg", "crop"),
        ("Millet",       130, 110, "kg", "crop"),
        ("Sorghum",      120, 100, "kg", "crop"),
        ("Cowpea",       350, 300, "kg", "crop"),
        ("Groundnut",    400, 350, "kg", "crop"),
        ("Sesame",       500, 450, "kg", "crop"),
        ("Cotton",       275, 250, "kg", "crop"),
        ("Tomato",       200, 175, "kg", "crop"),
        ("Onion",        150, 130, "kg", "crop"),
        ("Yam",          180, 160, "kg", "crop"),
        ("Sweet Potato", 120, 105, "kg", "crop"),
        ("Okra",         250, 220, "kg", "crop"),
    ]

    input_prices = [
        ("NPK Fertiliser",        450, 400, "kg",    "input"),
        ("Urea Fertiliser",       380, 340, "kg",    "input"),
        ("Pesticide",            3500, 3000, "litre", "input"),
        ("Herbicide",            2800, 2400, "litre", "input"),
        ("Certified Maize Seed",  600, 500, "kg",    "input"),
        ("Cowpea Seed",           700, 620, "kg",    "input"),
        ("Sorghum Seed",          450, 400, "kg",    "input"),
    ]

    for name, current, last_year, unit, category in crop_prices + input_prices:
        mp = MarketPrice(name, current, last_year, unit, category)
        prices.append(mp.to_dict())

    save_data(MARKET_FILE, prices)


def demo_crops():
    crops = []

    # 3 demo crops with productions records
    crop_data = [
        ("Maize",  "cereal",    10.0, "15/04/2026", "15/08/2026", 4500, 5000),
        ("Cowpea", "legume",     5.0, "20/04/2026", "20/07/2026", 1800, 2000),
        ("Tomato", "vegetable",  3.0, "01/03/2026", "01/06/2026", 2700, 2500),
    ]

    for name, ctype, area, plant, harvest, qty, expected in crop_data:
        crop = Crop(name, ctype, area, plant, harvest)
        d    = crop.to_dict()

        prod            = Production(name, "2026", qty, expected, area)
        d["production"] = prod.to_dict()

        crops.append(d)

    save_data(CROPS_FILE, crops)


def demo_expenses():
    expenses = []

    demo_expenses = [
        ("fertiliser", 15000, "01/04/2026", "NPK for all fields"),
        ("seeds",       8000, "10/04/2026", "Certified maize and cowpea seeds"),
        ("labour",     20000, "15/04/2026", "Planting labour costs"),
        ("pesticide",   25000, "01/05/2026", "Pesticide application"),
        ("water",       10000, "15/05/2026", "Irrigation water costs"),
    ]

    for category, amount, date, description in demo_expenses:
        exp = Expense(category, amount, date, description)
        expenses.append(exp.to_dict())

    save_data(EXPENSES_FILE, expenses)


def demo_instruments():
    irrigation      = IrrigationSystem("Main Irrigation System", 30, 40)
    irrigation.mode = "auto"

    light = LightSystem("Main Lighting System", "06:00", "20:00", 100)

    save_data(INSTRUMENTS_FILE, [irrigation.to_dict(), light.to_dict()])


def run_demo():
    # Adding of demo data
    if is_already_seeded():
        return

    demo_users()
    demo_market()
    demo_crops()
    demo_expenses()
    demo_instruments()

    print("  Demo data loaded.")
    print("  Login with: Demo Farmer / demo123")
