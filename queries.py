from util import *
from models import People

def findPeopleByFirstName(name):
    return tojson(models_to_dict(People.select().where(People.firstName == name)))

def findPeopleByRelative(rel):
    return tojson(models_to_dict(People.select().where(People.is_relative == bool(rel))))

def findPeopleByRelativeAndFirstName(rel, name):
    return tojson(models_to_dict(People.select().where((People.is_relative == rel) & (People.firstName == name))))

def findPeopleAll():
    return  tojson(models_to_dict(People.select()))

def findPeopleByid(id):
    return tojson(models_to_dict(People.select().where(People.id == id)))