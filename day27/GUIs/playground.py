def add(*args):
    sum = 0
    for num in args:
        sum += num
    return(sum)


print(add(2, 3, 4, 5, 7, 10, 8, 9))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)