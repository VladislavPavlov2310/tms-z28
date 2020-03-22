class Car:
    def __init__(self, brand='', model='', year=0, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    def __str__(self):
        return f'Car information:\n' \
               f'Brand: {self.__brand}, model: {self.__model}, year: {self.__year}, speed: {self.__speed}'

    def speed_get(self):
        return print(f'Current speed: {self.__speed}')

    def increase_speed(self):
        self.__speed += 5

    def reduce_speed(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def reverse(self):
        self.__speed *= -1


car1 = Car('BMW', 'X5', 2008, 160)
car1.increase_speed()
car1.speed_get()
car1.increase_speed()
car1.speed_get()
car1.reduce_speed()
car1.reverse()
car1.speed_get()
car1.stop()
print(car1)
