from animal import Animal

class Human(Animal):

    def info(self):
        return f"My name is {self.name}. I`m {self.height} cm tall and weigh {self.weight} kg."

    def study(self):
        return "I`m studying."

    def work(self):
        return "I`m working."


class Centaur(Human):

    def jump_over(self):
        return "I can jump over the mountain!"


centaur_object = Centaur(True, "Alpha", 100, 200)
print(centaur_object.info())
print(centaur_object.sleep())
print(centaur_object.jump_over())
print(centaur_object.work())
