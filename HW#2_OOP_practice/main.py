from person import Person
from realtor import Realtor
from random import randint

the_only_realtor = Realtor()
the_only_realtor.provide_info()
person_test = Person("Yaryna", 23, 100_000, "My home!")
# person_test.person_info()
# person_test.make_money(10000)
# print(person_test.money)
# person_test.make_money(10_000)
# print(person_test.money)
the_only_realtor.apply_discount()
person_test.buy_house()

p = 0.1
if randint(0, 1) >= p:
    the_only_realtor.steal_money()
    person_test.money = 0
else:
    print("I did not steal your money!")

