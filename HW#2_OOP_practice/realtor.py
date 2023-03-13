from house import House
from random import randint


class Realtor:
    instance_ = None

    def __new__(cls, *args, **kwargs):
        if cls.instance_ is None:
            cls.instance_ = super().__new__(cls)
        return cls.instance_

    def __init__(self):
        self.discount = randint(5, 20)
        self.r_name = 'Realtor Ivan'
        self.houses = [House(40, 30_000),
                       House(45, 35_000),
                       House(48, 40_000),
                       House(50, 49_000), ]

    def provide_info(self):
        print("Here is the list of available houses:\n")
        for h in self.houses:
            print(f"{self.houses.index(h)}) A house with area {h.area} sq. km. and it costs {h.cost}$\n")

    def apply_discount(self):
        print(f"Discount - {self.discount}%")
        for h in self.houses:
            h.cost *= 1 - self.discount / 100

    @staticmethod
    def steal_money():
        p = 0.1
        if randint(0, 1) >= p:
            print("I have stolen your money!")
        else:
            print("I did not steal your money!")

