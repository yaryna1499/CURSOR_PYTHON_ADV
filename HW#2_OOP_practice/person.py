from realtor import Realtor

realtor = Realtor()


class Person:
    def __init__(self, name: str,
                 age: int, money: float,
                 home: str):
        self.name = name
        self.age = age
        self.money = money
        self.home = home
        self.info = dict(Name=self.name, Age=self.age, Money=self.money, Home=self.home)

    def person_info(self):
        print(self.info)

    def make_money(self, amount: float):
        self.money += amount
        return self.money

    def buy_house(self, my_choice=int(input("Please, choose the number of the house - "))):
        for h in realtor.houses:
            if realtor.houses.index(h) == my_choice and self.money >= h.cost:
                print(f'You bought a house with area {h.area} sq. km. and it costs {h.cost}$')
                realtor.houses.remove(h)
                self.money -= h.cost
            else:
                print("Please, choose from available houses or make money!")
