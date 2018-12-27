from peewee import *

db = SqliteDatabase('people.db')

class People(Model):
    firstName = CharField()
    is_relative = BooleanField()

    class Meta:
        database = db  # модель будет использовать базу данных 'people.db'

People.create_table()
people1 = People(firstName='Иван', is_relative=True)
people2 = People(firstName='Маша', is_relative=True)
people3 = People(firstName='Гриша', is_relative=False)
people4 = People(firstName='Толя', is_relative=True)
people5 = People(firstName='Коля', is_relative=False)

people1.save()
people2.save()
people3.save()
people4.save()
people5.save()

for people in People.select().where(People.is_relative == False):
    print(people.firstName + " родственник ли ?:" + str(people.is_relative))


for people in People.select():
    print(people.__dict__)

for people in People.select().where(People.firstName == 'Иван'):
   print(people.__dict__)

for people in People.select().where(People.is_relative == False):
   print(people.__dict__)


print(people1.__dict__)

print(people1.firstName + " родственник ли ? :" + people.is_relative)