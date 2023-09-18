from calculator import Calculator, Car, ElectcicCar

if __name__ == '__main__':
    calc = Calculator()
    opel = Car('Ople Astra GTC', 284000, 7.5, 8000, 10000)
    land_cruiser = Car('Land Cruiser', 1500000, 10, 15000, 10000)
    ford_focus = Car('Focus', 400000, 7.8, 7000, 13000)
    calc.add_car(opel)
    calc.add_car(land_cruiser)
    calc.add_car(ford_focus)
    calc.print_cars()
