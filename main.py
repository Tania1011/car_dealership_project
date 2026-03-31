from car import Car
from database import (initialize_database, import_cars, add_car, get_all_cars,
                      get_car_by_id, update_car, delete_car, search_cars)

def show_menu():
    print("\n" + "="*40)
    print("   🚗  CAR DEALERSHIP MANAGER")
    print("="*40)
    # Print options 1–6
    print("1. Add New Car")
    print("2. View All Cars")
    print("3. Update Car Details")
    print("4. Delete Car")
    print("5. Search Car")
    print("6. Exit")
    # Return the user's input
    return input("\nChoose an option(1-6): ")  

# Add
def add_car_flow():
    try:
        make = input("Enter Make: ")
        model = input("Enter Model: ")
        year = int(input("Enter Year: "))
        price  = float(input("Enter Price: "))
        mileage = int(input("Enter Mileage: "))

        car = Car(make, model, year, price, mileage)
        add_car(car)

        print (f"✅ Car added successfully with ID:{car.id})")
    except ValueError as e:
        print (f"❌ Invalid input: {e}")

# View
def view_all_cars_flow():
    cars = get_all_cars()
    if not cars:
        print("No cars in inventory.")
        return
    
    for car in cars:
        print (car)

# Edit
def update_car_flow():
    try:
        car_id = int(input("Enter car ID to update: "))

        car = get_car_by_id(car_id)
        if not car:
            print("❌ Car not found.")
            return

        print(f"\n Current details:\n{car}\n")
        print("Enter new values: Press Enter to keep current value.")

        if new_make := input(f"Make [{car.make}]: "):
            car.make = new_make

        if new_model := input(f"Model [{car.model}]: "):
            car.model = new_model

        if new_year := input(f"Year [{car.year}]: "):
            car.year = int(new_year)

        if new_price := input(f"Price [{car.price}]: "):
            car.price = float(new_price)

        if new_mileage := input(f"Mileage [{car.mileage}]: "):
            car.mileage = int(new_mileage)

        update_car(car)
        print("✅ Car updated successfully.")

    except ValueError:
        print("❌ Invalid input.")

# Delete
def delete_car_flow():
    try:
        car_id = int(input("Enter car ID to confirm: "))
        car = get_car_by_id(car_id)
        if not car:
            print("❌ Car not found.")
            return

        print (car)
        confirm  =  input ("Are you sure you want to delete? (y/n): ").strip().lower()
        if confirm == "y":
            if delete_car(car_id):
                    print("✅ Car deleted successfully.")
            else:
                    print("❌ Failed to delete.")
        else:
            print("Deletion Cancelled.")
    except ValueError:
        print("❌ Invalid input.")

# Search
def search_cars_flow():
    keyword = input("Enter search keyword: ").strip()
    if not keyword:
        print("No keyword entered")
        return

    results = search_cars(keyword)
    if not results:
        print("No matching cars found")
        return

    print(f"\n Found {len(results)} car(s):")
    for car in results:
        print(car)



def main():
    initialize_database()  # Always call this first!
    import_cars()          # Load sample data if the table is empty
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            add_car_flow()
        elif choice == "2":
            view_all_cars_flow()
        elif choice == "3":
            update_car_flow()
        elif choice == "4":
            delete_car_flow()
        elif choice == "5":
            search_cars_flow()
        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter 1–6.")


if __name__ == "__main__":
    main()