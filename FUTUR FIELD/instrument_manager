# Manages the automation of irrigation and lighting instruments.

from models import IrrigationSystem, LightSystem
from file_handler import load_data, save_data, INSTRUMENTS_FILE, thinLine


def init_instruments():
    # add default instruments if the file is empty
    instruments = load_data(INSTRUMENTS_FILE)

    if len(instruments) == 0:
        irrigation = IrrigationSystem("Main irrigation", 30, 40)
        light      = LightSystem("Main lighting", "06:00", "20:00", 100)
        save_data(INSTRUMENTS_FILE, [irrigation.to_dict(), light.to_dict()])


def build_instrument(data):
    # rebuild an instrument object from the saved dictionary
    if data["instrument_type"] == "irrigation":
        obj = IrrigationSystem(
            data["name"],
            data["duration_minutes"],
            data["humidity_threshold"]
        )
        obj.is_on           = data["is_on"]
        obj.mode            = data["mode"]
        obj.last_activation = data["last_activation"]
    else:
        obj = LightSystem(
            data["name"],
            data["on_time"],
            data["off_time"],
            data["intensity"]
        )
        obj.is_on = data["is_on"]
        obj.mode  = data["mode"]
    return obj


def show_instruments():
    # Shows active instrument and there status (manual or auto mode)
    print(f"\n{thinLine}")
    print("  INSTRUMENT STATUS")
    print(thinLine)

    instruments = load_data(INSTRUMENTS_FILE)

    for i, inst in enumerate(instruments, 1):
        obj = build_instrument(inst)
        print(f"  [{i}] {obj.get_status()}")


def toggle_instrument():
    # On / Off 
    print(f"\n{thinLine}")
    print("  TOGGLE ON / OFF")
    print(thinLine)

    instruments = load_data(INSTRUMENTS_FILE)

    for i, inst in enumerate(instruments, 1):
        state = "ON" if inst["is_on"] else "OFF"
        print(f"  [{i}] {inst['name']} — {state}")

    choice = input("  Pick an instrument : ")

    try:
        idx = int(choice) - 1
        obj = build_instrument(instruments[idx])
        obj.toggle()
        instruments[idx] = obj.to_dict()
        save_data(INSTRUMENTS_FILE, instruments)
    except (ValueError, IndexError):
        print("  Invalid choice.")


def set_auto_mode():
    print(f"\n{thinLine}")
    print("  CONFIGURE AUTO MODE")
    print(thinLine)

    instruments = load_data(INSTRUMENTS_FILE)

    for i, inst in enumerate(instruments, 1):
        print(f"  [{i}] {inst['name']} (current mode: {inst['mode']})")

    choice = input("  Pick an instrument : ")

    try:
        idx  = int(choice) - 1
        inst = instruments[idx]
        obj  = build_instrument(inst)

        if inst["instrument_type"] == "irrigation":
            duration  = input("  Watering duration (minutes) : ")
            threshold = input("  Humidity threshold to trigger auto (%) : ")
            obj.duration_minutes   = int(duration)
            obj.humidity_threshold = int(threshold)

        elif inst["instrument_type"] == "lighting":
            on_time   = input("  Auto-on time (HH:MM) : ")
            off_time  = input("  Auto-off time (HH:MM) : ")
            intensity = input("  Intensity (1-100) : ")
            obj.on_time   = on_time
            obj.off_time  = off_time
            obj.intensity = int(intensity)

        obj.set_mode("auto")
        instruments[idx] = obj.to_dict()
        save_data(INSTRUMENTS_FILE, instruments)
        print("  Settings saved.")

    except (ValueError, IndexError):
        print("  Invalid choice.")


def simulate_auto():
    # Simulation of auto mode to show how it work
    print(f"\n{thinLine}")
    print("  SIMULATE AUTO TRIGGER")
    print(thinLine)

    instruments = load_data(INSTRUMENTS_FILE)

    for inst in instruments:
        obj = build_instrument(inst)

        if obj.mode != "auto":
            print(f"  {obj.name} — manual mode, skipped.")
            continue

        if inst["instrument_type"] == "irrigation":
            try:
                humidity = int(input(f"  Current soil humidity (%) for {obj.name} : "))
                if humidity < obj.humidity_threshold:
                    print(f"  {humidity}% < {obj.humidity_threshold}% threshold — triggering!")
                    obj.activate()
                else:
                    print(f"  Humidity is fine ({humidity}%). No watering needed.")
            except ValueError:
                print("  Invalid value.")

        elif inst["instrument_type"] == "lighting":
            current_time = input(f"  Current time (HH:MM) for {obj.name} : ")
            if obj.on_time <= current_time <= obj.off_time:
                print(f"  {current_time} is withinLine schedule ({obj.on_time}–{obj.off_time}) — triggering!")
                obj.activate()
            else:
                print(f"  Outside schedule ({obj.on_time}–{obj.off_time}).")

    save_data(INSTRUMENTS_FILE, instruments)


def instruments_menu():
    init_instruments()

    while True:
        print(f"\n{thinLine}")
        print("  AUTOMATIC INSTRUMENTS")
        print(thinLine)
        print("  [1] View instrument status")
        print("  [2] Toggle on / off")
        print("  [3] Configure auto mode")
        print("  [4] Simulate auto trigger")
        print("  [5] Back")

        choice = input("\n  Your choice : ")

        if choice == "1":
            show_instruments()
        elif choice == "2":
            toggle_instrument()
        elif choice == "3":
            set_auto_mode()
        elif choice == "4":
            simulate_auto()
        elif choice == "5":
            break
        else:
            print("  Invalid choice.")
