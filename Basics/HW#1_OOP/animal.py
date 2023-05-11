class Animal:
    def __init__(self, is_wild: bool, weight, height):
        self.is_wild = is_wild
        self.weight = weight
        self.height = height

    def info(self):
        if self.is_wild:
            print(f"I`m a wild animal with {self.weight} kg of mass and {self.height} metres height!")
        else:
            print(f"I`m a home animal with {self.weight} kg of mass and {self.height} metres height!")

    def sleep(self):
        print("I am sleeping!")

    def eat(self):
        print("I am eating!")


class Dog(Animal):
    def bark(self):
        print("I am barking: woof, woof!")


class Tiger(Animal):
    def attack(self):
        print("I`m going to attack you because I`m a wild animal.")


class Frog(Animal):
    def say_kwa(self):
        print("Kwa kwa!")


class Cat(Animal):
    def say_meow(self):
        print("Meow!")


class Mouse(Animal):
    def say_pi(self):
        print("pi pi pi")


if __name__ == "__main__":
    dog = Dog(False, 50, 0.5)
    dog.info()

    cat = Cat(False, 1, 0.2)
    cat.say_meow()

    tiger = Tiger(True, 100, 1)
    tiger.eat()

    frog = Frog(True, 0.2, 0.04)
    frog.say_kwa()

    mouse = Mouse(True, 0.3, 0.3)
    mouse.sleep()
