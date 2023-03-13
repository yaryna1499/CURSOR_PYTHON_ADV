from person import Person
from realtor import Realtor


the_only_realtor = Realtor()
the_only_realtor.provide_info()
person_test = Person("Yaryna", 23, 30_000, "My home!")
# person_test.person_info()
# person_test.make_money(10000)
# print(person_test.money)
# person_test.make_money(10_000)
# print(person_test.money)
the_only_realtor.apply_discount()
person_test.buy_house()
the_only_realtor.steal_money()

