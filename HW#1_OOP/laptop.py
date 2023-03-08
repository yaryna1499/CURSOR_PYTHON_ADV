from abc import ABC, abstractmethod

class Laptop(ABC):

    @abstractmethod
    def screen(self):
        pass

    @abstractmethod
    def keyboard(self):
        pass

    @abstractmethod
    def touchpad(self):
        pass

    @abstractmethod
    def webcam(self):
        pass

    @abstractmethod
    def ports(self):
        pass

    @abstractmethod
    def dynamics(self):
        pass


class HPLaptop(Laptop):
    def screen(self):
        print("Screen!")

    def keyboard(self):
        print("Keyboard")

    def touchpad(self):
        print("Touchpad")

    def webcam(self):
        print("Webcam")

    def ports(self):
        print("Ports")

    def dynamics(self):
        print("Dynamics!")



computer = HPLaptop()
computer.screen()
computer.keyboard()
computer.touchpad()
computer.webcam()
computer.ports()
computer.dynamics()
