import _json
from datetime import datetime
from models import CropsManager


class Crop:
    def __init__ (self,name,season,area_hectares,production_tons,expenses,revenue,year):
               self.name
               self.season
               self.area_hectares=area_hectares
               self.production_tons=production_tons
               self.expenses=expenses
               self.revenue=revenue
               self.year=year
    
    def calculate_yield(self):
        if self.area_hectares==0:
            return 0
        return self.production_tons / self.area_hectares
    
    def calculate_profit(self):
        return self.revenue - self.expenses

    def to_dict(self):
        return {
            "name":self.Name,
            "season":self.season,
            "area_hectares":self.area_hectares,
            "production_tons":self.production_tons,
            "expenses":self.expenses,
            "revenue":self.revenue,
            "year":self.year
        }
    
    
class CropsManager:
    def __init__(self,file_name="crops_data.json"):
        self.file_name = file_name
        self.crops = []
        self.load_data()

    def add_crop(self):
        print("\n=== Add New Crop ===")
        name = input("Crop name: ")
        season = input("Season: ")
        area_hectares = float(input("Area(hectares): "))
        production_tons = float(input("Production (tons): "))
        expenses = float(input("Expenses: "))
        revenue = float(input("Revenue"))
        year = int(input("Year: "))

        crop = Crop(name,season,area_hectares,production_tons,expenses,year)
        self.crops.append(crop)
        self.save_data()
        print("Crop added successfully.\n")

    def display_crops(self):
        print("\n=== Crop Records ===")
        if not self.crops:
            print("No crop records found.\n")
            return
        
        for index , crop in enumerate(self.crops, start=1):
            print(f"\nRecord #{index}")
            print(f"Crop Name       : {crop.name}")
            print(f"Season          : {crop.season}")
            print(f"Year            : {crop.year}")
            print(f"Area            : {crop.area_hectares} hectares")
            print(f"Production      : {crop.production_tons} tons")
            print(f"Yield           : {crop.calculate_yield():.2f} tons/hectare")
            print(f"Expenses           : {crop.expenses}")
            print(f"Revenue           : {crop.revenue}")
            print(f"Profit          : {crop.calculate_profit()}")
        print()

    def compare_years(self):
        print("\n=== Year Comparaison ===")
        if len(self.crops) < 2:
            print("Not enough data to compare years.\n")
            return

        years = sorted(set(crop.year for crop in self.crops))

        for year in years:
            yearly_crops = [crop for crop in self.crops if crop.year == year]
            total_production = sum(crop.production_tons for crop in yearly_crops)
            total_profit = sum(crop.calculate_profit() for crop in yearly_crops)
            average_yiel = (
                sum(crop.calculate_yield() for crop in yearly_crops) / len(yearly_crops)
            )
            print(f"\nYear: {year}")
            print(f"Total Production : {total_production:.2f} tons")
            print(f"Average Yield    : {average_yiel:.2f} tons/hectare")
            print(f"Total Profit : {total_profit:.2f}")
            print()
    
    def search_crop(self):
        print("\n=== Search Crop ===")
        search_name = input("Entrer crop name").lower()
        found = False

        for crop in self.crops:
            if crop.name.lower() == search_name:
                found = True
                print(f"\nCrop Name  :{crop.name}")
                print(f"Season  :{crop.season}")
                print(f"Year  :{crop.year}")
                print(f"Yield  :{crop.calculate_yield():.2f}")
                print(f"Profit  :{crop.calculate_profit():.2f}")
        if not found:
            print("Crop not found.")
        print()

    def save_data(self):
        data = [crop.to_dict() for crop in self.crops]
        with open(self.file_name, "r") as file:
            data = _json.__load(file)
            for item in data:
                crop = Crop(
                    item["name"],
                    item["season"],
                    item["area_hectares"],
                    item["production_tons"],
                    item["expenses"],
                    item["revenue"],
                    item["year"],
                )
                self.crops = []

    def generate_report(self):
        print("\n=== Farm Report ===")
        total_crops = len(self.crops)
        total_production = sum(crop.production_tons for crop in self.crops)
        total_profit = sum(crop.calculate_profit() for crop in self.crops)

        print(f"Generated On      : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total REcords     : {total_crops}")
        print(f"Total Production  : {total_production:.2f} tons")
        print(f"Total Profit     : {total_profit:.2f}")
        print()


# ========================== Main Program ==========================

    def display_menu():
        print("========== Agricultural Management System ==========")
        print("1. Add Crop")
        print("2. Display All Crops")
        print("3. search Crop")
        print("4. Compare Performance by Year")
        print("5. Generate Farm Report")
        print("6. Exit")

    
    manager = CropsManager()

    while True:
        display_menu()
        choice = input("\nEntrer your choice: ")

        if choice == "1":
            manager.add_crop()
        elif choice =="2":
            manager.display_crops()
        elif choice =="3":
            manager.search_crop()
        elif choice == "4":
            manager.compare_years()
        elif choice == "5":
            manager.generate_report()
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Please try again.\n")



                    






           
           
           
    



        



    


    
