class Car:
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """Модель аккумулятора для электромобиля."""

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def upgrate_battery(self, battery_size=100):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range_miles = 260
        elif self.battery_size == 100:
            range_miles = 315
        else:
            range_miles = 200

        print(f"This car can go about {range_miles} miles on a full charge.")


class ElectricCar(Car):
    """Электромобиль (наследуется от Car)."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# Создание объекта
my_tesla = ElectricCar('tesla', 'model s', 2019)

# Вывод информации
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.upgrate_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
