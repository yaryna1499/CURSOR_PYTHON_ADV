OOP


1. Сreate a class hierarchy of animals with at least 5 animals that have additional methods each, create an instance for each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class
class Animals:   
 """    
Parent class, should have eat, sleep    
"""

class Animal1(Animal):    
"""    
Some of the animal with 1-2 extra methods related to this animal    
"""

...
1.a. Create a new class Human and use multiple inheritance to create Centaur class, create an instance of Centaur class and call the common method of these classes and unique.

 class Human:    
"""    
Human class, should have eat, sleep, study, work    
"""

 class Centaur(.. , ..):    
"""    
Centaur class should be inherited from Human and Animal and has unique method related to it.   
 """
2. Сlass Profile:   
 """    
Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex    Override a printable string representation of Profile class and return: list of the params mentioned above    
"""

3.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamicsand create an HPLaptop class by using your interface.
