# Reads and writes all the JSON files (Our local database).
# Every other module uses load_data() and save_data() from here.

import json
import os

# file paths
USERS_FILE       = "data/users.json"
CROPS_FILE       = "data/crops.json"
MARKET_FILE      = "data/market.json"
INSTRUMENTS_FILE = "data/instruments.json"
EXPENSES_FILE    = "data/expenses.json"
HISTORY_FILE     = "data/history.json"

# separator for our interface
boldLine  = "=" * 55
thinLine = "-" * 55


def init_files():
    # create the data folder and empty JSON files if they don't exist
    if not os.path.exists("data"):
        os.makedirs("data")

    files = [
        USERS_FILE, CROPS_FILE, MARKET_FILE,
        INSTRUMENTS_FILE, EXPENSES_FILE, HISTORY_FILE
    ]

    for f in files:
        if not os.path.exists(f):
            with open(f, "w", encoding="utf-8") as file:
                json.dump([], file)


def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
