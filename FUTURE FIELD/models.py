# All the classes used in the project.

# Person -> Farmer
# Instrument -> IrrigationSystem / LightSystem
# Crop, Production, MarketPrice, Expense

from datetime import datetime


class Person:

    def __init__(self, name, phone):
        self.name  = name
        self.phone = phone

    def get_info(self):
        return f"Name: {self.name} | Phone: {self.phone}"

    def to_dict(self):
        return {"name": self.name, "phone": self.phone}


class Farmer(Person):
    # a farmer has extra info on top of a basic person

    def __init__(self, name, phone, farm_name, region, password):
        super().__init__(name, phone)
        self.farm_name = farm_name
        self.region    = region
        self._password = password 

    def check_password(self, password):
        return self._password == password

    def get_info(self):
        return (f"Farmer: {self.name} | Farm: {self.farm_name} "
                f"| Region: {self.region} | Phone: {self.phone}")

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "farm_name": self.farm_name,
            "region":    self.region,
            "password":  self._password,
            "role":      "farmer"
        })
        return base


class Instrument:
    # base class for instruments

    def __init__(self, name, instrument_type):
        self.name            = name
        self.instrument_type = instrument_type
        self.is_on           = False
        self.mode            = "manual"

    def toggle(self):
        self.is_on = not self.is_on
        state = "ON" if self.is_on else "OFF"
        print(f"  {self.name} is now {state}.")

    def set_mode(self, mode):
        self.mode = mode
        print(f"  {self.name} switched to {mode} mode.")

    def get_status(self):
        state = "ON" if self.is_on else "OFF"
        return f"{self.name} | State: {state} | Mode: {self.mode}"

    def to_dict(self):
        return {
            "name":            self.name,
            "instrument_type": self.instrument_type,
            "is_on":           self.is_on,
            "mode":            self.mode
        }


class IrrigationSystem(Instrument):

    def __init__(self, name, duration_minutes=30, humidity_threshold=40):
        super().__init__(name, "irrigation")
        self.duration_minutes   = duration_minutes
        self.humidity_threshold = humidity_threshold
        self.last_activation    = "never"

    def activate(self):
        self.is_on           = True
        self.last_activation = datetime.now().strftime("%d/%m/%Y %H:%M")
        print(f"  Irrigation activated for {self.duration_minutes} minutes.")

    def get_status(self):
        base = super().get_status()
        return (f"{base} | Duration: {self.duration_minutes} min "
                f"| Humidity threshold: {self.humidity_threshold}% "
                f"| Last activation: {self.last_activation}")

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "duration_minutes":   self.duration_minutes,
            "humidity_threshold": self.humidity_threshold,
            "last_activation":    self.last_activation
        })
        return base


class LightSystem(Instrument):

    def __init__(self, name, on_time="06:00", off_time="20:00", intensity=100):
        super().__init__(name, "lighting")
        self.on_time   = on_time
        self.off_time  = off_time
        self.intensity = intensity

    def activate(self):
        self.is_on = True
        print(f"  Lights on at {self.intensity}% intensity.")

    def get_status(self):
        base = super().get_status()
        return (f"{base} | Auto-on: {self.on_time} "
                f"| Auto-off: {self.off_time} "
                f"| Intensity: {self.intensity}%")

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "on_time":   self.on_time,
            "off_time":  self.off_time,
            "intensity": self.intensity
        })
        return base


class Crop:

    TYPES = ("cereal", "vegetable", "fruit", "tuber", "legume", "other")

    def __init__(self, name, crop_type, area_hectares, plant_date, harvest_date):
        self.name          = name
        self.crop_type     = crop_type
        self.area_hectares = float(area_hectares)
        self.plant_date    = plant_date
        self.harvest_date  = harvest_date
        self.status        = "active"

    def get_info(self):
        return (f"{self.name} | Type: {self.crop_type} "
                f"| Area: {self.area_hectares} ha "
                f"| Planted: {self.plant_date} "
                f"| Harvest: {self.harvest_date} "
                f"| Status: {self.status}")

    def to_dict(self):
        return {
            "name":          self.name,
            "crop_type":     self.crop_type,
            "area_hectares": self.area_hectares,
            "plant_date":    self.plant_date,
            "harvest_date":  self.harvest_date,
            "status":        self.status,
            "production":    None
        }


class Production:

    def __init__(self, crop_name, year, quantity_produced, expected_quantity, area_hectares):
        self.crop_name         = crop_name
        self.year              = year
        self.quantity_produced = float(quantity_produced)
        self.expected_quantity = float(expected_quantity)
        self.area_hectares     = float(area_hectares)

    def get_yield(self):
        if self.area_hectares == 0:
            return 0.0
        return round(self.quantity_produced / self.area_hectares, 2)

    def get_achievement_rate(self):
        if self.expected_quantity == 0:
            return 0.0
        return round((self.quantity_produced / self.expected_quantity) * 100, 1)

    def get_estimated_profit(self, price_per_kg, total_expenses=0):
        gross = self.quantity_produced * price_per_kg
        return round(gross - total_expenses, 2)

    def get_info(self):
        rate   = self.get_achievement_rate()
        result = "Target reached" if rate >= 100 else f"Target not reached ({rate}%)"
        return (f"{self.crop_name} {self.year} | "
                f"Produced: {self.quantity_produced} kg | "
                f"Target: {self.expected_quantity} kg | "
                f"Yield: {self.get_yield()} kg/ha | {result}")

    def to_dict(self):
        return {
            "crop_name":         self.crop_name,
            "year":              self.year,
            "quantity_produced": self.quantity_produced,
            "expected_quantity": self.expected_quantity,
            "area_hectares":     self.area_hectares
        }


class MarketPrice:

    def __init__(self, product_name, current_price, last_year_price, unit="kg", category="crop"):
        self.product_name    = product_name
        self.current_price   = float(current_price)
        self.last_year_price = float(last_year_price)
        self.unit            = unit
        self.category        = category

    def get_increase_rate(self):
        if self.last_year_price == 0:
            return 0.0
        return round(
            ((self.current_price - self.last_year_price) / self.last_year_price) * 100, 1
        )

    def get_info(self):
        rate      = self.get_increase_rate()
        direction = "up" if rate >= 0 else "down"
        return (f"[{self.category.upper()}] {self.product_name} | "
                f"Current: {self.current_price} FCFA/{self.unit} "
                f"| Last year: {self.last_year_price} FCFA/{self.unit} "
                f"| {direction} {abs(rate)}%")

    def to_dict(self):
        return {
            "product_name":    self.product_name,
            "current_price":   self.current_price,
            "last_year_price": self.last_year_price,
            "unit":            self.unit,
            "category":        self.category
        }


class Expense:

    CATEGORIES = (
        "fertiliser", "water", "labour",
        "equipment", "seeds", "pesticide", "other"
    )

    def __init__(self, category, amount, date, description):
        self.category    = category
        self.amount      = float(amount)
        self.date        = date
        self.description = description

    def get_info(self):
        return f"{self.category} | {self.amount} FCFA | {self.date} | {self.description}"

    def to_dict(self):
        return {
            "category":    self.category,
            "amount":      self.amount,
            "date":        self.date,
            "description": self.description
        }
