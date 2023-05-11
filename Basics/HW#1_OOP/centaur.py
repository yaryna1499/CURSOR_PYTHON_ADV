from animal import Animal


class Human(Animal):
    def __init__(self, name, is_wild, weight, height):
        super().__init__(is_wild, weight, height)
        self.name = name

    def info(self):
        print(f"My name is {self.name}. I`m {self.height} cm tall and weigh {self.weight} kg.")

    def study(self):
        print("I`m studying.")

    def work(self):
        print("I`m working.")


class Centaur(Human):
    def __init__(self, name, is_wild, weight, height):
        super().__init__(name, is_wild, weight, height)

    def jump_over(self):
        print("I can jump over the mountain!")


if __name__ == "__main__":
    centaur_object = Centaur("Alpha", True, 100, 200)
    centaur_object.info()
    centaur_object.sleep()
    centaur_object.jump_over()
    centaur_object.work()
    print(centaur_object.is_wild)
