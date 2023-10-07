import csv


class Car:
    def __init__(self, manufacturer, model, year=2020, mileage=0, fuel_efficiency=0.0):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_efficiency = fuel_efficiency

        with open('cars.csv', mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            writer.writerow([self.model, self.manufacturer])

    def __str__(self):
        return f"Car: {self.manufacturer} {self.model}, Year: {self.year}, Mileage: {self.mileage} km, Fuel Efficiency: {self.fuel_efficiency} L/100km"


class Truck(Car):
    def __init__(self, manufacturer, model, year=2020, mileage=0, fuel_efficiency=0.0, cargo_capacity=0):
        super().__init__(manufacturer, model, year, mileage, fuel_efficiency)
        self.cargo_capacity = cargo_capacity


class SportsCar(Car):
    def __init__(self, manufacturer, model, year=2020, mileage=0, fuel_efficiency=0.0, max_speed=0, price=0):
        super().__init__(manufacturer, model, year, mileage, fuel_efficiency)
        self.max_speed = max_speed
        self.price = price


truck = Truck("Volvo", "VNL", 2019, 50000, 15.0, 30000)
sports_car = SportsCar("Porsche", "911", 2022, 1000, 12.0, 300, 150000)

print(truck)
print(sports_car)
