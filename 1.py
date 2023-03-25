class Car:
    def __init__(self, car, year, mileage):
        self.__car = car
        self.__year = year
        self.__mileage = mileage

    def info(self):
        print(f'Машина = {self.__car}, год = {self.__year}, lastname = {self.__mileage}')

    def get_car(self):
        return self.__car

    def get_mileage(self):
        return self.__mileage

car_1 = Car('Peugeot', '2000', '270000')
car_2 = Car('Kia', '2010', '220000')

car_1.info()