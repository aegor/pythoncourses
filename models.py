from peewee import *
db = SqliteDatabase('people.db')

class People(Model):

    id = AutoField()
    firstName = CharField()
    is_relative = BooleanField()

    class Meta:
        database = db  # модель будет использовать базу данных 'people.db'

People.create_table()

def PeopleCreateMocks():
    People(firstName='Иван', is_relative=True).save()
    People(firstName='Маша', is_relative=True).save()
    People(firstName='Гриша', is_relative=False).save()
    People(firstName='Толя', is_relative=True).save()
    People(firstName='Коля', is_relative=False).save()

class PeopleProxy:
    def __init__(self, firstName="", is_relative=False):
        self.firstName = firstName
        self.is_relative = is_relative
