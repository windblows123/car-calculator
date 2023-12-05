from apis import get_gas_price, get_power_price

class Calculator:
    def __init__(self, mileage=15000, years=10, year_loss=10):
        self.mileage = mileage
        self.cars = {}    #Car: Year price
        self.years = years
        self.year_loss = year_loss / 100
    def add_car(self, car):
        year_cost = car.annual_cost(self.mileage)
        left_price = self.get_left_price(car)
        self.cars[car] = car.annual_cost(self.mileage) + (car.price - left_price) / self.years
    def get_left_price(self, car):
        initial_price = car.price
        for _ in range(self.years):
            initial_price -= initial_price * self.year_loss
        return initial_price
    def print_cars(self):
        for car, price in self.cars.items():
            print(f'{car.name}: {int(price)} рублей в год')

class Car:
    def __init__(self,
                 name: str,
                 price: int,
                 fuel_consamption: float,
                 service_cost: int,
                 ensurance_cost: int):
        self.name = name
        self.price = price
        self.fuel_consamption = fuel_consamption
        self.service_cost = service_cost
        self.ensurance_cost = ensurance_cost
    def static_annual_cost(self):
        return self.service_cost + self.ensurance_cost
    def dynamic_annual_cost(self, mileage):
        return self.fuel_consamption * mileage / 100 * get_gas_price()
    def annual_cost(self, mileage: int):
        return self.static_annual_cost() + self.dynamic_annual_cost(mileage)

class ElectcicCar(Car):
    def __init__(self, name: str, price: int, service_cost: int, ensurance_cost: int,
                 power_consamption: int):
        super().__init__(name=name, price=price, fuel_consamption=0, service_cost=0,
                         ensurance_cost=ensurance_cost)
        self.power_consamption = power_consamption

    def dynamic_annual_cost(self, mileage):
        return mileage * self.power_consamption * get_power_price() / 1000

