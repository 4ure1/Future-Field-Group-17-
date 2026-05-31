# 🌾 FUTUR FIELD
**Agricultural Management System — CLI Python Application**

FUTUR FIELD is a command-line application designed to help farmers manage their crops, track market prices, monitor expenses, control automated farm instruments, and generate season reports — all from a simple terminal interface.

---

## 👥 Team

| Member | GitHub | Contribution |
|---|---|---|
| **TAPSOBA Aurel** *(Project Lead)* | [@4ure1](https://github.com/4ure1) | `models.py` — all data classes |
| ZIDA Alvine | [@zidaalvine6-oss](https://github.com/zidaalvine6-oss) | `file_handler.py` + `main.py` — file I/O & app entry point |
| ZEBA Grâce | [@Gracezeba](https://github.com/Gracezeba) | `auth.py` + `report_manager.py` — authentication & reports |
| YOUGBARE Huldah | [@yougbarehulda-arch](https://github.com/yougbarehulda-arch) | `demo_data.py` — demo data seeding |
| ZOUNDI Janice | [@janicezoundi4-lab](https://github.com/janicezoundi4-lab) | `crops_manager.py` — crop & harvest management |
| YODA Sawilatou | [@sawilatou](https://github.com/sawilatou) | `market_manager.py` — market prices & expenses |
| ZONGO Djamilatou | [@zongo6461-beep](https://github.com/zongo6461-beep) | `instrument_manager.py` — irrigation & lighting automation |

---

## 📁 Project Structure

```
FUTUR FIELD/
│
├── main.py                 # Entry point — app launch & main menu           (ZIDA Alvine)
├── models.py               # All data classes (Farmer, Crop, Production…)   (TAPSOBA Aurel)
├── auth.py                 # Registration & login                           (ZEBA Grâce)
├── crops_manager.py        # Add crops, record harvests, production alerts  (ZOUNDI Janice)
├── market_manager.py       # Market prices, expenses, profit calculation    (YODA Sawilatou)
├── instrument_manager.py   # Irrigation & lighting automation               (ZONGO Djamilatou)
├── report_manager.py       # Season reports, year-over-year comparison      (ZEBA Grâce)
├── demo_data.py            # Pre-loaded demo data for testing               (YOUGBARE Huldah)
├── file_handler.py         # JSON file I/O (local database)                 (ZIDA Alvine)
│
└── data/                   # Auto-created on first run
    ├── users.json
    ├── crops.json
    ├── market.json
    ├── instruments.json
    ├── expenses.json
    └── history.json
```

---

## ✨ Features

### 🔐 Authentication (`auth.py`) — ZEBA Grâce
- Create a farmer account (name, phone, region, farm name, password)
- Login with name and password
- Demo account available for quick testing

### 🌱 Crop Management (`crops_manager.py`) — ZOUNDI Janice
- Add crops with type, area (hectares), planting date, and expected harvest date
- Record harvests with quantity produced vs. target
- Automatic yield calculation (kg/ha) and achievement rate
- Estimated profit shown at harvest time (if market price is available)
- Production alerts for crops below 70% or 100% of target

### 📈 Market & Finances (`market_manager.py`) — YODA Sawilatou
- Register and update market prices for crops and inputs (fertiliser, pesticides...)
- Prices stored in FCFA with year-over-year comparison
- Track all farm expenses by category (seeds, water, labour, equipment, etc.)
- Full profit calculation: gross revenue − total expenses = net profit

### ⚙️ Automatic Instruments (`instrument_manager.py`) — ZONGO Djamilatou
- Manage an **irrigation system**: duration, humidity threshold, last activation
- Manage a **lighting system**: auto on/off times, intensity
- Toggle instruments ON/OFF manually
- Configure auto mode with custom parameters
- Simulate auto trigger to test threshold-based logic

### 📊 Reports (`report_manager.py`) — ZEBA Grâce
- Full season report: all crops, yields, revenues, and net profit
- Year-over-year price comparison (% change per product)
- Best performing crop by total revenue

### 🌾 Demo Data (`demo_data.py`) — YOUGBARE Huldah
- Pre-loads realistic farm data on first launch (Burkina Faso market prices 2025–2026, in FCFA)
- 3 demo crops with harvest records: Maize (10 ha), Cowpea (5 ha), Tomato (3 ha)
- 12 crop prices + 7 input prices (fertiliser, pesticide…) in market.json
- 5 expenses across all categories (seeds, labour, water, NPK, pesticide)
- Auto irrigation (30 min, 40% threshold) + lighting (06:00–20:00) pre-configured
- `is_already_seeded()` prevents data from loading twice

### 🗃️ Data Persistence (`file_handler.py`) — ZIDA Alvine
- All data stored locally as JSON files under a `data/` folder
- Files are auto-created on first launch
- Every module uses shared `load_data()` and `save_data()` functions

---

## 🚀 Getting Started

### Requirements
- Python 3.10+
- No external libraries required (standard library only)

### Run the app

```bash
git clone https://github.com/4ure1/Future-Field-Group-17-
cd "FUTUR FIELD"
python main.py
```

On first launch, the app creates the `data/` folder and loads demo data automatically.

### Demo account
```
Name     : Demo Farmer
Password : demo123
```

---

## 🏗️ Data Models (`models.py`) — TAPSOBA Aurel

| Class | Description |
|---|---|
| `Person` | Base class — name and phone |
| `Farmer` | Extends Person — adds farm name, region, password |
| `Instrument` | Base class for farm devices — state (on/off), mode (manual/auto) |
| `IrrigationSystem` | Extends Instrument — duration, humidity threshold, last activation |
| `LightSystem` | Extends Instrument — on/off schedule, intensity |
| `Crop` | Name, type, area (ha), planting/harvest dates, status |
| `Production` | Crop harvest record — quantity, target, yield, achievement rate |
| `MarketPrice` | Product price in FCFA — current vs. last year, category |
| `Expense` | Farm expense — category, amount, date, description |

---
