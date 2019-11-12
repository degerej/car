# Joe Degere
# 11/11/19
# Homework


class Vehicle:
    def __init__(self, name, brand, shift, year ):
        self.name = name
        self.brand = brand
        self.shift = shift
        self.year = year

    def description(self):
        print(f"I'm gonna give you a tour of this vehicle: It is a {self.name} made in {self.year}.")
        print(f"This {self.name} is a {self.shift} just to be aware.")
        print(f"The car brand is {self.brand} and the year is {self.year}")

