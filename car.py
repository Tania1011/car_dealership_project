class Car:

    # Task 1.1 — Define the class and constructor
    def __init__(self, make, model, year, price, mileage , id=None):
        """constructor"""
        # Call a separate validation function
        self.validate_input( make, model, year, price, mileage)
        # Assign attributes after validation
        self.make = make
        self.model = model 
        self.year = year
        self.price = price
        self.mileage = mileage 
        self.id = id

    # Task 1.2 — Add a __str__ method
    def __str__(self):
        """it display all the car's info in a readable format, user friendly"""

        return (
        f"[ID: {self.id}]"
        f"{self.year} {self.make} {self.model} | "
        f"${self.price:,.2f} | {self.mileage:,} km"
        )
    
    # Task 1.3 — Add a to_tuple() method
    def to_tuple(self):
        # Return all the car's data except the ID, as a tuple in the order: (make, model, year, price, mileage).

        return (
            self.make, 
            self.model, 
            self.year, 
            self.price, 
            self.mileage
            )
    
    # Task 1.4 (Optional Challenge) — Add input validation -  to check the values before assigning them.
    def validate_input(self, make, model, year, price, mileage):
       
        if make.strip() == "" or model.strip() == "":
            raise ValueError("Make and model cannot be empty")
        if year <= 0:
            raise ValueError(f"Year must be positive, got {year}")
        if price < 0:
            raise ValueError(f"Price cannot be negative, got {price}")
        if mileage < 0:
            raise ValueError(f"Mileage cannot be negative, got {mileage}")

test_car = Car("Tesla", "Model 3", 2023, 52000.5, 3000, id=1)
print(test_car)
print(test_car.to_tuple())
test_car2 = Car("Tesla", "Model 2", 2021, 49000.25, 2000, id=2)
print(test_car2)
print(test_car2.to_tuple())
