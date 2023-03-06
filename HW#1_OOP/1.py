class Animal:
    def __init__(self, is_wild: bool, weight, height):
        self.weight = weight
        self.is_wild = is_wild
        self.height = height

    def info(self):
        if self.is_wild:
            return f"I`m a wild animal with {self.weight} kg of mass and {self.height} metres height!"
        else:
            return f"I`m a home animal with {self.weight} kg of mass and {self.height} metres height!"

    def sleep(self):
        return "I am sleeping!"

    def eat(self):
        return "I am eating!"


class Dog(Animal):
    def bark(self):
        return "I am barking: woof, woof!"

class Tiger(Animal):
    def attack(self):
        return "I`m going to attack you because I`m a wild animal."

class Frog(Animal):
    def say_kwa(self):
        return "Kwa kwa!"

class Cat(Animal):
    def say_meow(self):
        return "Meow!"

class Mouse(Animal):
    def say_pi(self):
        return "pi pi pi"

dog_Rex = Dog(False, 50, 0.5)
print(dog_Rex.info())

cat_Murchyk = Cat(False, 1, 0.2)
print(cat_Murchyk.say_meow())

tiger = Tiger(True, 100, 1)
print(tiger.eat())

frog = Frog(True, 0.2, 0.04)
print(frog.say_kwa())

mouse = Mouse(True, 0.3, 0.3)
print(mouse.sleep())
