from controller_peewee_test import *
import pickle

people1 = People(firstName='Иван', is_relative=True)
people2 = People(firstName='Маша', is_relative=True)
people3 = People(firstName='Гриша', is_relative=False)
people4 = People(firstName='Толя', is_relative=True)
people5 = People(firstName='Коля', is_relative=False)

f = open("example", "wba")
pickle.dump(people1, f)
pickle.dump(people2, f)
pickle.dump(people3, f)
pickle.dump(people4, f)
pickle.dump(people5, f)
f.close()

f = open("example", "rb")
value1 = pickle.load(f)
value2 = pickle.load(f)
value3 = pickle.load(f)
value4 = pickle.load(f)
value5 = pickle.load(f)
f.close()

print(value1.__dict__)
print(value2.__dict__)
print(value3.__dict__)
print(value4.__dict__)
print(value5.__dict__)
